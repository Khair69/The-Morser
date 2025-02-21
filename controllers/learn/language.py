from models.main import Model
from views.main import View

class LearnLangController:
    def __init__(self, model:Model, view: View) -> None:
        self.model = model
        self.view = view
        self.frame = self.view.frames["learnLang"]
        self._bind()

    def _bind(self) -> None:
        self.frame.button_home.config(command=self.home)
        self.frame.button_back.config(command=self.back)
        self.frame.button_e2m.config(command=self.e2m)


    def home(self) -> None:
        self.view.switch("home") 

    def back(self) -> None:
        self.view.switch("learn") 

    def e2m(self) -> None:
        self.view.switch("learnTranslate") 