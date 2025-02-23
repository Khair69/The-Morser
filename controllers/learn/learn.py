from models.main import Model
from views.main import View

class LearnController:
    def __init__(self, model:Model, view: View) -> None:
        self.model = model
        self.view = view
        self.frame = self.view.frames["learn"]
        self._bind()

    def _bind(self) -> None:
        self.frame.button_home.config(command=self.home)
        self.frame.button_translate.config(command=self.translate)
        self.frame.button_letters.config(command=self.letters)

    def home(self) -> None:
        self.view.switch("home") 

    def translate(self) -> None:
        self.view.switch("learnTranslate")

    def letters(self) -> None:
        self.view.switch("learnLetters")