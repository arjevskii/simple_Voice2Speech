#pip install SpeechRecognition wolframalpha

import wolframalpha
import os
import speech_recognition as sr

# clear the current window/terminal output
os.system('clear')

# obtain audio from the microphone
r = sr.Recognizer()

# audio recorded
with sr.Microphone() as source:
    print("Please speak into Microphone...")
    audio = r.listen(source)

#output audio into text
try:
    print(r.recognize_google(audio))

except sr.UnknownValueError:
    print("Could not understand the audio input")

except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
