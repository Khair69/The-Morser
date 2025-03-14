from tkinter import Frame
import customtkinter as CTk
import models.pref as pref
from PIL import Image

ASSETS_PATH = pref.resource_path("data/assets/")

class LearnTranslateView(Frame):
    def __init__(self, master):
        super().__init__(master)

        #configs
        self.corner_rad = 15

        self.canvas = CTk.CTkCanvas(self, bg="#1F1F1F", height=768, width=1024, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.pack(fill="both", expand=True)

        #text area input
        self.text_area = CTk.CTkTextbox(self, font=("Segoe UI Variable Display", 16),  width=844.0, height=292.0,  bg_color="#1f1f1f", text_color="#bb6b44",corner_radius=10, fg_color="#191919")

        #back button
        self.back_button_image = CTk.CTkImage(Image.open(ASSETS_PATH+"back_button.png"), size=(40,40))
        self.button_back = CTk.CTkButton(self, image=self.back_button_image, width=40.0, height=40.0, bg_color="#1f1f1f", fg_color="#1f1f1f", hover_color="#1f1f1f", corner_radius=0, text="")
        self.button_back.place(x=19.0, y=19.0)

        #settings button
        self.settings_button_image = CTk.CTkImage(Image.open(ASSETS_PATH+"settings_button.png"), size=(40,40))
        self.button_settings = CTk.CTkButton(self, image=self.settings_button_image, width=40.0, height=40.0, bg_color="#1f1f1f", fg_color="#1f1f1f", hover_color="#1f1f1f", corner_radius=0, text="")
        self.button_settings.place(x=965.0, y=709.0)

        #e2m
        self.button_e2m = CTk.CTkButton(self, width=250, height=50, text="English to Morse", font=("Segoe UI Variable Display Bold", 29), text_color="#191919", corner_radius=self.corner_rad, bg_color="#1F1F1F", fg_color="#bb6b44", hover_color="#874d31")
        self.button_e2m.place(x=387.0, y=269.0)

        #m2e
        self.button_m2e = CTk.CTkButton(self, width=250, height=50, text="Morse to English", font=("Segoe UI Variable Display Bold", 29), text_color="#191919", corner_radius=self.corner_rad, bg_color="#1F1F1F", fg_color="#bb6b44", hover_color="#874d31")
        self.button_m2e.place(x=387.0, y=449.0)

        #enter button
        self.button_enter = CTk.CTkButton(self, width=250, height=50, text="Enter", font=("Segoe UI Variable Display Bold", 29), text_color="#191919", corner_radius=self.corner_rad, bg_color="#1F1F1F", fg_color="#bb6b44", hover_color="#874d31")

        #start button
        self.button_start = CTk.CTkButton(self, width=250, height=50, text="Start", font=("Segoe UI Variable Display Bold", 29), text_color="#191919", corner_radius=self.corner_rad, bg_color="#1F1F1F", fg_color="#bb6b44", hover_color="#874d31")

        #next button
        self.button_next = CTk.CTkButton(self, width=250, height=50, text="Next", font=("Segoe UI Variable Display Bold", 29), text_color="#191919", corner_radius=self.corner_rad, bg_color="#1F1F1F", fg_color="#bb6b44", hover_color="#874d31")

        #output
        self.word_label = CTk.CTkLabel(self, bg_color="#1f1f1f", text_color="#bb6b44", font=("Segoe UI Variable Display Semibold", 32) ,text="", wraplength=1000)

        #resault
        self.res_label = CTk.CTkLabel(self, bg_color="#1f1f1f", text_color="#bb6b44", font=("Segoe UI Variable Display Bold", 18), text="")

        #progbar
        self.prog_bar = CTk.CTkProgressBar(self, orientation="horizontal",bg_color="#1f1f1f", progress_color="#bb6b44", fg_color="#191919", width=844)
        self.prog_bar.set(0)

        #new button
        self.button_custom = CTk.CTkButton(self, width=155, height=50, text="New", font=("Segoe UI Variable Display Bold", 29), text_color="#191919", corner_radius=self.corner_rad, bg_color="#1F1F1F", fg_color="#bb6b44", hover_color="#874d31")

        #scrollabe frame
        self.choose_frame = CTk.CTkScrollableFrame(self, width=400, height=400, corner_radius=15, fg_color="#191919", bg_color="#1f1f1f", label_text="Choose a set of words", label_font=("Segoe UI Variable Display Bold", 18), label_anchor="w")


