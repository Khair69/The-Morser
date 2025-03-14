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
        self.frame.button_home.configure(command=self.home)
        self.frame.button_back.configure(command=self.back)
        self.frame.button_settings.configure(command=self.settings)

    def home(self) -> None:
        self.view.switch("home")
        self.obj.switch("home")

    def back(self) -> None:
        self.view.switch("learn")
        self.obj.switch("learn")

    def settings(self) -> None:
        self.view.settings()
        self.obj.settings()