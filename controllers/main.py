from models.main import Model
from models.translator import Translator
from views.main import View

from .home import HomeController
from .translate import TranslateController

class Controller:
    def __init__(self,model: Model,view: View) -> None:
        self.view = view
        self.model = model
        self.home_controller = HomeController(model,view)
        self.translate_controller = TranslateController(model,view)

    def start(self) -> None:
        self.view.switch("home")
        self.view.start_mainloop()