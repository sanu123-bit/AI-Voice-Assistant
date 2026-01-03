import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pyjokes
import random
import pyautogui
from plyer import notification



engine = pyttsx3.init('sapi5')
engine.setProperty('volume', 1.0)
engine.setProperty('rate', 180)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greet_me():
    hour = int(datetime.datetime.now().hour)
    if 6 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour <= 16:
        speak("Good afternoon!")
    elif 16 < hour < 19:
        speak("Good evening!")
    speak("I am your virtual assistant. How may I assist you?")

def takeCommand():  
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 100
        r.adjust_for_ambient_noise(source, 1.2)
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
    except Exception as e:
        # print("Say that again please...")
        return "None"
    return query.lower()

if __name__ == '__main__':
    greet_me()
    while True:
        query = takeCommand()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        # elif 'hello' or 'hii' in query:
        #     speak("Welcome, How can I help you.")

        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com")

        elif 'open google' in query:
            webbrowser.open("https://www.google.com")

        elif 'search on google' in query:
            speak("What should I search for?")
            search_query = takeCommand()
            webbrowser.open(f"https://www.google.com/search?q={search_query}")

        elif 'open stackoverflow' in query:
            webbrowser.open("https://stackoverflow.com")

        elif 'play music' in query:
            
            speak("Playing music")
            song = random.randint(1, 3) 
            if song == 1:
                webbrowser.open("https://youtu.be/TIiTI5fR2rQ")
            elif song == 2:
                webbrowser.open("https://youtu.be/TIiTI5fR2rQ")
            elif song == 3:
               webbrowser.open("https://youtu.be/TIiTI5fR2rQ")


           
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif 'open vs code' in query:
            codePath = "C:\\Users\\<YourUsername>\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open chrome' in query:
            chromePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(chromePath)

        elif 'write note' in query:
            speak("What should I write ?")
            # note = takecommand()
            note = query.replace("write note", "")
            note = note.strip()
            if note != "":
                speak("Adding note : "+ note)
                with open ('note.txt', 'a') as f:
                    f.write(note + "/n")
            # with open('note.txt', 'w') as f:
            #     f.write(note)
            # speak("Note written successfully.")

        elif 'read note' in query:
            try:
                with open('note.txt', 'r') as f:
                    speak("Here is your note:")
                    speak(f.read())
            except FileNotFoundError:
                speak("No notes found.")

        elif 'display note' in query:
            with open('note.txt', "r") as f:
                notes = f.read()
            notification.notify(
                title = "NOTE",
                message = notes
            )



        elif 'open' in query:
            request = query.replace("open", "")
            pyautogui.press("super")
            pyautogui.typewrite(request)
            pyautogui.sleep(2)
            pyautogui.press("enter")

        
        elif 'tell me a joke' in query:
            joke = pyjokes.get_joke()
            print(joke)
            speak(joke)

        elif 'exit' in query or 'quit' in query:
            speak("Goodbye! Have a nice day.")
            break

        else:
            speak("I'm sorry, I didn't understand. Can you please repeat?")
