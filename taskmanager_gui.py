import tkinter as tk
from classes import TaskManager

manager = TaskManager()

# Display Task Manager using tkinter
def displayTaskManager():
    # Get Task Queue
    tasks = manager.displayQueue()

    # Add a task to the queue
    def addTask():
        # Get task description and priority from the tkinter textboxes: "desc_var" and "prrty_var"
        if (not ((desc_var.get() == "") and (prrty_var.get() == ""))):
            desc = desc_var.get()
            prrty = int(prrty_var.get())

            # Add the input task to the queue
            manager.addTask(desc, prrty)
        
        # Update the tkinter display
        updateDisplay()

    # Update the task queue display
    def updateDisplay():
        # Delete Previous Queue Display
        for widget in frame.winfo_children():
            widget.destroy()

        # Display New Queue
        tk.Label(frame, text="TASKS:").pack()
        for task in tasks:
            label = tk.Label(frame, text=("Task (id: #" + str(task.getID()) + ") Pr(" + str(task.getPriority())+ ")\n" + task.getDesc()))
            label.pack()


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
    # Button to to Add the input task
    add_button = tk.Button(inp_frame, text="Add Task", command=addTask)
    add_button.pack()


    # Task Queue Frame
    frame = tk.Frame()
    frame.grid(row=0, column=1, sticky="new")
    tk.Label(frame, text="TASKS:").pack()


    # Task History Frame
    hist_frame = tk.Frame()
    hist_frame.grid(row=0, column=3, sticky="new")
    tk.Label(hist_frame, text="Last Completed Task:").grid(row=1)


    # Run Display Window
    root.mainloop()

displayTaskManager()