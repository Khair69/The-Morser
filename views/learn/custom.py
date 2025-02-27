from tkinter import Frame
import customtkinter as CTk
import models.pref as pref
from PIL import Image

ASSETS_PATH = pref.resource_path("data/assets/")

class LearnCustomView(Frame):
    def __init__(self, master):
        super().__init__(master)

        #configs
        self.corner_rad = 15

        self.canvas = CTk.CTkCanvas(self, bg="#1F1F1F", height=768, width=1024, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.pack(fill="both", expand=True)

        #back button
        self.back_button_image = CTk.CTkImage(Image.open(ASSETS_PATH+"back_button.png"), size=(40,40))
        self.button_back = CTk.CTkButton(self, image=self.back_button_image, width=40.0, height=40.0, bg_color="#1f1f1f", fg_color="#1f1f1f", hover_color="#1f1f1f", corner_radius=0, text="")
        self.button_back.place(x=19.0, y=19.0)

        #settings button
        self.settings_button_image = CTk.CTkImage(Image.open(ASSETS_PATH+"settings_button.png"), size=(40,40))
        self.button_settings = CTk.CTkButton(self, image=self.settings_button_image, width=40.0, height=40.0, bg_color="#1f1f1f", fg_color="#1f1f1f", hover_color="#1f1f1f", corner_radius=0, text="")
        self.button_settings.place(x=965.0, y=709.0)

        #word entry
        self.inp_word = CTk.CTkEntry(self,width=600, height=50, font=("Segoe UI Variable Display SemiBold", 29), placeholder_text="word", corner_radius=self.corner_rad, fg_color="#191919", bg_color="#1f1f1f", text_color="#bb6b44", placeholder_text_color="#3f3f3f")
        self.inp_word.place(x=100, y=350)

        #add button
        self.button_add = CTk.CTkButton(self, width=150, height=50, text="Add", font=("Segoe UI Variable Display Bold", 29), text_color="#191919", corner_radius=self.corner_rad, bg_color="#1F1F1F", fg_color="#bb6b44", hover_color="#874d31")
        self.button_add.place(x=730.0, y=350.0)

        #save button
        self.button_save = CTk.CTkButton(self, width=250, height=50, text="Save", font=("Segoe UI Variable Display Bold", 29), text_color="#191919", corner_radius=self.corner_rad, bg_color="#1F1F1F", fg_color="#bb6b44", hover_color="#874d31")
        self.button_save.place(x=387.0, y=600.0)

        #desc
        self.desc_label = CTk.CTkLabel(self, text="Add words then click save", font=("Segoe UI Variable Display Bold", 29), text_color="#bb6b44", bg_color="#1f1f1f")
        self.desc_label.place(x=110, y=230)