class Create:

    def __init__(self, name: str, Container: list):
        assert len(name) > len(""), f"You can't make a to do list with no name!"
        taskList = []
        self.name = name
        self.Container = Container
        print("\nEnter 'bas bhai' when you're done.\n")
        taskList.append(name)
        while True:
            task = input("Enter your task: ")
            if task.lower() == "bas bhai":
                break
            taskList.append(task)
        Container.append(taskList)
        print(taskList[0],' : ')
        for i in taskList:
            if i == taskList[0]:
                continue
            print(i)
