## Classes Used in "PyTaskManager" Project

# Task Class
class Task:
    # Constructor Method
    def __init__(self, description : str, priority : int):
        # Set Description of the task
        self.__desc = description
        # Set ID of the task
        self.__id = hash(description)
        # Set Priority of the task
        self.__prty = priority
        # Initialize task as Incomplete
        self.__completed = False

    # Getters
    def getDesc(self):
        return self.__desc
    def getID(self):
        return self.__id
    def getPriority(self):
        return self.__prty
    def isCompleted(self):
        return self.__completed
    
    # Setters
    def setCompleted(self, status : bool):
        self.__completed = status
        return

    # Display Task
    def displayTask(self):
        print("Task:", self.__desc, "(id: #" + str(self.__id) + ")")
        print("Priority:", self.__prty)
        print("Completed:", self.__completed)