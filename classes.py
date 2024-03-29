## Classes Used in "PyTaskManager" Project

# Task Class
class Task:
    # ID class variable
    increment_ID = 0

    # Constructor Method
    def __init__(self, description : str, priority : int):
        # Set Description of the task
        self.__desc = description
        # Set ID of the task Incrementally
        Task.increment_ID += 1
        self.__id = self.increment_ID
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
        return {"desc": self.__desc, "id": self.__id, "priority": self.__prty, "status": self.__completed}


#Task Queue Class to store Tasks
class TaskQueue():
    # Constructor Method
    def __init__(self):
        self.__lst = []

    # Check if task queue is empty
    def isEmpty(self):
        return (len(self.__lst) == 0)

    # Add an item with priority
    def enqueue(self, task : Task):
        # Case 1: List is empty
        if self.isEmpty():
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
    
    # Mark first item as complete
    def markComplete(self):
        self.__lst[0].setCompleted(True)

    # Display Priority Queue
    def displayQueue(self):
        return self.__lst
    

# Stack Class to store completed tasks
class Stack():
    # Constructor Method
    def __init__(self):
        self.__lst = []

    # Check if stack is empty
    def isEmpty(self):
        return (len(self.__lst) == 0)

    # Add item to top of stack
    def push(self, task : Task):
        # Add item to beginning of list
        self.__lst.insert(0, task)

    # Remove item from top of stack
    def pop(self):
        # Case 1: List is empty
        if self.isEmpty():
            # Inform User that list is empty
            print("Empty")
            return
        # Case 2: List not empty
        else:
            # remove and return first item in list
            return self.__lst.pop(0)
    
    # Display Stack
    def displayStack(self):
        return self.__lst
        
    # See top of stack
    def peek(self):
        # Case 1: List empty
        if (self.isEmpty()):
            return None
        # Case 2: List not empty
        else:
            # Return first item in stack
            return self.__lst[0]
        

# Task Manager Classs to manage all tasks
class TaskManager():
    # Constructor Method
    def __init__(self):
        self.__task_queue = TaskQueue()
        self.__task_history = Stack()

    # Add New task to task queue
    def addTask(self, task : str, priority : int):
        self.__task_queue.enqueue(Task(task, priority))

    # Get task using id
    def getTask(self, id : int):
        for i in range(len(self.__task_queue)):
            if (self.__task_queue[i].getID() == id):
                return self.__task_queue[i]
        return -1
    
    # Mark top task as complete
    def completeTask(self):
        # Case 1: List is empty
        if self.__task_queue.isEmpty():
            # Inform user that list is empty
            print("Empty")
        # Case 2: List not empty
        else:
            # Mark first task as complete
            self.__task_queue.markComplete()
            # Move first item in task queue to top of task history
            self.__task_history.push(self.__task_queue.dequeue())

    # Display task queue
    def displayQueue(self):
        return self.__task_queue.displayQueue()

    # Display task history
    def displayHistory(self):
        return self.__task_history.displayStack()

    # Display last completed task
    def peekDisplay(self):
        return self.__task_history.peek()