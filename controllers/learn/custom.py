from models.main import Model
from views.main import View
from tkinter import messagebox
from customtkinter import CTkInputDialog

class LearnCustomController:
    def __init__(self, model:Model, view: View, obj) -> None:
        self.model = model
        self.view = view
        self.frame = self.view.current_frame
        self.obj = obj
        self.mode = ""
        self._bind()
        self.words = {}

    def _bind(self) -> None:
        self.frame.button_back.configure(command=self.back)
        self.frame.button_add.configure(command=self.add)
        self.frame.button_save.configure(command=self.save)
        self.frame.inp_word.bind("<Return>",self.add)


    def back(self) -> None:
        e = messagebox.askokcancel(title="Exit?", message="Are you sure you want to exit?\nYou have unsaved changes.")
        if e:
            self.view.switch("learnTranslate") 
            self.obj.switch("learnTranslate")
    
    def add(self, *args) -> None:
        eng_w = self.frame.inp_word.get().strip().upper()
        morse_w = self.model.translator.to_morse(eng_w)
        self.words.update({eng_w:morse_w})
        self.frame.inp_word.delete(0,"end")
    
    def save(self) -> None:
        if self.words:
            self.dialog = CTkInputDialog(text="What do you want to name the file?", title="Name", fg_color="#1f1f1f", button_fg_color="#bb6b44", button_hover_color="#874d31", button_text_color="#191919", entry_fg_color="#191919", entry_text_color="#bb6b44")
            file_name = self.dialog.get_input()
            if file_name:
                self.model.custom.save(self.words, file_name)
                self.view.switch("learnTranslate") 
                self.obj.switch("learnTranslate")
            else:
                messagebox.showwarning(title="No file name", message="Please provide a file name")        
        else:
            messagebox.showwarning(title="Empty List", message="The words list can't be empty!")