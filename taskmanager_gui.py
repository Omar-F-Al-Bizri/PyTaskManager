import tkinter as tk


class GUI():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Py Task Manager")
        self.root.geometry("800x500")

        self.root.mainloop()


app = GUI()