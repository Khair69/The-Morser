from typing import TypedDict

from .root import Root
from .home import HomeView
from .translate import TranslateView

class Frames(TypedDict):
    home: HomeView
    translate: TranslateView

class View:
    def __init__(self):
        self.root = Root()
        self.frames: Frames = {}

        self._add_frame(HomeView, "home")
        self._add_frame(TranslateView, "translate")

    def _add_frame(self, Frame, name: str) -> None:
        self.frames[name] = Frame(self.root)
        self.frames[name].grid(row=0, column=0, sticky="nsew")

    def switch(self, name: str) -> None:
        frame = self.frames[name]
        frame.tkraise()

    def start_mainloop(self) -> None:
        self.root.mainloop()