## Classes Used in "PyTaskManager" Project

# Task Class
class Task:
    def __init__(self, description : str, priority : int):
        # Set Description of the task
        self.desc = description
        # Set ID of the task
        self.id = hash(description)
        # Set Priority of the task
        self.prty = priority
        # Initialize task as Incomplete
        self.completed = False