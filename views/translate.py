from tkinter import Frame, StringVar
import customtkinter as CTk
import models.pref as pref
from PIL import Image

ASSETS_PATH = pref.get_base_path()

class TranslateView(Frame):
    def __init__(self, master):
        super().__init__(master)

        self.canvas = CTk.CTkCanvas(self, bg="#1F1F1F", height=768, width=1024, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.pack(fill="both", expand=True)

        #text area input
        self.text_area = CTk.CTkTextbox(self, font=("Segoe UI Variable Display", 16), width=844, height=159,  bg_color="#1f1f1f", text_color="#bb6b44",corner_radius=10, fg_color="#191919")
        self.text_area.place(x=90.0, y=162.0)

        #output rect
        self.output_rect = self.round_rectangle(90.0, 354.0, 934.0, 648.0, r=10, fill="#191919")

        #output lable
        self.output_label = CTk.CTkLabel(self, bg_color="#191919", text_color="#bb6b44", font=("Segoe UI Variable Display Bold", 28), anchor="nw", justify="left",wraplength=824, width=824.0, height=282 ,text="")
        self.output_label.place(x=100.0, y=360.0)

        #home button
        self.home_button_image = CTk.CTkImage(Image.open(pref.relative_to_assets(ASSETS_PATH,"home_button.png")), size=(40,40))
        self.button_home = CTk.CTkButton(self, image=self.home_button_image, width=40.0, height=40.0, bg_color="#1f1f1f", fg_color="#1f1f1f", hover_color="#1f1f1f", corner_radius=0, text="")
        self.button_home.place(x=90.0, y=56.0)

        #playbutton
        self.play_button_image = CTk.CTkImage(Image.open(pref.relative_to_assets(ASSETS_PATH,"play_button.png")), size=(40,40))
        self.button_play = CTk.CTkButton(self, image=self.play_button_image, width=40.0, height=40.0, bg_color="#1f1f1f", fg_color="#1f1f1f", hover_color="#1f1f1f", corner_radius=0, text="")
        self.button_play.place(x=492.0, y=673.0)

        #stop button
        self.stop_button_image = CTk.CTkImage(Image.open(pref.relative_to_assets(ASSETS_PATH,"pause_button.png")), size=(40,40))
        self.button_stop = CTk.CTkButton(self, image=self.stop_button_image, width=40.0, height=40.0, bg_color="#1f1f1f", fg_color="#1f1f1f", hover_color="#1f1f1f", corner_radius=0, text="")

        """
        #progressbar
        #canvas.create_rectangle( 89.0, 738.9999262151706, 934.0, 740.0, fill="#FFFFFF", outline="")
        # Create a progress bar
        self.progress_bar = Progressbar(self, orient="horizontal", length=845, mode="determinate")
        self.progress_bar.place(x=89, y=738.9999262151706, )
        """

        self.translation_mode = StringVar(value="English to Morse")
        modes = ["English to Morse", "Morse to English"]
        # Create combo box for mode selection
        self.combo_box = CTk.CTkComboBox(self, values=modes , font=("Segoe UI Variable Display Bold", 18), dropdown_font=("Segoe UI Variable Display Bold", 18), width=250, height=50, corner_radius=25, bg_color="#1f1f1f", border_color="#bb6b44", button_color="#bb6b44", button_hover_color="#874d31", text_color="#808080")
        self.combo_box["values"] = ("English to Morse", "Morse to English")
        self.combo_box.place(x=684, y=51)

    #func to create rounded rect
    def round_rectangle(self, x1, y1, x2, y2, r=25, **kwargs):    
        points = (x1+r, y1, x1+r, y1, x2-r, y1, x2-r, y1, x2, y1, x2, y1+r, x2, y1+r, x2, y2-r, x2, y2-r, x2, y2, x2-r, y2, x2-r, y2, x1+r, y2, x1+r, y2, x1, y2, x1, y2-r, x1, y2-r, x1, y1+r, x1, y1+r, x1, y1)
        return self.canvas.create_polygon(points, **kwargs, smooth=True)