from models.main import Model
from views.main import View

class LearnController:
    def __init__(self, model:Model, view: View, obj) -> None:
        self.model = model
        self.view = view
        self.frame = self.view.current_frame
        self.obj = obj
        self._bind()

    def _bind(self) -> None:
        self.frame.button_home.config(command=self.home)
        self.frame.button_translate.config(command=self.translate)
        self.frame.button_letters.config(command=self.letters)

    def home(self) -> None:
        self.view.switch("home") 
        self.obj.switch("home")

    def translate(self) -> None:
        self.view.switch("learnTranslate")
        self.obj.switch("learnTranslate")

    def letters(self) -> None:
        self.view.switch("learnLetters")
        self.obj.switch("learnLetters")
