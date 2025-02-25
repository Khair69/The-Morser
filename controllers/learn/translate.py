from models.main import Model
from views.main import View
from tkinter import CENTER, messagebox

class LearnTranslateController:
    def __init__(self, model:Model, view: View, obj) -> None:
        self.model = model
        self.view = view
        self.frame = self.view.current_frame
        self.obj = obj
        self.mode = ""
        self._bind()

    def _bind(self) -> None:
        self.frame.button_home.configure(command=self.home)
        self.frame.button_back.configure(command=self.back)
        self.frame.button_start.configure(command=self.start_game)
        self.frame.button_enter.configure(command=self.check)
        self.frame.button_next.configure(command=self.next)
        self.frame.button_e2m.configure(command=self.e2m)
        self.frame.button_m2e.configure(command=self.m2e)
        self.frame.button_settings.configure(command=self.settings)

    def home(self) -> None:
        e = messagebox.askokcancel(title="Exit?", message="Are you sure you want to exit?\nYou will lose all progress.")
        if e:
            self.view.switch("home") 
            self.obj.switch("home")

    def back(self) -> None:
        e = messagebox.askokcancel(title="Exit?", message="Are you sure you want to exit?\nYou will lose all progress.")
        if e:
            self.view.switch("learn") 
            self.obj.switch("learn")

    def choose(self) -> None:
        self.frame.button_e2m.place_forget()
        self.frame.button_m2e.place_forget()
        self.frame.button_start.place(x=387.0, y=300.0)

    def e2m(self) -> None:
        self.mode = "e2m"
        self.choose()

    def m2e(self) -> None:
        self.mode = "m2e"
        self.choose()

    def start_game(self) -> None:
        self.frame.button_start.place_forget()
        self.model.learn.start(self.mode)
        self.word = self.model.learn.get_word()
        self.frame.word_label.configure(text=self.word)
        self.frame.word_label.place(x=512.0, y=177.0,anchor=CENTER)
        self.frame.button_enter.place(x=387.0, y=663.0)
        self.frame.text_area.place(x=90.0, y=321.0)
        self.frame.prog_bar.configure(determinate_speed=0.5/(self.model.learn.total/100))
        self.frame.prog_bar.place(x=90, y=20)

    def check(self) -> None:
        guess = self.frame.text_area.get(0.0, "end").strip()  # Get user input
        res = self.model.learn.check(self.word,guess)
        if res == True:
            self.frame.res_label.configure(text_color="green", text="Correct!")
            self.model.learn.score +=1
        else:
            self.frame.res_label.configure(text_color="red", text=f"Wrong, it's {res}")

        self.frame.res_label.place(x=512.0, y=300.0,anchor=CENTER)
        self.frame.button_enter.place_forget()
        self.frame.button_next.place(x=387.0, y=663.0)
    
    def next(self) -> None:
        self.word = self.model.learn.get_word()
        self.frame.prog_bar.step()
        if self.word == False:
            self.frame.word_label.configure(text=f"THE GAME IS DONE\nYou got {self.model.learn.score} out of {self.model.learn.total}")
            self.frame.button_next.place_forget()
            self.frame.prog_bar.set(1)
            return

        self.frame.word_label.configure(text=self.word)
        self.frame.res_label.place_forget()
        self.frame.button_next.place_forget()
        self.frame.button_enter.place(x=387.0, y=663.0)
        self.frame.text_area.delete(0.0, "end")

    def settings(self) -> None:
        self.view.settings()
        self.obj.settings()