import pyttsx3
import datetime
import speech_recognition as sr

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('rate', 120)    # Speed percent (can go over 100)
engine.setProperty('voice', voices[0].id)
def speak(audio):
    '''this function gives voice output of the given argument'''
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    '''This function check the time and accordingly greet you with voice output'''
    hour = datetime.datetime.now().hour
    if hour <12:
        speak("Good Morning Sir")
    elif hour==12:
        speak("Good Noon Sir")
    elif hour<15:
        speak("Good Afternoon Sir")
    else:
        speak("Good Evening Sir!")
    speak("I am Anna, How may i help you sir")

def takeCommand():
    '''This function take take the voice command using speech recongnition'''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 0.8
        audio = r.listen(source)
    try:
        print('Recognizing...')
        query = r.recognize_google(audio)
        print(f"You Said:{query}")
    except Exception as e:
        print (e)
        print("say that again please...")
        return 'None'
    return query
if __name__ == "__main__":
    pass
    # takeCommand()
