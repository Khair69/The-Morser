from tkinter import Frame
import customtkinter as CTk
import models.pref as pref
from PIL import Image

ASSETS_PATH = pref.get_base_path()

class LearnLettersView(Frame):
    def __init__(self,master):
        super().__init__(master)

        self.canvas = CTk.CTkCanvas(self, bg="#1F1F1F", height=768, width=1024, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.pack(fill="both", expand=True)

        #settings button
        self.settings_button_image = CTk.CTkImage(Image.open(pref.relative_to_assets(ASSETS_PATH,"settings_button.png")), size=(40,40))
        self.button_settings = CTk.CTkButton(self, image=self.settings_button_image, width=40.0, height=40.0, bg_color="#1f1f1f", fg_color="#1f1f1f", hover_color="#1f1f1f", corner_radius=0, text="")
        self.button_settings.place(x=965.0, y=709.0)
        
        #home button
        self.home_button_image = CTk.CTkImage(Image.open(pref.relative_to_assets(ASSETS_PATH,"home_button.png")), size=(40,40))
        self.button_home = CTk.CTkButton(self, image=self.home_button_image, width=40.0, height=40.0, bg_color="#1f1f1f", fg_color="#1f1f1f", hover_color="#1f1f1f", corner_radius=0, text="")
        self.button_home.place(x=10.0, y=10.0)

        #back button
        self.back_button_image = CTk.CTkImage(Image.open(pref.relative_to_assets(ASSETS_PATH,"back_button.png")), size=(40,40))
        self.button_back = CTk.CTkButton(self, image=self.back_button_image, width=40.0, height=40.0, bg_color="#1f1f1f", fg_color="#1f1f1f", hover_color="#1f1f1f", corner_radius=0, text="")
        self.button_back.place(x=63.0, y=10.0)

        self.letters_image_image = CTk.CTkImage(dark_image=Image.open(pref.relative_to_assets(ASSETS_PATH,"International_Morse_Code.png")), size=(563,704))
        self.img_label = CTk.CTkLabel(self, text="", image=self.letters_image_image, bg_color="#1F1F1F")
        self.img_label.place(x=230.5, y=32)
