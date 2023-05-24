#By "Stay toxic" team 
#Team Head "Devesh Mishra"

import pyttsx3
import openai
import os
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import pywhatkit
import psutil
import pyjokes

from myapi import apikey

openai.api_key = apikey
def dc():
    a= listen()

    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": a}])
    print(completion.choices[0].message.content)
    exit()

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Function to speak out the given text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to greet the user
def greet():
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("How can I assist you today?")

# Function to listen to user's command
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en')
        print(f"User: {query}\n")
    except Exception as e:
        print("Sorry, I didn't catch that. Can you please repeat?")
        return "None"
    return query.lower()

# Function to perform actions based on user's command
def process_command(command):
    if 'wikipedia' in command:
        speak("Searching Wikipedia...")
        command = command.replace("wikipedia", "")
        results = wikipedia.summary(command, sentences=2)
        speak("According to Wikipedia")
        print(results)
        speak(results)
    elif 'open youtube' in command:
        webbrowser.open("https://www.youtube.com/")
    elif 'jarvis' in command:
        speak("Hi, I am jarvis")
    
    elif 'open google' in command:
        webbrowser.open("https://www.google.com/")
    elif 'play' in command:
        song = command.replace("play", "")
        speak(f"Playing {song}")
        pywhatkit.playonyt(song)
    elif 'time' in command:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The current time is {current_time}")
    elif 'cpu usage' in command:
        cpu_usage = str(psutil.cpu_percent())
        speak(f"The CPU usage is {cpu_usage} percent")
    elif 'joke' in command:
        joke = pyjokes.get_joke()
        speak(joke)
    elif 'exit' in command:
        speak("Goodbye!, this ai is developed by stay toxic team")
        exit()
    elif 'toxic youtube' in command:
        webbrowser.open("https://www.youtube.com/@toxicsecurity")
    elif 'open intelligence' in command:
        dc()
    elif 'make request' in command:
        
        speak("Here's the telegram channel")
        webbrowser.open("https://t.me/+FkjsTYJP6D1mYzRl")
        speak("Would you like to Email the developer?")
        xv= listen()
        if 'yes' in xv:
            email_address = "deveshmishra975@gmail.com"

            def open_compose_email():
                mailto_link = f"mailto:{email_address}"
                webbrowser.open(mailto_link)

            print("This function is not avilable this time, you can email the team on 'staytoxicsec@gmail.com' ")
            #open_compose_email()
            speak("Thank you!, any other task?")
        else:
            speak("Thank you!, any other task?")
        
         
    else:
        speak("Sorry, I couldn't understand your command.")

# Main function to run the virtual assistant
def run_jarvis():
    greet()
    while True:
        command = listen()
        if command != 'None':
            process_command(command)

# Run the virtual assistant
if __name__ == "__main__":
    run_jarvis()
