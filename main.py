from create import Create


def AddTask(name, container):
    while True:
        t = input("Enter the task you wanna add: ")
        if t.lower() == "bas bhai":
            break
        for i in container:
            if i[0] == name:
                i.append(t)
    print("Task(s) added to the list!")


def RemoveTask(name, container):
    while True:
        t = input("Enter the task you wanna remove: ")
        if t.lower() == "bas bhai":
            break
        for i in container:
            if i[0] == name:
                i.remove(t)
    print("Task(s) removed from the list!")


def Completed(name, container):
    t = input("Enter the task you have completed: ")
    for i in container:
        if i[0] == name:
            i.remove(t)
    print(t, '✅')
    print("Congrats on completing the task. Keep going!!")


print('*'*120)
print("                                              ****** TO - DO - LIST ******")
print('*'*120)
n = 0
container = []

while n == 0:
    choice = int(input("""
    << MAIN MENU >>
1. Create a To - Do List
2. Use To - Do List
3. Remove To - Do List
4. Quit
Enter your choices : """))
                                                            # Create
    if choice == 1:
        n1 = 0
        while n1 == 0:
            name = input("Enter the name of the To - Do list: ")
            create = Create(name, container)

            print("List Created!")
            ch1 = int(input('''
        << CREATE >>
    1. Add Task
    2. Remove Task
    3. Mark as Completed ✅
    4. Quit
    Enter your Choice: '''))

            if ch1 == 1:
                AddTask(name, container)
            elif ch1 == 2:
                for i in container:
                    print(i, '\n')
                task = input("Enter the task you wanna remove: ")
                RemoveTask(name, container)
            elif ch1 == 3:
                task = input("Enter the task you wanna mark as completed: ")
                Completed(container, task)

            elif ch1 == 4:
                n1 = 1

            else:
                print("Wrong Choice! Try Again.")
                                                                # Use

    elif choice == 2:
        n2 = 0
        while n2 == 0:
            for i in container:
                print(i[0])
            n = input('Enter the name of the list you wanna use😈: ')
            ch2 = int(input('''
                << USE >>
            1. Add Task
            2. Remove Task
            3. Mark as Completed ✅
            4. Quit
            Enter your Choice: '''))
            if ch2 == 1:
                AddTask(n, container)
            elif ch2 == 2:
                RemoveTask(n, container)
            elif ch2 == 3:
                Completed(n, container)
            elif ch2 == 4:
                n2 = 1
            else:
                print("Wrong Choice! Try Again.")

                                                            #remove
    elif choice == 3:
        for i in container:
            print(i[0])
        t = input("Enter the list you wanna remove: ")
        for i in container:
            if t == i[0]:
                container.remove(i)
        print("List Successfully Removed!")

    elif choice == 4:
        n = 1
    else:
        print("Wrong Input! Try Again.")
