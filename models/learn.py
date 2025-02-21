import json
import random

class Learn:
    def __init__(self, mode =None, data_file="data/set_words.json"):
        with open(data_file, "r") as file:
            self.e2m = json.load(file)
        #self.m2e = {v: k for k, v in self.e2m.items()}
        self.english_word, self.morse_word = "",""
        self.asked = set()
        self.mode = mode

    def get_word(self):
        remaining = list(set(self.e2m.items()) - self.asked)

        if not remaining:
            return False
        
        self.english_word, self.morse_word = random.choice(remaining)

        self.asked.add((self.english_word, self.morse_word))
        return True

    def check(self, guess):
        if self.mode == "e2m":
            if guess.strip() == self.morse_word:
                return True
            else:
                return self.morse_word
        elif self.mode == "m2e":
            if guess.strip().lower() == self.english_word.lower():
                return True
            else:
                return self.english_word


