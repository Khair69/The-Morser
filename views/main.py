from typing import TypedDict

from .root import Root
from .home import HomeView
from .translate import TranslateView
from .learn.learn import LearnMenuView
from .learn.translate import LearnTranslateView
from .learn.letters import LearnLettersView

class Frames(TypedDict):
    home: HomeView
    translate: TranslateView
    learn: LearnMenuView
    learnTranslate : LearnTranslateView
    learnLetters : LearnLettersView

class View:
    def __init__(self):
        self.root = Root()
        self.frames: Frames = {}

        self._add_frame(HomeView, "home")
        self._add_frame(TranslateView, "translate")
        self._add_frame(LearnMenuView, "learn")
        self._add_frame(LearnTranslateView, "learnTranslate")
        self._add_frame(LearnLettersView, "learnLetters")

    def _add_frame(self, Frame, name: str) -> None:
        self.frames[name] = Frame(self.root)
        self.frames[name].grid(row=0, column=0, sticky="nsew")

    def switch(self, name: str) -> None:
        frame = self.frames[name]
        frame.tkraise()

    def start_mainloop(self) -> None:
        self.root.mainloop()