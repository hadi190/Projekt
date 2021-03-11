import tkinter as tk
import pymongo
import time
import re
import socket
import threading

from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017')
UserDB = client.Users.users
Chatt = client.Chatt

HEIGHT = 700
WIDTH = 1100

allmänID = "gnfsgngs"

root = tk.Tk()
canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH)
canvas.pack()


def firstPage():
    frame.place_forget()
    frontframe.place(relx=0,rely=0,relwidth=1,relheight=1)
    sideframe.place(relwidth=0.17, relheight=1)
    chatView.place(relwidth=0.83, relheight=0.95, relx=0.17)
    chatText.place(relwidth=0.83,relheight=0.05, rely=0.95, relx=0.17)
    allmänt.place(relwidth=1,relheight=0.08)


def hemsida():
    for item in home:
        item.destroy()
    for stuff in nyAnv:
        stuff.destroy()

    firstPage()

def öppnaChatt():
    for linjer in Chatt.Public:

        text = linjer.find_one()

        linjer = tk.Label(chatText, bg="#F0F0F0", text=text)
        
        linjer.place(relwidth=1,relheight=1)

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
    error.config(font=("Courier", int(buttonsize)))

def loggainKonto():
    login_namn = UserDB.find_one({"namn": användarnamn.get()})

    if login_namn.lösenord == lösenord.get():
        print("Rätt!")
    #insert code for checking username and pass on database
    hemsida()


AllText = Chatt.Public.find()


def slutför():
    regex = re.compile('[@_!#$%^&*()<>?/|}{~:]') 

    if(regex.search(skapaNamn.get()) == None):
        if len(skapaNamn.get()) > 4:
            if len(skapaLösenord.get()) > 4:
                if skapaLösenord.get() == skapaLösenordtvå.get():
                    if UserDB.find({"namn": skapaNamn.get()}).count() <= 0:
                        user_data = {
                            "namn" : skapaNamn.get(),
                            "lösenord" : skapaLösenord.get()
                        }   
                        UserDB.insert_one(user_data)
                        hemsida()
                    else :
                        error.config(text="Det finns redan en användare med det namnet!")
                else :
                    error.config(text="Lösenorden stämmer inte!")
            else :
                error.config(text="Lösenordet måste vara längre än 4 karaktärer!")
        else :
            error.config(text="Namnet måste vara längre än 4 karaktärer!")
    else : 
        error.config(text="Du måste använda bokstäver!")

def skapaSÄ():

    for stuff in home:
        stuff.place_forget()
    
    label.place(rely=0.01, relx=0.1, relwidth=0.8, relheight=0.3)
    tillbaka.place(relwidth=0.1,relheight=0.07)
    skapaNamnLabel.place(rely=0.25, relx=0.25, relwidth=0.5,relheight=0.05)
    skapaNamn.place(rely=0.3, relx=0.25, relwidth=0.5, relheight=0.05)
    SkapalösLabel.place(rely=0.4, relx=0.25, relwidth=0.5,relheight=0.05)
    skapaLösenord.place(rely=0.45, relx=0.25, relwidth=0.5, relheight=0.05)
    SkapalösLabeltvå.place(rely=0.56, relx=0.25, relwidth=0.5, relheight = 0.04)
    skapaLösenordtvå.place(rely=0.61, relx=0.25, relwidth=0.5, relheight=0.05)
    error.place(rely=0.664, relx=0.01, relwidth=1, relheight=0.03)
    skapafull.place(rely=0.72, relx=0.35, relwidth=0.3, relheight = 0.1)

def returnHome():
    for item in nyAnv:
        item.place_forget()

    label.place(rely=0.01, relx=0.1, relwidth=0.8, relheight=0.3)
    anvLabel.place(rely=0.25, relx=0.25, relwidth=0.5,relheight=0.05)
    användarnamn.place(rely=0.3, relx=0.25, relwidth=0.5, relheight=0.05)
    lösLabel.place(rely=0.4, relx=0.25, relwidth=0.5,relheight=0.05)
    lösenord.place(rely=0.45, relx=0.25, relwidth=0.5, relheight=0.05)
    loggaIn.place(rely=0.53, relx=0.35, relwidth=0.3, relheight = 0.1)
    skapaLabel.place(rely=0.65, relx=0.35, relwidth=0.3, relheight = 0.04)
    skapa.place(rely=0.72, relx=0.35, relwidth=0.3, relheight = 0.1)


frame = tk.Frame(root, bg="#b8d6de")
frame.place(relx=0.3,rely=0.05,relwidth=0.4,relheight=0.85)

frontframe = tk.Frame(root, bg="#FF5733")
sideframe =tk.Frame(frontframe, bg="#F0F0F0", bd=1)
chatText = tk.Entry(frontframe, bg="#F0F0F0")
chatView = tk.Frame(frontframe, bg="#b8d6de")

allmänt = tk.Button(sideframe, bg="#F0F0F0", text="Den allmänna chatten", command=öppnaChatt)
allmänt.config(font=("Courier", 10))

tillbaka = tk.Button(root, text="<--", command=returnHome)
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

loggaIn = tk.Button(frame, bg="white", text="Logga in", command=loggainKonto)
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

error = tk.Label(frame, bg="#b8d6de", text="", fg="#c32340")
error.config(font=("Courier", 15))

home = (label, anvLabel, användarnamn, lösLabel, lösenord, loggaIn, skapaLabel, skapa)
nyAnv = (tillbaka, skapaNamnLabel, skapaNamn, SkapalösLabel, skapaLösenord, SkapalösLabeltvå, skapaLösenordtvå, skapafull, error)


def skicka(nugget):
    Chatt.Public.insert(nugget)



chatText.bind("<Return>", skicka(chatText.get()))





root.bind("<Configure>", resize)
root.mainloop()