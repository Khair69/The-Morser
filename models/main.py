from .translator import Translator
from .audio_gen import MorseAudio
from .learn import Learn
from .custom import Custom

class Model:
    def __init__(self):
        self.translator = Translator()
        self.audio_gen = MorseAudio()
        self.learn = Learn()
        self.custom = Custom()