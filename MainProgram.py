from tkinter.constants import X
from typing import Container, Text
from Soul import *
import speech_recognition as sr #pip install SpeechRecognition
from wikipedia.wikipedia import summary 
import tkinter as tk    #Parte grafica



#-  -   -   -   -   -   -   -   -   PARTE GRAFICA    -   -   -   -   -   -
window = tk.Tk()    #creazione finestra
window.geometry("600x600")  #Dimensioni
window.title("Azzurra") #Titolo
window.configure(background='#252525')
window.resizable(False, False) #non sarà possibile ridimenzionare scheda

#Il titolo che apparirà al centro dello schermo
title = tk.Label(window, text="AZZURRA", background="#252525", foreground="#158BFF", font=("Bold", 50))
title.place(x=130, y=20)

#Il bottone per iniziare a parlare
provaBottone = tk.Button(text="BOTTONE", bd=5)
provaBottone.place(x=275, y=200)



#-  -   -   -   -   -   -   -   -   MAIN -  -   -   -   -   -   -   -   
if __name__ == "__main__":
    window.mainloop()   #Avvio finestra (dovrò metterla dentro la funzione main )

    #Inizializzazione anima di Aurora
    AuroraSoul = Soul()
    AuroraSoul.main()


