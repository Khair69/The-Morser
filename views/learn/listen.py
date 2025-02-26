from tkinter import Frame
import customtkinter as CTk
import models.pref as pref
from PIL import Image

ASSETS_PATH = pref.get_base_path()

class LearnListenView(Frame):
    def __init__(self, master):
        super().__init__(master)

        #configs
        self.corner_rad = 15

        self.canvas = CTk.CTkCanvas(self, bg="#1F1F1F", height=768, width=1024, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.pack(fill="both", expand=True)

        #text area input
        self.text_area = CTk.CTkTextbox(self, font=("Segoe UI Variable Display", 16),  width=844.0, height=292.0,  bg_color="#1f1f1f", text_color="#bb6b44",corner_radius=10, fg_color="#191919")

        #back button
        self.back_button_image = CTk.CTkImage(Image.open(pref.relative_to_assets(ASSETS_PATH,"back_button.png")), size=(40,40))
        self.button_back = CTk.CTkButton(self, image=self.back_button_image, width=40.0, height=40.0, bg_color="#1f1f1f", fg_color="#1f1f1f", hover_color="#1f1f1f", corner_radius=0, text="")
        self.button_back.place(x=19.0, y=19.0)

        #settings button
        self.settings_button_image = CTk.CTkImage(Image.open(pref.relative_to_assets(ASSETS_PATH,"settings_button.png")), size=(40,40))
        self.button_settings = CTk.CTkButton(self, image=self.settings_button_image, width=40.0, height=40.0, bg_color="#1f1f1f", fg_color="#1f1f1f", hover_color="#1f1f1f", corner_radius=0, text="")
        self.button_settings.place(x=965.0, y=709.0)

        #enter button
        self.button_enter = CTk.CTkButton(self, width=250, height=50, text="Enter", font=("Segoe UI Variable Display Bold", 29), text_color="#191919", corner_radius=self.corner_rad, bg_color="#1F1F1F", fg_color="#bb6b44", hover_color="#874d31")

        #start button
        self.button_start = CTk.CTkButton(self, width=250, height=50, text="Start", font=("Segoe UI Variable Display Bold", 29), text_color="#191919", corner_radius=self.corner_rad, bg_color="#1F1F1F", fg_color="#bb6b44", hover_color="#874d31")
        self.button_start.place(x=315.0, y=600.0)

        #next button
        self.button_next = CTk.CTkButton(self, width=250, height=50, text="Next", font=("Segoe UI Variable Display Bold", 29), text_color="#191919", corner_radius=self.corner_rad, bg_color="#1F1F1F", fg_color="#bb6b44", hover_color="#874d31")

        #resault
        self.res_label = CTk.CTkLabel(self, bg_color="#1f1f1f", text_color="#bb6b44", font=("Segoe UI Variable Display Bold", 18), text="")

        #progbar
        self.prog_bar = CTk.CTkProgressBar(self, orientation="horizontal",bg_color="#1f1f1f", progress_color="#bb6b44", fg_color="#191919", width=844)
        self.prog_bar.set(0)

        #play button
        self.play_button_image = CTk.CTkImage(Image.open(pref.relative_to_assets(ASSETS_PATH,"play_button.png")), size=(40,40))
        self.button_play = CTk.CTkButton(self, image=self.play_button_image, width=40.0, height=40.0, bg_color="#1f1f1f", fg_color="#1f1f1f", hover_color="#1f1f1f", corner_radius=0, text="")

        #stop button
        self.stop_button_image = CTk.CTkImage(Image.open(pref.relative_to_assets(ASSETS_PATH,"pause_button.png")), size=(40,40))
        self.button_stop = CTk.CTkButton(self, image=self.stop_button_image, width=40.0, height=40.0, bg_color="#1f1f1f", fg_color="#1f1f1f", hover_color="#1f1f1f", corner_radius=0, text="")

        #new button
        self.button_custom = CTk.CTkButton(self, width=155, height=50, text="New", font=("Segoe UI Variable Display Bold", 29), text_color="#191919", corner_radius=self.corner_rad, bg_color="#1F1F1F", fg_color="#bb6b44", hover_color="#874d31")
        self.button_custom.place(x=580.0, y=600.0)

        #scrollabe frame
        self.choose_frame = CTk.CTkScrollableFrame(self, width=400, height=400, corner_radius=15, fg_color="#191919", bg_color="#1f1f1f", label_text="Choose a set of words", label_font=("Segoe UI Variable Display Bold", 18), label_anchor="w")
        self.choose_frame.place(x=312, y=100)
