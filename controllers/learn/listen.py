from models.main import Model
from views.main import View
from tkinter import CENTER, messagebox
from customtkinter import CTkLabel, CTkFrame

class LearnListenController:
    def __init__(self, model:Model, view: View, obj) -> None:
        self.model = model
        self.view = view
        self.frame = self.view.current_frame
        self.obj = obj
        self._bind()

    def _bind(self) -> None:
        self.frame.button_back.configure(command=self.back)
        self.frame.button_start.configure(command=self.start_game)
        self.frame.button_enter.configure(command=self.check)
        self.frame.button_next.configure(command=self.next)
        self.frame.button_play.configure(command=self.generate_audio)
        self.frame.button_stop.configure(command=self.stop)
        self.frame.button_settings.configure(command=self.settings)
        self.frame.button_custom.configure(command=self.custom)
        self.load()

    def back(self) -> None:
        e = messagebox.askokcancel(title="Exit?", message="Are you sure you want to exit?\nYou will lose all progress.")
        if e:
            self.view.switch("learn") 
            self.obj.switch("learn")

    def start_game(self) -> None:
        if not self.selected_set:
            messagebox.showwarning(title="No file selected", message="You didn't select a set")  
            return           
        self.frame.button_start.place_forget()
        self.model.learn.start("m2e", self.selected_set.cget("text"))
        self.word = self.model.learn.get_word()
        self.frame.button_enter.place(x=387.0, y=663.0)
        self.frame.text_area.place(x=90.0, y=321.0)
        self.frame.prog_bar.configure(determinate_speed=0.5/(self.model.learn.total/100))
        self.frame.prog_bar.place(x=90, y=20)
        self.frame.button_play.place(x=492.0, y=177.0)
        self.frame.button_custom.place_forget()
        self.frame.choose_frame.place_forget()

    def generate_audio(self):
        self.model.audio_gen.play_morse(self.word)
        self.frame.button_play.place_forget()
        self.frame.button_stop.place(x=492.0, y=177.0)

    def stop(self):
        self.model.audio_gen.stop()
        self.frame.button_stop.place_forget()
        self.frame.button_play.place(x=492.0, y=177.0)

    def check(self) -> None:
        guess = self.frame.text_area.get(0.0, "end").strip()  # Get user input
        res = self.model.learn.check(self.word,guess)
        if res == True:
            self.frame.res_label.configure(text_color="green", text="Correct!")
            self.model.learn.score +=1
        else:
            self.frame.res_label.configure(text_color="red", text=f"Wrong, it's {res}")

        self.frame.res_label.place(x=512.0, y=295.0,anchor=CENTER)
        self.frame.button_enter.place_forget()
        self.frame.button_next.place(x=387.0, y=663.0)
    
    def next(self) -> None:
        self.stop()
        self.word = self.model.learn.get_word()
        self.frame.prog_bar.step()
        if self.word == False:
            self.frame.res_label.configure(text_color="#bb6b44", text=f"THE GAME IS DONE\nYou got {self.model.learn.score} out of {self.model.learn.total}")
            self.frame.button_next.place_forget()
            self.frame.button_play.place_forget()
            self.frame.prog_bar.set(1)
            return

        self.frame.button_play.place(x=492.0, y=177.0)
        self.frame.res_label.place_forget()
        self.frame.button_next.place_forget()
        self.frame.button_enter.place(x=387.0, y=663.0)
        self.frame.text_area.delete(0.0, "end")

    def settings(self) -> None:
        self.view.settings()
        self.obj.settings()

    def custom(self) -> None:
        self.view.switch("custom")
        self.obj.switch("custom")

    def load(self) -> None:
        self.sets = self.model.custom.read()
        self.selected_set = None
        for set in self.sets:
            s = CTkLabel(self.frame.choose_frame, text=set, font=("Segoe UI Variable Display Bold", 29), text_color="#bb6b44", bg_color="#191919", corner_radius=10, cursor="hand2")
            s.pack(pady = 7, anchor="w")
            s.bind("<Button-1>", self.lbl_choose)
            l = CTkFrame(self.frame.choose_frame, height=1, bg_color="#555555")
            l.pack(fill="x", padx=10, pady=5)

    def lbl_choose(self, event):
        if self.selected_set:
            self.selected_set.configure(bg="#191919")
        self.selected_set = event.widget
        self.selected_set.configure(bg="#0b0b0b")