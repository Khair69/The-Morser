import json

class Translator:
    def __init__(self, data_file="data/morse_code.json"):
        with open(data_file, "r") as file:
            self.morse_dict = json.load(file)
        self.reverse_dict = {v: k for k, v in self.morse_dict.items()}

    def to_morse(self, message: str) -> str:
        return " / ".join(
            " ".join(self.morse_dict.get(char.upper(), "?") for char in word) for word in message.split())
    
    def to_english(self, message: str) -> str:
        return " ".join("".join(self.reverse_dict.get(code, "?") for code in word.split()) for word in message.split(" / "))