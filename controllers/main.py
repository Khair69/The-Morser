from models.main import Model
from views.main import View

from .home import HomeController
from .translate import TranslateController
from .learn.learn import LearnController
from .learn.translate import LearnTranslateController
from .learn.letters import LearnLettersController
from .learn.listen import LearnListenController
from .settings import SettingsController

class Controller:
    def __init__(self,model: Model,view: View) -> None:
        self.view = view
        self.model = model

        self.controller_classes ={
            "home": HomeController,
            "translate": TranslateController,
            "learn": LearnController,
            "learnTranslate": LearnTranslateController,
            "learnLetters": LearnLettersController,
            "learnListen": LearnListenController,
            "settings": SettingsController
        }
        self.current_controller = None
        self.settings_controller = None

    def switch(self, name):
        new_controller = self.controller_classes[name](self.model,self.view,self)
        if self.current_controller is not None:
            del self.current_controller
        self.current_controller = new_controller

    def start(self) -> None:
        self.view.switch("home")
        self.switch("home")
        self.view.start_mainloop()

    def settings(self) -> None:
        if self.settings_controller is None:
            self.settings_controller = self.controller_classes["settings"](self.model,self.view, self)