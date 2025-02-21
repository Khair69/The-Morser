import os
from pydub import AudioSegment
from pydub.generators import Sine
from pydub.playback import play
from multiprocessing import Process

# Define a temp folder inside the project directory
TEMP_DIR = os.path.join(os.path.dirname(__file__), "temp_audio")
os.makedirs(TEMP_DIR, exist_ok=True)  # Ensure the folder exists

class MorseAudio:
    DOT_DURATION = 200  # milliseconds
    DASH_DURATION = DOT_DURATION * 3
    FREQUENCY = 800  # Hz

    def generate_tone(self, duration):
        return Sine(self.FREQUENCY).to_audio_segment(duration=duration)

    def play_morse(self, morse_code):
        """Generates and plays Morse code audio from the project directory."""
        silence = AudioSegment.silent(duration=self.DOT_DURATION)
        word_gap = AudioSegment.silent(duration=self.DASH_DURATION * 2)
        audio = AudioSegment.silent(duration=0)

        for symbol in morse_code:
            if symbol == ".":
                audio += self.generate_tone(self.DOT_DURATION) + silence
            elif symbol == "-":
                audio += self.generate_tone(self.DASH_DURATION) + silence
            elif symbol == " ":
                audio += silence  # Letter separation
            elif symbol == "/":
                audio += word_gap  # Word separation

        # Save the audio file inside the project folder
        audio_file_path = os.path.join(TEMP_DIR, "morse_output.wav")
        audio.export(audio_file_path, format="wav")

        self.proc = Process(target=play, args=(audio,))

        # Try playing the file, but ignore errors
        try:
            self.proc.start()
        except Exception as e:
            print(f"Warning: Could not play audio. Error: {e}")

    def stop(self):
        self.proc.terminate()
