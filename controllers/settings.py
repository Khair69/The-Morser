from models.main import Model
from views.main import View

class SettingsController:
    def __init__(self, model: Model, view: View, obj) -> None:
        self.model = model
        self.view = view
        self.frame = self.view.settings_frame
        self.obj = obj
        self._bind()

    def _bind(self) -> None:
        self.frame.volume_slider.configure(command=self.volume)
        self.frame.button_reset.configure(command=self.reset)

    def volume(self, val) -> None:
        self.model.audio_gen.VOLUME = val

    def reset(self) -> None:
        self.frame.volume_slider.set(0)
        self.volume(0)
