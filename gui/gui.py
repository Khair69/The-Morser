import tkinter as tk
from tkinter import Canvas, Button, PhotoImage, Entry, Text, Button, PhotoImage
from pathlib import Path
import sys
from logic.translator import Translator

# Function to get the base path for assets (for cross-platform compatibility)
def get_base_path():
    if hasattr(sys, "_MEIPASS"):
        return Path(sys._MEIPASS) / "assets"
    return Path(__file__).parent / "assets"

ASSETS_PATH = get_base_path()

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

#translator object
translator = Translator()

# Main Application Class
class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("The Morser")
        self.geometry("1024x768")
        self.configure(bg="#1F1F1F")
        self.resizable(False, False)

        # Dictionary to store frames (pages)
        self.frames = {}

        # Initialize pages
        for Page in (MainPage, TranslatePage):
            frame = Page(self)
            self.frames[Page] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(MainPage)  # Show the main page initially

    def show_frame(self, page):
        """Raise the selected frame to the front."""
        frame = self.frames[page]
        frame.tkraise()

# Main Page Class
class MainPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="#1F1F1F")

        canvas = Canvas(self, bg="#1F1F1F", height=768, width=1024, bd=0, highlightthickness=0, relief="ridge")
        canvas.pack(fill="both", expand=True)

        main_image_image = PhotoImage(file=relative_to_assets("main_image.png"))
        canvas.create_image(256.0, 384.0, image=main_image_image)
        self.main_image = main_image_image  # Keep reference to prevent garbage collection

        settings_button_image = PhotoImage(file=relative_to_assets("settings_button.png"))
        button_settings = Button(self, image=settings_button_image, borderwidth=0, highlightthickness=0, command=lambda: print("SETTINGS clicked"), relief="flat")
        button_settings.place(x=965.0, y=709.0, width=40.0, height=40.0)
        self.settings_button_image = settings_button_image

        translate_button_image = PhotoImage(file=relative_to_assets("translate_button.png"))
        button_translate = Button(self, image=translate_button_image, borderwidth=0, highlightthickness=0, command=lambda: master.show_frame(TranslatePage), relief="flat")
        button_translate.place(x=647.0, y=180.0, width=250.0, height=50.0)
        self.translate_button_image = translate_button_image

        audio_button_image = PhotoImage(file=relative_to_assets("audio_button.png"))
        button_audio = Button(self, image=audio_button_image, borderwidth=0, highlightthickness=0, command=lambda: print("AUDIO clicked"), relief="flat")
        button_audio.place(x=647.0, y=540.0, width=250.0, height=50.0)
        self.audio_button_image = audio_button_image

        learn_button_image = PhotoImage(file=relative_to_assets("learn_button.png"))
        button_learn = Button(self, image=learn_button_image, borderwidth=0, highlightthickness=0, command=lambda: print("LEARN clicked"), relief="flat")
        button_learn.place(x=647.0, y=360.0, width=250.0, height=50.0)
        self.learn_button_image = learn_button_image

# Translate Page Class
class TranslatePage(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="#1F1F1F")

        canvas = Canvas(self, bg="#1F1F1F", height=768, width=1024, bd=0, highlightthickness=0, relief="ridge")
        canvas.pack(fill="both", expand=True)

        text_area_image = PhotoImage(file=relative_to_assets("text_area.png"))
        canvas.create_image(512.0, 242.5, image=text_area_image)
        self.text_area_image = text_area_image  # Keep reference

        text_area = tk.Text(self, bd=0, bg="#191919", fg="#000716", highlightthickness=0)
        text_area.place(x=90.0, y=162.0, width=844.0, height=159.0)

        #output and line
        canvas.create_rectangle(90.0, 354.0, 934.0, 648.0, fill="#191919", outline="")
        canvas.create_rectangle(89.0, 646.9998177080748, 934.0, 648.0, fill="#F58B57", outline="")

        #combobox
        canvas.create_rectangle(684.0, 51.0, 934.0, 101.0, fill="#191919", outline="")

        #home button
        home_button_image = PhotoImage(file=relative_to_assets("home_button.png"))
        button_home = Button(self, image=home_button_image, borderwidth=0, highlightthickness=0, command=lambda: master.show_frame(MainPage), relief="flat")
        button_home.place(x=90.0, y=56.0, width=40.0, height=40.0)
        self.home_button_image = home_button_image

        play_button_image = PhotoImage(file=relative_to_assets("play_button.png"))
        button_play = Button(self, image=play_button_image, borderwidth=0, highlightthickness=0, command=lambda: print("PLAY clicked"), relief="flat")
        button_play.place(x=492.0, y=673.0, width=40.0, height=40.0)
        self.play_button_image = play_button_image

        canvas.create_rectangle( 89.0, 738.9999262151706, 934.0, 740.0, fill="#FFFFFF", outline="")

# Run the application
if __name__ == "__main__":
    app = MainApp()
    app.mainloop()