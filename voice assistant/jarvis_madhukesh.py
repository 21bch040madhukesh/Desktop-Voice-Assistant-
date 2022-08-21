# Welcome to MADHUKESH SINGH'S desktop voice assistant
# It wil be fun meeting Jarvis

import pyttsx3
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishkaro():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am jarvis Sir. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("#Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("#Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print("User said: {query}\n")
        print(query)

    except Exception as e:
        # print(e)    
        print("*Say again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('', '') 
   #server.login('abc@gmail.com', 'P@ssw0rd') like this 
    server.sendmail('', to, content)
   #server.sendemail('abc@gmail.com',to,content) like this
    server.close()

if __name__ == "__main__":
    wishkaro()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing diferent commands given to ai based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   
            
        elif 'open amazon' in query:
            webbrowser.open("amazon.in")
            
        elif 'open flipkart' in query:
            webbrowser.open("flipkart.com")
            
        elif 'open linkedin' in query:
            webbrowser.open("linkedin.com")

        elif 'play music' in query:
            music_dir = 'Music'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak("Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "path"
            #give the path pf file you want to open.
            os.startfile(codePath)

        elif 'email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "21bch040@nith.ac.in"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend Bittu bhai. I am not able to send this email")