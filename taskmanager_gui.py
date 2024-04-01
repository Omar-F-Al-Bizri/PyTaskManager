import tkinter as tk
from classes import TaskManager


# Display Task Manager using tkinter
def displayTaskManager():

    manager = TaskManager

    # Add a task to the queue
    def addTask():
        # Get task description and priority from the tkinter textboxes: "desc_var" and "prrty_var"
        if (not ((desc_var.get() == "") and (prrty_var.get() == ""))):
            desc = desc_var.get()
            prrty = int(prrty_var.get())

            # Add the input task to the queue
            manager.addTask(desc, prrty)


    # Display Window
    root = tk.Tk()
    root.geometry("800x500")
    root.title("Task Manager")


    # Task Input Frame
    inp_frame = tk.Frame()
    inp_frame.grid(row=0, column=0, sticky="new")
    # Input description of task
    # Label
    desc_label = tk.Label(inp_frame, text="Description")
    desc_label.pack()
    # Input
    desc_var = tk.StringVar()
    desc_entry = tk.Entry(inp_frame, textvariable=desc_var)
    desc_entry.pack()
    # Input Priority of task
    # Label
    prrty_label = tk.Label(inp_frame, text="Priority")
    prrty_label.pack()
    # Input
    prrty_var = tk.StringVar()
    prrty_entry = tk.Entry(inp_frame, textvariable=prrty_var)
    prrty_entry.pack()


    # Task Queue Frame
    frame = tk.Frame()
    frame.grid(row=0, column=1, sticky="new")
    tk.Label(frame, text="TASKS:").pack()


    # Run Display Window
    root.mainloop()

displayTaskManager()