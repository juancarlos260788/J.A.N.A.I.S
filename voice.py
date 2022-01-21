
#YOU NEED TO INSTALL AND IMPORT THE LIST FROM LINE 4 TILL LINE 17

import pyttsx3
import speech_recognition as sr
import smtplib
import datetime
import secrets
from email.message import EmailMessage
import webbrowser as wb
import wikipedia
import requests
import pyautogui
import pywhatkit
from time import sleep
import clipboard
import os
import pyjokes


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def c19():
    r = requests.get('https://ourworldindata.org/explorers/coronavirus-data-explorer')

    covid_data = f'Confirmed cases : {data["cases"]}'
    print(covid_data)
    speaj(covid_data)


def getvoices(voice):
    voices = engine.getProperty('voices')
    print(voices[1].id)
    if voice == 1:
        engine.setProperty('voice', voices[1].id)
    if voice == 2:
        engine.setProperty('voice', voices[1].id)
    speak("Hello")

def time():
    Time = datetime.dateti
    me.now().strftime("%I:%M:%S")
    #Hours = I, minutes= M and seconds =S
    speak("The current time is:")
    speak(Time)

def date():
    day = int(datetime.datetime.now().day)
    month = int(datetime.datetime.now().month)
    year = int(datetime.datetime.now().year)
    speak("Today is: ")
    speak(day)
    speak(month)
    speak(year)

#Now this part is for your greetings...well, not your greeting but the greetings Janais will say to you, make sense?
def greeting():
    hour =datetime.datetime.now().hour
    if hour >=6 and hour <12:
        speak("Good Morning Sir! Welcome back")
    elif hour >=12 and hour <18:
        speak("Good afternoon sir! Welcome back")
    elif hour >=18 and hour <24:
        speak("Good evening sir! Welcome back")
    else:
        speak("Good Night sir!")
def whishme():
    greeting()
    speak("I've been waiting for you")
    speak("Yanais at your service, please tell me how can I assist you?")


#while True:
#    voice = int(input("Press 1 for male voice\nPress 2 for female voice\n"))
#    speak(audio)

#    getvoices(voice)

#whishme()

def takeCommandCMD():
    query = input("Please tell me how can I assist you?\n")
    return query

def sendwhatsmsg(phone_no, message):
    Message =message
    wb.open('https://web.whatsapp.com/send?phone='+phone_no+'&text='+Message)
    sleep(10)
    pyautogui.press("Enter")

def searchgoogle():
    speak('what should I search for you?')
    search =takeCommandMic()
    wb.open('https://www.google.com/search?='+search)

def takeCommandMic():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Waiting your commands...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Working on it...")
        query = r.recognize_google(audio , language="en-GB")
        print(query)
    except Exception as e:
        print(e)
        speak("Would you repeat that again, please?")
        return "None"
    return query


if __name__ == "__main__":
    getvoices(2)
    whishme()
    while True:
        query = takeCommandMic().lower()

        if 'time' in query:
            time()

        elif 'date' in query:
            date()

        elif 'message' in query:
            user_name = {

                'A'  : '+xxxx ',
                'B' : '+xxxx',
                'C' : '+xxxx'

            }

            try:
                speak("To whom you want to send the message?")
                name = takeCommandMic()
                phone_no = user_name[name]
                speak("What's the message, sir?")
                message = takeCommandMic()
                sendwhatsmsg(phone_no, message)
                speak('message has been send')
            except Exception as e:
                print(e)
                speak("Unable to send the message")

        elif 'c19' in query:
            c19()


        elif 'wikipedia' in query:
            speak('searching on wiki...')
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences = 3)
            print(result)
            speak(result)

        elif 'search' in query:
            searchgoogle()



        elif 'offline' in query:
            quit()

