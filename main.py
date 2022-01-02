#J.A.N.A.I.S (Just Another Normal Artificial Intelligence System)
#Created by Juan Carlos P. Melgar

#Reason: If Iron Man had JARVIS and FRIDAY, then why can't I have my own assistant?)


#THE FOLLOWING REQUIREMENTS NEED TO BE INSTALLED IN THE CONSOLE#

#Install pyttsx3: pip install pyttsx3
#Install PYAUDIO: pip install pipwin, then  pipwin install pyaudio (yeah, this one is quite annoying)
#Install voice recog: pip install SpeechRecognition
#Advance control on browser: pip install pywhatkit
#If you need wiki (coz why not?): pip install wikipedia
#And for jokes (coz every single AI need a funny side): pip install pyjokes


#Ok now the script ^ ^

#FIRST STEP: Voice recognition and transcription into the console.
#Unfortunately, JANAIS only recognize English :-(

import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
from gtts import gTTS
import os

voice = ""
while True:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            audio = r.listen(source)
            text = r.recognize_google(audio)
            print(text)
            if text == "stop":
                break
            text = r.recognize_google(audio)
            voice =voice +str(text)
        except:
            print("say something...")
hr =gTTS(text=voice, Lang='en', slow=False)
hr.save("1.wav")





