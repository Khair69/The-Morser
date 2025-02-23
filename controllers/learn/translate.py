from models.main import Model
from views.main import View
from tkinter import CENTER, END

class LearnTranslateController:
    def __init__(self, model:Model, view: View) -> None:
        self.model = model
        self.view = view
        self.frame = self.view.frames["learnTranslate"]
        self._bind()
        

    def _bind(self) -> None:
        self.frame.button_home.config(command=self.home)
        self.frame.button_back.config(command=self.back)
        self.frame.button_start.config(command=self.start_game)
        self.frame.button_enter.config(command=self.check)
        self.frame.button_next.config(command=self.next)

    def home(self) -> None:
        self.view.switch("home") 

    def back(self) -> None:
        self.view.switch("learnLang") 

    def start_game(self) -> None:
        self.frame.button_start.place_forget()
        self.model.learn.start("e2m")
        self.word = self.model.learn.get_word()
        self.frame.word_label.config(text=self.word)
        self.frame.word_label.place(x=512.0, y=177.0,anchor=CENTER)
        self.frame.button_enter.place(x=387.0, y=663.0, width=250.0, height=50.0)

        self.frame.canvas.create_image(512.0, 468.0, image=self.frame.text_area_image)
        self.frame.text_area.place(x=90.0, y=321.0, width=844.0, height=292.0)
        #line
        self.frame.canvas.create_rectangle(89.0, 613.9998177080747, 934.0, 615.0, fill="#F58B57", outline="")

    def check(self) -> None:
        guess = self.frame.text_area.get("1.0", END).strip()  # Get user input
        res = self.model.learn.check(self.word,guess)
        if res == True:
            self.frame.res_label.config(fg="green", text="Correct!")
        else:
            self.frame.res_label.config(fg="red", text=f"Wrong, it's {res}")

        self.frame.res_label.place(x=512.0, y=300.0,anchor=CENTER)
        self.frame.button_enter.place_forget()
        self.frame.button_next.place(x=387.0, y=663.0, width=250.0, height=50.0)
    
    def next(self) -> None:
        self.word = self.model.learn.get_word()
        if self.word == False:
            self.frame.word_label.config(text="THE GAME IS DONE")
            self.frame.button_enter.place(x=387.0, y=663.0, width=250.0, height=50.0)
            return

        self.frame.word_label.config(text=self.word)
        self.frame.res_label.place_forget()
        self.frame.button_next.place_forget()
        self.frame.button_enter.place(x=387.0, y=663.0, width=250.0, height=50.0)
        self.frame.text_area.delete("1.0", END)


