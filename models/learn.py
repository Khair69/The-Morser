import json
import random

class Learn:
    def __init__(self):
        pass

    def start(self, mode, file_name):
        self.mode = mode if mode=="e2m" or "m2e" else None
        with open(f"data/custom_sets/{file_name}.json", "r") as file:
            self.e2m = json.load(file)
        self.m2e = {v: k for k, v in self.e2m.items()}
        self.asked = set()
        self.total = len(self.e2m)
        self.score = 0

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
                return self.e2m[word].strip()
            
        elif self.mode == "m2e":
            if guess.strip().lower() == self.m2e[word].strip().lower():
                return True
            else:
                return self.m2e[word].strip()

