from tkinter import END
from models.main import Model
from views.main import View

class TranslateController:
    def __init__(self, model:Model, view:View):
        self.model = model
        self.view = view
        self.frame = self.view.frames["translate"]
        self._bind()

    def _bind(self) -> None:
        self.frame.button_home.config(command=self.home)
        # Bind text input event
        self.frame.text_area.bind("<KeyRelease>", self.translate_text)
        self.frame.button_play.config(command=self.generate_audio)

    def home(self) -> None:
        self.view.switch("home") 

    def translate_text(self, event=None):
        #Translate the text to Morse code in real time.
        text = self.frame.text_area.get("1.0", END).strip()  # Get user input
        mode = self.frame.combo_box.get()
        morse_code = self.model.translator.to_morse(text) if mode == "English to Morse" else self.model.translator.to_english(text) # Translate using your Translator class
        self.frame.output_label.config(text=morse_code)  # Display Morse code

    def generate_audio(self):
        mode = self.frame.combo_box.get()
        message = self.frame.text_area.get("1.0", END).strip() if mode == "Morse to English" else self.frame.output_label.cget("text")
        self.model.audio_gen.play_morse(message)