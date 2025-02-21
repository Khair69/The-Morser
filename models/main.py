from .translator import Translator
from .audio_gen import MorseAudio
from .learn import Learn

class Model:
    def __init__(self):
        self.translator = Translator()
        self.audio_gen = MorseAudio()
        self.learn = Learn()