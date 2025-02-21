from models.main import Model
from views.main import View

class HomeController:
    def __init__(self, model: Model, view: View) -> None:
        self.model = model
        self.view = view
        self.frame = self.view.frames["home"]
        self._bind()

    def _bind(self) -> None:
        self.frame.button_translate.config(command=self.translate)
        self.frame.button_learn.config(command=self.learn)

    def translate(self) -> None:
        self.view.switch("translate")

    def learn(self) -> None:
        self.view.switch("learn")