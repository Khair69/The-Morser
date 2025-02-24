import customtkinter as CTk
import models.pref as pref

class Root(CTk.CTk):
    def __init__(self):
        super().__init__()

        CTk.set_appearance_mode("dark")
        #CTk.set_default_color_theme("red")

        self.title("The Morser")
        self.geometry("1024x768")
        self.resizable(False, False)
        self.iconbitmap(pref.relative_to_assets(pref.get_base_path(),"icon.ico"))