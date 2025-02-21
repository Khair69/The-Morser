import models.pref as pref
from tkinter import Frame, Canvas, Button, PhotoImage, CENTER, Label


ASSETS_PATH = pref.get_base_path()

class LearnMenuView(Frame):
    def __init__(self,master):
        super().__init__(master, bg="#1F1F1F")

        self.canvas = Canvas(self, bg = "#1F1F1F", height = 768, width = 1024, bd = 0, highlightthickness = 0, relief = "ridge")
        self.canvas.pack(fill="both", expand=True)

        #image on the left
        self.main_image_image = PhotoImage(file=pref.relative_to_assets(ASSETS_PATH,"main_image.png"))
        self.canvas.create_image(256.0, 384.0, image=self.main_image_image)
        self.main_image = self.main_image_image  # Keep reference to prevent garbage collection


        #settings button
        self.settings_button_image = PhotoImage(file=pref.relative_to_assets(ASSETS_PATH,"settings_button.png"))
        self.button_settings = Button(self, image=self.settings_button_image, borderwidth=0, highlightthickness=0, relief="flat")
        self.button_settings.place(x=965.0, y=709.0, width=40.0, height=40.0)
        self.settings_button_image = self.settings_button_image
        
        #home button
        home_button_image = PhotoImage(file=pref.relative_to_assets(ASSETS_PATH,"home_button.png"))
        self.button_home = Button(self, image=home_button_image, borderwidth=0, highlightthickness=0, relief="flat")
        self.button_home.place(x=548.0, y=36.0, width=40.0, height=40.0)
        self.home_button_image = home_button_image
        
        #go to listen page button
        self.listen_button_image = PhotoImage(file=pref.relative_to_assets(ASSETS_PATH,"listen_button.png"))
        self.listen = Button(self, image=self.listen_button_image, borderwidth=0, highlightthickness=0, relief="flat")
        self.listen.place(x=647.0, y=540.0, width=250.0, height=50.0)
        self.listen_button_image = self.listen_button_image

        #go to letters page button
        self.letters_button_image = PhotoImage(file=pref.relative_to_assets(ASSETS_PATH,"letters_button.png"))
        self.letters = Button(self, image=self.letters_button_image, borderwidth=0, highlightthickness=0, relief="flat")
        self.letters.place(x=647.0, y=360.0, width=250.0, height=50.0)
        self.letters_button_image = self.letters_button_image  

        #go to translate page button
        self.translate_button_image = PhotoImage(file=pref.relative_to_assets(ASSETS_PATH,"translate_button.png"))
        self.button_translate = Button(self, image=self.translate_button_image, borderwidth=0, highlightthickness=0, relief="flat")
        self.button_translate.place(x=647.0, y=180.0, width=250.0, height=50.0)
        self.translate_button_image = self.translate_button_image

        #descriptions
        self.canvas.create_text(
            772.0,
            610.0,
            width=314.0,
            justify=CENTER,
            text="Listen to Morse Code and try to translate it to English",
            fill="#FFFFFF",
            font=("NotoSansArabic SemiBold", 15 * -1)
        )

        self.canvas.create_text(
            772.0,
            430.0,
            width=314.0,
            justify=CENTER,
            text="Learn the letters and symbols in Morse Code, and some other cool figures ",
            fill="#FFFFFF",
            font=("NotoSansArabic SemiBold", 15 * -1)
        )

        self.canvas.create_text(
            772.0,
            250.0,
            width=314.0,
            justify=CENTER,
            text=" A set of words to translate from English to Morse code or vice versa",
            fill="#FFFFFF",
            font=("NotoSansArabic SemiBold", 15 * -1)
        )
