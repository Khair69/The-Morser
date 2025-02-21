import models.pref as pref
from tkinter import Canvas, Button, PhotoImage, Frame

ASSETS_PATH = pref.get_base_path()

class LearnLangMenuView(Frame):
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

        #go to m2e page button
        self.m2e_button_image = PhotoImage(file=pref.relative_to_assets(ASSETS_PATH,"m2e_button.png"))
        self.button_m2e = Button(self, image=self.m2e_button_image, borderwidth=0, highlightthickness=0, relief="flat")
        self.button_m2e.place(x=647.0, y=449.0, width=250.0, height=50.0)
        self.m2e_button_image = self.m2e_button_image  

        #go to e2m page button
        self.e2m_button_image = PhotoImage(file=pref.relative_to_assets(ASSETS_PATH,"e2m_button.png"))
        self.button_e2m = Button(self, image=self.e2m_button_image, borderwidth=0, highlightthickness=0, relief="flat")
        self.button_e2m.place(x=647.0, y=269.0, width=250.0, height=50.0)
        self.e2m_button_image = self.e2m_button_image  

        #back button
        back_button_image = PhotoImage(file=pref.relative_to_assets(ASSETS_PATH,"back_button.png"))
        self.button_back = Button(self, image=back_button_image, borderwidth=0, highlightthickness=0, relief="flat")
        self.button_back.place(x=601.0, y=36.0, width=40.0, height=40.0)
        self.back_button_image = back_button_image  