from tkinter import Canvas, PhotoImage, Button, Frame
import models.pref as pref

ASSETS_PATH = pref.get_base_path()

class HomeView(Frame):
    def __init__(self, master):
        super().__init__(master, bg="#1F1F1F")

        #canvas or smth idk
        self.canvas = Canvas(self, bg="#1F1F1F", height=768, width=1024, bd=0, highlightthickness=0, relief="ridge")
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

        #go to translate page button
        self.translate_button_image = PhotoImage(file=pref.relative_to_assets(ASSETS_PATH,"translate_button.png"))
        self.button_translate = Button(self, image=self.translate_button_image, borderwidth=0, highlightthickness=0, relief="flat")
        self.button_translate.place(x=647.0, y=180.0, width=250.0, height=50.0)
        self.translate_button_image = self.translate_button_image

        #go to audio page button
        self.audio_button_image = PhotoImage(file=pref.relative_to_assets(ASSETS_PATH,"audio_button.png"))
        self.button_audio = Button(self, image=self.audio_button_image, borderwidth=0, highlightthickness=0, relief="flat")
        self.button_audio.place(x=647.0, y=540.0, width=250.0, height=50.0)
        self.audio_button_image = self.audio_button_image

        #go to learn page button
        self.learn_button_image = PhotoImage(file=pref.relative_to_assets(ASSETS_PATH,"learn_button.png"))
        self.button_learn = Button(self, image=self.learn_button_image, borderwidth=0, highlightthickness=0, relief="flat")
        self.button_learn.place(x=647.0, y=360.0, width=250.0, height=50.0)
        self.learn_button_image = self.learn_button_image
