from models.main import Model
from views.main import View

from .home import HomeController
from .translate import TranslateController
from .learn.learn import LearnController
from .learn.translate import LearnTranslateController
from .learn.letters import LearnLettersController

class Controller:
    def __init__(self,model: Model,view: View) -> None:
        self.view = view
        self.model = model

        self.controller_classes ={
            "home": HomeController,
            "translate": TranslateController,
            "learn": LearnController,
            "learnTranslate": LearnTranslateController,
            "learnLetters": LearnLettersController
        }
        self.current_controller = None

    def switch(self, name):
        new_controller = self.controller_classes[name](self.model,self.view,self)
        if self.current_controller is not None:
            self.current_controller.destroy()
        self.current_controller = new_controller

    def start(self) -> None:
        self.view.switch("home")
        self.switch("home")
        self.view.start_mainloop()