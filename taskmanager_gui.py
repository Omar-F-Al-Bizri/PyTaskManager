import tkinter as tk


# Display Task Manager using tkinter
def displayTaskManager():
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

    # Run Display Window
    root.mainloop()

displayTaskManager()