from .root import Root
from .home import HomeView
from .translate import TranslateView
from .learn.learn import LearnMenuView
from .learn.translate import LearnTranslateView
from .learn.letters import LearnLettersView
from .learn.listen import LearnListenView
class View:
    def __init__(self):
        self.root = Root()

        self.frame_classes ={
            "home": HomeView,
            "translate": TranslateView,
            "learn": LearnMenuView,
            "learnTranslate": LearnTranslateView,
            "learnLetters": LearnLettersView,
            "learnListen": LearnListenView
        }
        self.current_frame = None

    def switch(self, name):
        new_frame = self.frame_classes[name](self.root)
        if self.current_frame is not None:
            self.current_frame.destroy()
        self.current_frame = new_frame
        self.current_frame.grid(row=0, column=0, sticky="nsew")

    def start_mainloop(self) -> None:
        self.root.mainloop()