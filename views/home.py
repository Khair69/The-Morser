from tkinter import Frame
import models.pref as pref
import customtkinter as CTk
from PIL import Image

ASSETS_PATH = pref.get_base_path()

class HomeView(Frame):
    def __init__(self, master):
        super().__init__(master)
        
        #configs
        self.corner_rad = 15

        #canvas or smth idk
        self.canvas = CTk.CTkCanvas(self, bg="#1F1F1F", height=768, width=1024, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.pack(fill="both", expand=True)

        #image on the left
        self.main_image = CTk.CTkImage(dark_image=Image.open(pref.relative_to_assets(ASSETS_PATH,"main_image.png")), size=(512,768))
        self.img_label = CTk.CTkLabel(self, text="", image=self.main_image, bg_color="#1F1F1F")
        self.img_label.place(x=0, y=0)

        #settings button
        self.settings_button_image = CTk.CTkImage(Image.open(pref.relative_to_assets(ASSETS_PATH,"settings_button.png")), size=(40,40))
        self.button_settings = CTk.CTkButton(self, image=self.settings_button_image, width=40.0, height=40.0, bg_color="#1f1f1f", fg_color="#1f1f1f", hover_color="#1f1f1f", corner_radius=0, text="")
        self.button_settings.place(x=965.0, y=709.0)

        #go to translate page button
        self.button_translate = CTk.CTkButton(self, width=250, height=50, text="Translate", font=("Segoe UI Variable Display Bold", 29), text_color="#191919", corner_radius=self.corner_rad, bg_color="#1F1F1F", fg_color="#bb6b44", hover_color="#874d31")
        self.button_translate.place(x=647.0, y=270.0)
    
        #go to learn page button
        self.button_learn = CTk.CTkButton(self, width=250, height=50, text="Learn", font=("Segoe UI Variable Display Bold", 29), text_color="#191919", corner_radius=self.corner_rad, bg_color="#1F1F1F", fg_color="#bb6b44", hover_color="#874d31")
        self.button_learn.place(x=647.0, y=450.0)
