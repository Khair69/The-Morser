import json
import random

class Learn:
    def __init__(self, data_file="data/set_words.json"):
        with open(data_file, "r") as file:
            self.e2m = json.load(file)
        self.m2e = {v: k for k, v in self.e2m.items()}

    def start(self, mode):
        self.mode = mode if mode=="e2m" or "m2e" else None
        self.asked = set()

    def get_word(self):
        remaining = list(set(self.e2m.items()) - self.asked)

        if not remaining:
            return False
        
        english_word, morse_word = random.choice(remaining)

        self.asked.add((english_word, morse_word))

        return english_word if self.mode == "e2m" else morse_word
        
    def check(self, word, guess):
        if self.mode == "e2m":
            if guess.strip().lower() == self.e2m[word].strip().lower():
                return True
            else:
                return self.e2m[word].strip().lower()
            
        elif self.mode == "m2e":
            if guess.strip().lower() == self.m2e[word].strip().lower():
                return True
            else:
                return self.m2e[word].strip().lower()

