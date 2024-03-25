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


# Priority Queue Class to store Tasks
class priorityQueue():
    # Constructor Method
    def __init__(self):
        self.__lst = []

    # Add an item with priority
    def enqueue(self, task : Task):
        # Case 1: List is empty
        if len(self.__lst) == 0:
            self.__lst.append(task)
        # Case 2: List not empty
        else:
            current = 0
            while self.__lst[current].getPriority() > task.getPriority():
                # Sub-Case 1: Reached end of List
                if current == len(self.__lst) - 1:
                    # Add the item at the end
                    self.__lst.append(task)
                    return
                # Sub-Case 2: Not end of List
                else:
                    # Move to the next item in the list
                    current += 1
            # Add the item in its position
            self.__lst.insert(current, task)
            return

    # Remove item with highest priority
    def dequeue(self):
        # Case 1: List is empty
        if len(self.__lst) == 0:
            # Inform user that list is empty
            print("Empty")
            return
        # Case 2: List not empty
        else:
            # Remove and Return first item in list
            return self.__lst.pop(0)
    
    def displayQueue(self):
        if len(self.__lst) == 0:
            print("Empty")
        else:
            for i in range(len(self.__lst)):
                self.__lst[i].displayTask()
                print()
        return