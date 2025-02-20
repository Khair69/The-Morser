from tkinter import Canvas, PhotoImage, Button, Frame, StringVar, Text, Label, END
from tkinter.ttk import Progressbar, Combobox
import controllers.pref as pref

ASSETS_PATH = pref.get_base_path()

class TranslateView(Frame):
    def __init__(self, master):
        super().__init__(master, bg="#1F1F1F")

        canvas = Canvas(self, bg="#1F1F1F", height=768, width=1024, bd=0, highlightthickness=0, relief="ridge")
        canvas.pack(fill="both", expand=True)

        #text area input
        text_area_image = PhotoImage(file=pref.relative_to_assets(ASSETS_PATH,"text_area.png"))
        canvas.create_image(512.0, 242.5, image=text_area_image)
        self.text_area_image = text_area_image  # Keep reference

        self.text_area = Text(self, bd=0, bg="#191919", fg="#F58B57", font=("Nato Sans Arabic", 16), highlightthickness=0)
        self.text_area.place(x=90.0, y=162.0, width=844.0, height=159.0)

        #output rect and line
        canvas.create_rectangle(90.0, 354.0, 934.0, 648.0, fill="#191919", outline="")
        canvas.create_rectangle(89.0, 646.9998177080748, 934.0, 648.0, fill="#F58B57", outline="")

        #output lable
        self.output_label = Label(self, bg="#191919", fg="#F58B57", font=("Nato Sans Arabic", 16), anchor="nw", justify="left",wraplength=844)
        self.output_label.place(x=90.0, y=354.0, width=844.0, height=159.0)

        #home button
        home_button_image = PhotoImage(file=pref.relative_to_assets(ASSETS_PATH,"home_button.png"))
        self.button_home = Button(self, image=home_button_image, borderwidth=0, highlightthickness=0, relief="flat")
        self.button_home.place(x=90.0, y=56.0, width=40.0, height=40.0)
        self.home_button_image = home_button_image

        #playbutton
        play_button_image = PhotoImage(file=pref.relative_to_assets(ASSETS_PATH,"play_button.png"))
        self.button_play = Button(self, image=play_button_image, borderwidth=0, highlightthickness=0, relief="flat")
        self.button_play.place(x=492.0, y=673.0, width=40.0, height=40.0)
        self.play_button_image = play_button_image

        #progressbar
        #canvas.create_rectangle( 89.0, 738.9999262151706, 934.0, 740.0, fill="#FFFFFF", outline="")
        # Create a progress bar
        self.progress_bar = Progressbar(self, orient="horizontal", length=845, mode="determinate")
        self.progress_bar.place(x=89, y=738.9999262151706, )

        self.translation_mode = StringVar(value="English to Morse")
        # Create combo box for mode selection
        canvas.create_rectangle(684.0, 51.0, 934.0, 101.0, fill="#191919", outline="")
        self.combo_box = Combobox(self, state="readonly", textvariable=self.translation_mode ,font=("Nato Sans Arabic", 12))
        self.combo_box["values"] = ("English to Morse", "Morse to English")
        self.combo_box.place(x=684, y=51, width=250, height=50)