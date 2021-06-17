import pyttsx3
import datetime
import speech_recognition as sr

engine = pyttsx3.init()

voiceRate = 170 #La velocità della voce di Azzurra
engine.setProperty('rate', voiceRate)


#-  -   -   -   -   -   -   -   -   FUNZIONI -  -   -   -   -   -   -   -   

#La funzione per dare comandi ad Azzurra
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Sono in ascolto...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Cerco di capire...")
        query = r.recognize_google(audio, language="it-IT")
        print(query)
    except Exception as e:
        print(e)
        speak("Non ho capito. Ripeti, per favore.")
        return "None"
    return speak ("hai detto: " + query)
    

#La funzione per far parlare Azzurra
def speak(audio): 
    engine.say(audio)
    engine.runAndWait()

def activation():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("Buongiorno")
    elif hour >= 12 and hour < 18:
        speak("Buon pomeriggio")
    else:
        speak("Buona sera")

    speak("Come posso aiutarti?")

#La funzione per verificare che ore sono
def nowTime(): 
    time = datetime.datetime.now().strftime("%H:%M") #Prende l'orario attuale e lo rende una stringa
    time = "Sono le " + time
    speak(time)

#La funzione per verificare che giorno è
def nowDay(): 
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    speak("Oggi è il " + str(day) + " " + str(month) + " del " + str(year))

activation()
listen()
