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
        self.frame.button_translate.configure(command=self.translate)
        self.frame.button_learn.configure(command=self.learn)
        self.frame.button_settings.configure(command=self.settings)

    def translate(self) -> None:
        self.view.switch("translate")
        self.obj.switch("translate")

    def learn(self) -> None:
        self.view.switch("learn")
        self.obj.switch("learn")

    def settings(self) -> None:
        self.view.settings()
        self.obj.settings()