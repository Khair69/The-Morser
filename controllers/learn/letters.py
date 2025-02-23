from models.main import Model
from views.main import View

class LearnLettersController:
    def __init__(self, model:Model, view: View, obj) -> None:
        self.model = model
        self.view = view
        self.frame = self.view.current_frame
        self.obj = obj
        self._bind()

    def _bind(self) -> None:
        self.frame.button_home.config(command=self.home)
        self.frame.button_back.config(command=self.back)
    
    def home(self) -> None:
        self.view.switch("home")
        self.obj.switch("home")

    def back(self) -> None:
        self.view.switch("learn")
        self.obj.switch("learn")
