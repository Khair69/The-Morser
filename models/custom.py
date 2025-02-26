import json
import models.pref as pref
import os

class Custom:
    def __init__(self):
        self.path = pref.get_base_path_json()

    def save(self, words: list, file_name: str) -> None:
        with open(f"{self.path}/{file_name}.json", "w") as file:
            json.dump(words, file, indent=4)    

    def read(self) -> None:
        filenames = [os.path.splitext(file)[0]
                    for file in os.listdir(self.path)
                    if os.path.isfile(os.path.join(self.path, file))
        ]
        return filenames