import models.pref as pref
import customtkinter as CTk

ASSETS_PATH = pref.get_base_path()

class SettingsView(CTk.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)

        #configs
        self.corner_rad = 15
        self.geometry("400x300")
        self.title("Settings")
        self.resizable(False, False)
        self.after(250, lambda: self.iconbitmap(pref.relative_to_assets(pref.get_base_path(),"icon.ico")))
        self.after(250, lambda: self.focus())

        #canvas or smth idk
        self.canvas = CTk.CTkCanvas(self, bg="#1F1F1F", height=300, width=400, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.pack(fill="both", expand=True)

        #volume slider
        self.vol_label = CTk.CTkLabel(self, text="Volume", text_color="#bb6b44", font=("Segoe UI Variable Display Bold", 16), bg_color="#1f1f1f")
        self.vol_label.place(x=50,y=20)
        self.volume_slider = CTk.CTkSlider(self, from_=-50, to=50, width=300, progress_color="#bb6b44", button_color="#874d31", button_hover_color="#a85f3b", bg_color="#1f1f1f")
        self.volume_slider.set(0)
        self.volume_slider.place(x=50,y=45)

        #reset button
        self.button_reset = CTk.CTkButton(self, width=70, height=40, text="Reset", font=("Segoe UI Variable Display Bold", 16), text_color="#191919", corner_radius=self.corner_rad, bg_color="#1F1F1F", fg_color="#bb6b44", hover_color="#874d31")
        self.button_reset.place(x=315.0, y=245.0)