from tkinter import Canvas,Text, Button, PhotoImage,Frame, Label, CENTER
import models.pref as pref

ASSETS_PATH = pref.get_base_path()

class LearnTranslateView(Frame):
    def __init__(self, master):
        super().__init__(master, bg="#1F1F1F")

        self.canvas = Canvas(self, bg="#1F1F1F", height=768, width=1024, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.pack(fill="both", expand=True)

        #text area input
        text_area_image = PhotoImage(file=pref.relative_to_assets(ASSETS_PATH,"text_area2.png"))
        self.canvas.create_image(512.0, 468.0, image=text_area_image)
        self.text_area_image = text_area_image  # Keep reference

        self.text_area = Text(self, bd=0, bg="#191919", fg="#F58B57", font=("Nato Sans Arabic", 16), highlightthickness=0)
        self.text_area.place(x=90.0, y=321.0, width=844.0, height=292.0)


        self.canvas.create_rectangle(89.0, 613.9998177080747, 934.0, 615.0, fill="#F58B57", outline="")

        #home button
        home_button_image = PhotoImage(file=pref.relative_to_assets(ASSETS_PATH,"home_button.png"))
        self.button_home = Button(self, image=home_button_image, borderwidth=0, highlightthickness=0, relief="flat")
        self.button_home.place(x=90.0, y=56.0, width=40.0, height=40.0)
        self.home_button_image = home_button_image

        #back button
        back_button_image = PhotoImage(file=pref.relative_to_assets(ASSETS_PATH,"back_button.png"))
        self.button_back = Button(self, image=back_button_image, borderwidth=0, highlightthickness=0, relief="flat")
        self.button_back.place(x=143.0, y=56.0, width=40.0, height=40.0)
        self.back_button_image = back_button_image  

        #settings button
        self.settings_button_image = PhotoImage(file=pref.relative_to_assets(ASSETS_PATH,"settings_button.png"))
        self.button_settings = Button(self, image=self.settings_button_image, borderwidth=0, highlightthickness=0, relief="flat")
        self.button_settings.place(x=965.0, y=709.0, width=40.0, height=40.0)
        self.settings_button_image = self.settings_button_image

        #go to enter page button
        self.enter_button_image = PhotoImage(file=pref.relative_to_assets(ASSETS_PATH,"enter_button.png"))
        self.button_enter = Button(self, image=self.enter_button_image, borderwidth=0, highlightthickness=0, relief="flat")
        self.button_enter.place(x=387.0, y=663.0, width=250.0, height=50.0)
        self.enter_button_image = self.enter_button_image

        self.word_label = Label(self,bg="#1f1f1f", fg="#F58B57", font=("Nato Sans Arabic Black", 40 * -1))
        self.word_label.place(x=512.0, y=177.0,anchor=CENTER)
