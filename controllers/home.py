from models.main import Model
from views.main import View

class HomeController:
    def __init__(self, model: Model, view: View, obj) -> None:
        self.model = model
        self.view = view
        self.frame = self.view.current_frame
        self.obj = obj
        self._bind()

    def _bind(self) -> None:
        self.frame.button_translate.config(command=self.translate)
        self.frame.button_learn.config(command=self.learn)

    def translate(self) -> None:
        self.view.switch("translate")
        self.obj.switch("translate")

    def learn(self) -> None:
        self.view.switch("learn")
        self.obj.switch("learn")
