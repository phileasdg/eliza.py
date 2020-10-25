import gtts
from playsound import playsound
import os

# make request to google to get synthesis
tts = gtts.gTTS("Hello world", lang="en-au")

# save the audio file
tts.save(os.path.join("C:/Users/phile/PycharmProjects/eliza.py/text_to_speech/", "hello.mp3"))

# play the audio file
playsound("hello.mp3")


