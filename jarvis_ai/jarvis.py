import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import pyaudio
import time
# import os

def speech_text():
    recognize = sr.Recognizer()
    while True:
        with sr.Microphone() as source:
            print("Listening...")
            recognize.adjust_for_ambient_noise(source)
            audio = recognize.listen(source)
            try:
                print("Recognizing...")
                data = recognize.recognize_google(audio)
                print(data)
                return data
            except sr.UnknownValueError:
                print("Not able to recognize")
                continue

def txt_speech(x):
    
    engine=pyttsx3.init()
    voices=engine.getProperty("voices")
    engine.setProperty("voice",voices[0].id)
    rate=engine.getProperty("rate")
    engine.setProperty("rate",100)
    engine.say(x)
    engine.runAndWait()
    
    
    

if __name__ == "__main__":

        while True:
            speech_data=speech_text().lower()
            if "your name" in speech_data:
                name="my name is jarvis voice assistant"
                txt_speech(name)
            elif "age" in speech_data:
                age="i am not a human iam ai"
                txt_speech(age)
            elif "open youtube" in speech_data:
                txt_speech("Opening YouTube")
                webbrowser.open("https://www.youtube.com")     
            elif "joke" in speech_data:
                joke=pyjokes.get_joke()
                txt_speech(joke)
            elif "time" in speech_data:
                current_time=datetime.datetime.now().strftime("%I:%M %p")
                txt_speech(f"The Current Time is {current_time}")
            elif "open linkedin" in speech_data:
                txt_speech("opening linkedin")
                webbrowser.open("https://www.linkedin.com/in/abdulrafaykhan-dev/")         
            elif "open whatsapp" in speech_data:
                txt_speech("opening whatsapp")
                webbrowser.open("https://web.whatsapp.com")         
            elif "open instagram" in speech_data:
                txt_speech("opening instagram")
                webbrowser.open("https://www.instagram.com/iam__abdul_rafay/")       
            elif "open google" in speech_data:
                txt_speech("opening google")
                webbrowser.open("https://www.google.com")       
            elif "open github" in speech_data:
                txt_speech("opening github")
                webbrowser.open("https://github.com/iamabdulrafay")       
            elif "open chat gpt" in speech_data:
                txt_speech("opening chat gpt")
                webbrowser.open("https://chatgpt.com/")       
         
            elif "exit" in speech_data:
                txt_speech("thanks for using jarvis ai voice assistant")
                break 
            
            
            else:
             print("thanks for using ai voice assistant ")      
    
            time.sleep(3)    

    
  
