import models.pref as pref
from tkinter import Frame, Canvas, Button, PhotoImage, CENTER, Label

ASSETS_PATH = pref.get_base_path()

class LearnLettersView(Frame):
    def __init__(self,master):
        super().__init__(master, bg="#1F1F1F")

        self.canvas = Canvas(self, bg = "#1F1F1F", height = 768, width = 1024, bd = 0, highlightthickness = 0, relief = "ridge")
        self.canvas.pack(fill="both", expand=True)

        #settings button
        self.settings_button_image = PhotoImage(file=pref.relative_to_assets(ASSETS_PATH,"settings_button.png"))
        self.button_settings = Button(self, image=self.settings_button_image, borderwidth=0, highlightthickness=0, relief="flat")
        self.button_settings.place(x=965.0, y=709.0, width=40.0, height=40.0)
        
        #home button
        self.home_button_image = PhotoImage(file=pref.relative_to_assets(ASSETS_PATH,"home_button.png"))
        self.button_home = Button(self, image=self.home_button_image, borderwidth=0, highlightthickness=0, relief="flat")
        self.button_home.place(x=90.0, y=56.0, width=40.0, height=40.0)

        #back button
        self.back_button_image = PhotoImage(file=pref.relative_to_assets(ASSETS_PATH,"back_button.png"))
        self.button_back = Button(self, image=self.back_button_image, borderwidth=0, highlightthickness=0, relief="flat")
        self.button_back.place(x=143.0, y=56.0, width=40.0, height=40.0)

        self.main_image_image = PhotoImage(file=pref.relative_to_assets(ASSETS_PATH,"International_Morse_Code.png"))
        self.canvas.create_image(511.0, 384.0, image=self.main_image_image)
