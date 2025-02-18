import tkinter as tk
from logic.translator import Translator

class MorseGUI:
    def __init__(self, root):
        self.translator = Translator()
        self.root = root
        self.root.title("Morse Code Translator")

        self.entry = tk.Entry(root)
        self.entry.pack()

        self.translate_btn = tk.Button(root, text="Translate", command=self.translate)
        self.translate_btn.pack()

        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

    def translate(self):
        text = self.entry.get()
        result = self.translator.to_morse(text)
        self.result_label.config(text=result)

if __name__ == "__main__":
    root = tk.Tk()
    app = MorseGUI(root)
    root.mainloop()