import pyttsx3

engine = pyttsx3.init()


def speak(audio): #La funzione per far parlare Azzurra
    engine.say(audio)
    engine.runAndWait()

speak("Ciao, io sono Azzurra. Sarò la tua assistente personale.")