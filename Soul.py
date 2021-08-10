import pyttsx3  #pip install pyttsx3
import datetime
import speech_recognition as sr #pip install SpeechRecognition
import wikipedia    #pip install wikipedia
import smtplib
import getpass
from wikipedia.wikipedia import summary
from typing import Container, ContextManager, Text
from urllib.parse import quote_from_bytes
from pyttsx3 import engine, speak



class Soul:

    wikipedia.set_lang("it")

    #-  -   -   -   -   -   -   -   -   FUNZIONI AURORA -  -   -   -   -   -   -   -   
        
    #La funzione per far parlare Azzurra
    def speak(self, audio):
        engine = pyttsx3.init()
        voiceRate = 170 #La velocità della voce di Azzurra
        engine.setProperty('rate', voiceRate)
        engine.say(audio)
        print(audio)
        engine.runAndWait()

    def activation(self):
        hour = datetime.datetime.now().hour
        if hour >= 6 and hour < 12:
            self.speak("Buongiorno")
        elif hour >= 12 and hour < 18:
            self.speak("Buon pomeriggio")
        else:
            self.speak("Buona sera")
            self.speak("Come posso aiutarti?")

    #La funzione per dare comandi ad Azzurra
    def listen(self):
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
            self.speak("Non ho capito. Ripeti, per favore.")
            return "None"
        return query


    #La funzione per verificare che ore sono
    def nowTime(self): 
        time = datetime.datetime.now().strftime("%H:%M") #Prende l'orario attuale e lo rende una stringa
        time = "Sono le " + time
        self.speak(time)


    #La funzione per verificare che giorno è
    def nowDay(self): 
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

        self.speak("Oggi è il " + str(day) + " " + month + " del " + str(year))

    #La funzione per cercare qualcosa su wikipedia
    def wikiSearch(self, searchTitle):
        self.speak("Certamente...")
        print(searchTitle)
        try:
            searchTitle = searchTitle.replace("wikipedia", "") #Rimpiazza la parola "wikipedia" dalla stringa
            wiki = wikipedia.summary(searchTitle, sentences = 2)
            self.speak(wiki)
        except Exception as e:
            print(e)
            self.speak("Non ho trovato alcun risultato. Prova a riformulare la richiesta.")

    #La funzione per inviare mail
    def sendMail(self, to, content):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        speak("Inserire la password del tuo account email") #Per un fattore di sicurezza. È possibile anche rimuoverlo
        pswd = getpass.getpass()
        server.login('2.carem03@gmail.com', pswd)
        server.sendmail('2.carem03@gmail.com', to, content)
        server.close




    #-  -   -   -   -   -   -   -   -   MAIN    -  -   -   -   -   -   -   -  
    def main(self): 
        self.activation()

        while True:
            query = self.listen().lower() #Associa a query il risultato di ciò che Azzurra sente
            print(query)

            #Verifica il contenuto della query
            if "ora" in query or "ore" in query:
                self.nowTime()
            elif "giorno" in query or "quanto ne abbiamo" in query:
                self.nowDay()
            elif "spegniti" in query or "riposa" in query or "dormi" in query or "offline" in query:    
                self.speak("Buonanotte.")
                quit()
            elif "wikipedia" in query:
                self.wikiSearch(query)
            elif "scrivi una mail" in query or "invia una mail" in query:
                try:
                    speak("Quale sarà il contenuto della mail?")
                    mailContent = self.listen()
                    speak("Inserire l'email del destinatario.")
                    to = input()
                    self.sendMail(to, mailContent)
                    speak("Email inviata correttamente")
                except Exception as e:
                    print(e)
                    speak("Impossibile inviare la mail.")


        
