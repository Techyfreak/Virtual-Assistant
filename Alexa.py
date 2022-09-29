import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

bot = pyttsx3.init()
voices = bot.getProperty('voices')
bot.setProperty('voice',voices[1].id)


def talk(words):
    bot.say(words)
    bot.runAndWait()

listener = sr.Recognizer()


def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening..!')
            voice = listener.listen(source)
            text = listener.recognize_google(voice)
            text = text.lower()
            #if 'hello' in text:
            print('User :'+text)
                #talk(text)
    except:
        pass
    return text

def run_alexa():
    text= take_command()

    if 'play' in  text:
        song = text.replace('play','')

        talk('playing' + song)
        print('Alexa : playing' +song)
        pywhatkit.playonyt(song)

    elif 'time' in text:
        time = datetime.datetime.now().strftime('%I :%M %p')
        talk('the time now is' +time)
        print('Alexa :The time now is ' + time)

    elif 'tell me about' in text:
        person = text.replace('tell me about','')
        info = wikipedia.summary(person,1)
        print('Alexa :'+info)
        talk(info)

    else:
        talk('well,requesting to say once again')
        print('Alexa:well,requesting to say once again')



while True:
    run_alexa()
