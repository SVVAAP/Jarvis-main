from __future__ import with_statement
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
import cv2
import pywhatkit as kit
import sys
import pyautogui
import time
import operator
import requests

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 150)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("Ready To Comply. What can I do for you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        elif "channel analytics" in query:
            webbrowser.open("https://studio.youtube.com/channel/UCxeYbp9rU_HuIwVcuHvK0pw/analytics/tab-overview/period-default")
        
        elif 'search on youtube' in query:
            query = query.replace("search on youtube", "")
            webbrowser.open(f"www.youtube.com/results?search_query={query}")
        
        elif 'open youtube' in query:
            speak("What would you like to watch?")
            qrry = takeCommand().lower()
            kit.playonyt(f"{qrry}")
        
        elif 'close chrome' in query:
            os.system("taskkill /f /im chrome.exe")
        
        elif 'close youtube' in query:
            os.system("taskkill /f /im msedge.exe")
        
        elif 'open google' in query:
            speak("What should I search?")
            qry = takeCommand().lower()
            webbrowser.open(f"{qry}")
            results = wikipedia.summary(qry, sentences=2)
            speak(results)
        
        elif 'close google' in query:
            os.system("taskkill /f /im msedge.exe")
        
        elif 'play music' in query:
            music_dir = 'E:\Musics'
            songs = os.listdir(music_dir) 
            os.startfile(os.path.join(music_dir, random.choice(songs)))
        
        elif 'play iron man movie' in query:
            npath = "E:\ironman.mkv" 
            os.startfile(npath)
        
        elif 'close movie' in query:
            os.system("taskkill /f /im vlc.exe")
        
        elif 'close music' in query:
            os.system("taskkill /f /im vlc.exe")
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S") 
            speak(f"Sir, the time is {strTime}")
        
        elif "shut down the system" in query:
            os.system("shutdown /s /t 5")
        
        elif "restart the system" in query:
            os.system("shutdown /r /t 5")
        
        elif "Lock the system" in query:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
        
        # Add more commands here...

        elif "go to sleep" in query:
            speak('Alright then, I am switching off')
            sys.exit()
