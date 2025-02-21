from models.main import Model
from views.main import View

from .home import HomeController
from .translate import TranslateController
from .learn.learn import LearnController
from .learn.language import LearnLangController
from .learn.translate import LearnTranslateController

class Controller:
    def __init__(self,model: Model,view: View) -> None:
        self.view = view
        self.model = model
        self.home_controller = HomeController(model,view)
        self.translate_controller = TranslateController(model,view)
        self.learn_controller = LearnController(model,view)
        self.learnLang_controller = LearnLangController(model,view)
        self.learnTranslate_controller = LearnTranslateController(model,view)

    def start(self) -> None:
        self.view.switch("home")
        self.view.start_mainloop()