import webbrowser
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listner = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)

    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:

            print('listening...')
            voice = listner.listen(source)
            command = listner.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)



    except:
        pass
    return command


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is' + time)
    elif 'what is' in command:
        person = command.replace('what is', '')
        info = wikipedia.summary(person, 5)
        print(info)
        talk(info)
    elif 'how are you' in command:
        talk('I am fine thank you')
    elif 'joke' in command:
        talk(pyjokes.get_joke())

    elif 'sending message' in command:
        message = command.replace('sending message', '')
        talk('whatsapp' + message)
        pywhatkit.sendwhatmsg('+919226885381', 'How are you', 19, 18)
    elif 'open' in command:
        whatsapp = command.replace('open', '')
        talk('openining' + whatsapp)
        pywhatkit.open_web()
    elif 'website' in command:
        website = command.replace('website', '')
        talk('opening' + website)
        webbrowser.open('https://www.google.com')

    elif 'mmcoe' in command:
        website = command.replace('mmcoe', '')
        talk('opening' + website)
        webbrowser.open('https://www.mmcoe.edu.in')




    else:
        talk('Please say the command again.')


while True:
    run_alexa()
