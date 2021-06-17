import pyttsx3
import datetime

engine = pyttsx3.init()

voiceRate = 170 #La velocità della voce di Azzurra
engine.setProperty('rate', voiceRate)


#-  -   -   -   -   -   -   -   -   FUNZIONI -  -   -   -   -   -   -   -   

def speak(audio): #La funzione per far parlare Azzurra
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




def nowTime(): #La funzione per verificare che ore sono
    time = datetime.datetime.now().strftime("%H:%M") #Prende l'orario attuale e lo rende una stringa
    time = "Sono le " + time
    speak(time)

def nowDay(): #La funzione per verificare che giorno è
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    speak("Oggi è il " + str(day) + " " + str(month) + " del " + str(year))

activation()