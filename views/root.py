from tkinter import Tk

class Root(Tk):
    def __init__(self):
        super().__init__()

        self.title("The Morser")
        self.geometry("1024x768")
        self.configure(bg="#1F1F1F")
        self.resizable(False, False)