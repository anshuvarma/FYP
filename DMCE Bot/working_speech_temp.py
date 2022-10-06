from datetime import datetime
from email.mime import audio
import pyttsx3
from sacrebleu import sentence_bleu 
import speech_recognition as sr
import wikipedia


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1])
engine.setProperty('voice', voices[1].id)


# Does the job of speaking functionality
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Wishes the person
def wishMe():
    hour = int(datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!!!")
    elif hour >=12 and hour < 18:
        speak("Good Afternoon!!!")
    else:
        speak("Good Evening!!!")
    
    speak("This is bot. How may I help you ??")

# It takes the microhphone input from user and returns text output basically it converts speech to text
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout = 5, phrase_time_limit = 5)

    try:
        print("Recognizing")
        query = r.recognize_google(audio, language='eng-in')
        print("User Said", query)
    
    except Exception as e:
        # print(e)

        print("Say that again")
        return "None"

    return query

if __name__ == "__main__":
    # speak("Hello!!! How are you")
    wishMe()
    while True:
        query = takeCommand().lower()
    
        # Logic to implement some commads
        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace('wikipedia', "")
            results = wikipedia.summary(query, sentences = 3)
            speak("According to wikipedia")
            print(results)
            speak(results)