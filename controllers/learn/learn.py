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
        self.frame.button_home.configure(command=self.home)
        self.frame.button_translate.configure(command=self.translate)
        self.frame.button_letters.configure(command=self.letters)
        self.frame.button_listen.configure(command=self.listen)

    def home(self) -> None:
        self.view.switch("home") 
        self.obj.switch("home")

    def translate(self) -> None:
        self.view.switch("learnTranslate")
        self.obj.switch("learnTranslate")

    def letters(self) -> None:
        self.view.switch("learnLetters")
        self.obj.switch("learnLetters")

    def listen(self) -> None:
        self.view.switch("learnListen")
        self.obj.switch("learnListen")