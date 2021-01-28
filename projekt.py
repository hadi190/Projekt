import tkinter as tk
import pymongo
import time
import re

from pymongo import MongoClient
client = MongoClient()

def resize(e):

    size = e.width / 10
    labelsize = e.width / 23
    buttonsize = e.width / 33

    label.config(font=("Courier", int(size)))
    anvLabel.config(font=("Courier", int(labelsize)))
    lösLabel.config(font=("Courier", int(labelsize)))
    loggaIn.config(font=("Courier", int(buttonsize)))
    skapa.config(font=("Courier", int(buttonsize)))
    skapaLabel.config(font=("Courier", int(labelsize))) 
    skapaNamnLabel.config(font=("Courier", int(labelsize)))
    SkapalösLabel.config(font=("Courier", int(labelsize)))
    SkapalösLabeltvå.config(font=("Courier", int(labelsize)))
    skapafull.config(font=("Courier", int(buttonsize)))

def slutför():
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]') 

    if(regex.search(skapaNamn.get()) == None):
        if len(skapaNamn.get()) > 4:
            if len(skapaLösenord.get()) > 4:
                if skapaLösenord.get() == skapaLösenordtvå.get():
                    print("grattis det skulle funka!")

    else : 
        print("skulle inte funka :(")

def skapaSÄ():
    anvLabel.place_forget()
    användarnamn.place_forget()
    lösLabel.place_forget()
    lösenord.place_forget()
    loggaIn.place_forget()
    skapaLabel.place_forget()
    skapa.place_forget()
    tillbaka.place(relwidth=0.1,relheight=0.07)
    skapaNamnLabel.place(rely=0.25, relx=0.25, relwidth=0.5,relheight=0.05)
    skapaNamn.place(rely=0.3, relx=0.25, relwidth=0.5, relheight=0.05)
    SkapalösLabel.place(rely=0.4, relx=0.25, relwidth=0.5,relheight=0.05)
    skapaLösenord.place(rely=0.45, relx=0.25, relwidth=0.5, relheight=0.05)
    SkapalösLabeltvå.place(rely=0.56, relx=0.25, relwidth=0.5, relheight = 0.04)
    skapaLösenordtvå.place(rely=0.61, relx=0.25, relwidth=0.5, relheight=0.05)
    skapafull.place(rely=0.72, relx=0.35, relwidth=0.3, relheight = 0.1)

def returnHome():
    skapaNamnLabel.place_forget()
    skapaNamn.place_forget()
    tillbaka.place_forget()
    SkapalösLabel.place_forget()
    skapaLösenord.place_forget()
    SkapalösLabeltvå.place_forget()
    skapaLösenordtvå.place_forget()
    skapafull.place_forget()
    time.sleep(0.1)

    label.place(rely=0.01, relx=0.1, relwidth=0.8, relheight=0.3)
    anvLabel.place(rely=0.25, relx=0.25, relwidth=0.5,relheight=0.05)
    användarnamn.place(rely=0.3, relx=0.25, relwidth=0.5, relheight=0.05)
    lösLabel.place(rely=0.4, relx=0.25, relwidth=0.5,relheight=0.05)
    lösenord.place(rely=0.45, relx=0.25, relwidth=0.5, relheight=0.05)
    loggaIn.place(rely=0.53, relx=0.35, relwidth=0.3, relheight = 0.1)
    skapaLabel.place(rely=0.65, relx=0.35, relwidth=0.3, relheight = 0.04)
    skapa.place(rely=0.72, relx=0.35, relwidth=0.3, relheight = 0.1)

HEIGHT = 700
WIDTH = 1100

root = tk.Tk()
canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH)
canvas.pack()

frame = tk.Frame(root, bg="#b8d6de")
frame.place(relx=0.3,rely=0.05,relwidth=0.4,relheight=0.85)

tillbaka = tk.Button(frame, text="<--", command=returnHome)
tillbaka.config(font=("Courier", 20))

label = tk.Label(frame, text="The Room", bg="#b8d6de")
label.config(font=("Courier", 20))
label.place(rely=0.01, relx=0.1, relwidth=0.8, relheight=0.3)

anvLabel = tk.Label(frame, text="Användarnamn", bg="#b8d6de")
anvLabel.config(font=("Courier", 15))
anvLabel.place(rely=0.25, relx=0.25, relwidth=0.5,relheight=0.05)

användarnamn = tk.Entry(frame)
användarnamn.place(rely=0.3, relx=0.25, relwidth=0.5, relheight=0.05)

lösLabel = tk.Label(frame, text="Lösenord", bg="#b8d6de")
lösLabel.config(font=("Courier", 15))
lösLabel.place(rely=0.4, relx=0.25, relwidth=0.5,relheight=0.05)

lösenord = tk.Entry(frame)
lösenord.config(show="*")
lösenord.place(rely=0.45, relx=0.25, relwidth=0.5, relheight=0.05)

loggaIn = tk.Button(frame, bg="white", text="Logga in")
loggaIn.config(font=("Courier", 10))
loggaIn.place(rely=0.53, relx=0.35, relwidth=0.3, relheight = 0.1)

skapaLabel = tk.Label(frame, bg="#b8d6de", text="Eller")
skapaLabel.config(font=("Courier", 10))
skapaLabel.place(rely=0.65, relx=0.35, relwidth=0.3, relheight = 0.04)

skapa = tk.Button(frame, bg="white", text="Skapa användare", command=skapaSÄ)
skapa.config(font=("Courier", 10))
skapa.place(rely=0.72, relx=0.35, relwidth=0.3, relheight = 0.1)

skapaNamnLabel = tk.Label(frame, bg="#b8d6de", text="Välj Användarnamn")
skapaNamnLabel.config(font=("Courier", 15))

skapaNamn = tk.Entry(frame)

SkapalösLabel = tk.Label(frame, text="Välj lösenord", bg="#b8d6de")
SkapalösLabel.config(font=("Courier", 15))

skapaLösenord = tk.Entry(frame)
skapaLösenord.config(show="*")

SkapalösLabeltvå = tk.Label(frame, text="Ange lösenordet", bg="#b8d6de")
SkapalösLabeltvå.config(font=("Courier", 15))

skapaLösenordtvå = tk.Entry(frame)
skapaLösenordtvå.config(show="*")

skapafull = tk.Button(frame, bg="white", text="Skapa användare", command=slutför)
skapafull.config(font=("Courier", 10))


root.bind("<Configure>", resize)
root.mainloop()