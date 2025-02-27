import customtkinter as CTk
import models.pref as pref
from PIL import Image
from tkinter import Frame, CENTER

ASSETS_PATH = pref.resource_path("data/assets/")

class LearnMenuView(Frame):
    def __init__(self,master):
        super().__init__(master)

        #configs
        self.corner_rad = 15

        self.canvas = CTk.CTkCanvas(self, bg="#1F1F1F", height=768, width=1024, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.pack(fill="both", expand=True)

        #image on the left
        self.main_image = CTk.CTkImage(dark_image=Image.open(ASSETS_PATH+"main_image.png"), size=(512,768))
        self.img_label = CTk.CTkLabel(self, text="", image=self.main_image, bg_color="#1F1F1F")
        self.img_label.place(x=0, y=0)

        #settings button
        self.settings_button_image = CTk.CTkImage(Image.open(ASSETS_PATH+"settings_button.png"), size=(40,40))
        self.button_settings = CTk.CTkButton(self, image=self.settings_button_image, width=40.0, height=40.0, bg_color="#1f1f1f", fg_color="#1f1f1f", hover_color="#1f1f1f", corner_radius=0, text="")
        self.button_settings.place(x=965.0, y=709.0)
        
        #home button
        self.home_button_image = CTk.CTkImage(Image.open(ASSETS_PATH+"home_button.png"), size=(40,40))
        self.button_home = CTk.CTkButton(self, image=self.home_button_image, width=40.0, height=40.0, bg_color="#1f1f1f", fg_color="#1f1f1f", hover_color="#1f1f1f", corner_radius=0, text="")
        self.button_home.place(x=548.0, y=36.0)
        
        #go to translate page button
        self.button_translate = CTk.CTkButton(self, width=250, height=50, text="Translate", font=("Segoe UI Variable Display Bold", 29), text_color="#191919", corner_radius=self.corner_rad, bg_color="#1F1F1F", fg_color="#bb6b44", hover_color="#874d31")
        self.button_translate.place(x=647.0, y=180.0)

        #go to letters page button
        self.button_letters = CTk.CTkButton(self, width=250, height=50, text="Letters", font=("Segoe UI Variable Display Bold", 29), text_color="#191919", corner_radius=self.corner_rad, bg_color="#1F1F1F", fg_color="#bb6b44", hover_color="#874d31")
        self.button_letters.place(x=647.0, y=360.0)

        #go to listen page button
        self.button_listen = CTk.CTkButton(self, width=250, height=50, text="Listen", font=("Segoe UI Variable Display Bold", 29), text_color="#191919", corner_radius=self.corner_rad, bg_color="#1F1F1F", fg_color="#bb6b44", hover_color="#874d31")
        self.button_listen.place(x=647.0, y=540.0)

        #descriptions
        self.canvas.create_text(
            772.0,
            250.0,
            width=314.0,
            justify=CENTER,
            text=" A set of words to translate from English to Morse code or vice versa",
            fill="#FFFFFF",
            font=("Segoe UI Variable Display", 12)
        )

        self.canvas.create_text(
            772.0,
            430.0,
            width=314.0,
            justify=CENTER,
            text="Learn the letters and symbols in Morse Code, and some other cool figures ",
            fill="#FFFFFF",
            font=("Segoe UI Variable Display", 12)
        )

        self.canvas.create_text(
            772.0,
            610.0,
            width=314.0,
            justify=CENTER,
            text="Listen to Morse Code and try to translate it to English",
            fill="#FFFFFF",
            font=("Segoe UI Variable Display", 12)
        )