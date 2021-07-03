from tkinter.constants import X
from typing import Container, Text
import pyttsx3  #pip install pyttsx3
import datetime
import speech_recognition as sr #pip install SpeechRecognition
import wikipedia    #pip install wikipedia
from wikipedia.wikipedia import summary 
import tkinter as tk    #Parte grafica

engine = pyttsx3.init()
voiceRate = 170 #La velocità della voce di Azzurra
engine.setProperty('rate', voiceRate)
wikipedia.set_lang("it")


#-  -   -   -   -   -   -   -   -   PARTE GRAFICA    -   -   -   -   -   -
window = tk.Tk()    #creazione finestra
window.geometry("600x600")  #Dimensioni
window.title("Azzurra") #Titolo
window.configure(background='#252525')
window.resizable(False, False) #non sarà possibile ridimenzionare scheda

#Il titolo che apparirà al centro dello schermo
title = tk.Label(window, text="AZZURRA", background="#252525", foreground="#158BFF", font=("Bold", 50))
title.place(x=20, y=20)

#Il bottone per iniziare a parlare
provaBottone = tk.Button(text="BOTTONE")
provaBottone.place(x=275, y=200)


 


#-  -   -   -   -   -   -   -   -   FUNZIONI AURORA -  -   -   -   -   -   -   -   

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
        query = query.replace("azzurra", "") #Rimuove il suo nome dalla stringa

    except Exception as e:
        print(e)
        speak("Non ho capito. Ripeti, per favore.")
        return "None"
    return query

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

    #Converte numeri in mesi
    if month == 1:
        month = "Gennaio"
    elif month == 2:
        month = "Febbraio"
    elif month == 3:
        month = "Marzo"
    elif month == 4:
        month = "Aprile"
    elif month == 5:
        month = "Maggio"
    elif month == 6:
        month = "Giugno"
    elif month == 7:
        month = "Luglio"
    elif month == 8:
        month = "Agosto"
    elif month == 9:
        month = "Settembre"
    elif month == 10:
        month = "Ottobre"
    elif month == 11:
        month = "Novembre"
    elif month == 12:
        month = "Dicembre"

    speak("Oggi è il " + str(day) + " " + month + " del " + str(year))

#La funzione per cercare qualcosa su wikipedia
def wikiSearch(searchTitle):
    speak("Certamente...")
    print(searchTitle)
    try:
        searchTitle = searchTitle.replace("wikipedia", "") #Rimpiazza la parola "wikipedia" dalla stringa
        wiki = wikipedia.summary(searchTitle, sentences = 2)
        speak(wiki)
    except Exception as e:
        print(e)
        speak("Non ho trovato alcun risultato. Prova a riformulare la richiesta.")

    


#-  -   -   -   -   -   -   -   -   MAIN    -  -   -   -   -   -   -   -  
def main():
    activation()

    while True:
        query = listen().lower() #Associa a query il risultato di ciò che Azzurra sente
        print(query)

        #Verifica il contenuto della query
        if "ora" in query or "ore" in query:
            nowTime()
        elif "giorno" in query or "quanto ne abbiamo" in query:
            nowDay()
        elif "spegniti" in query or "riposa" in query or "dormi" in query or "offline" in query:    
            speak("Buonanotte.")
            quit()
        elif "wikipedia" in query:
            wikiSearch(query)





#Viene richiamato il main
if __name__ == "__main__":
    #main()
    window.mainloop()   #Avvio finestra (dovrò metterla dentro la funzione main )

