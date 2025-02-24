import customtkinter as CTk
class Root(CTk.CTk):
    def __init__(self):
        super().__init__()

        CTk.set_appearance_mode("dark")
        #CTk.set_default_color_theme("red")

        self.title("The Morser")
        self.geometry("1024x768")
        self.resizable(False, False)