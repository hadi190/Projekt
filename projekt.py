import tkinter as tk

def test_function():
    print("hej")

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

HEIGHT = 700
WIDTH = 1100

root = tk.Tk()
canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH)
canvas.pack()

frame = tk.Frame(root, bg="#b8d6de")
frame.place(relx=0.3,rely=0.05,relwidth=0.4,relheight=0.85)

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
lösenord.place(rely=0.45, relx=0.25, relwidth=0.5, relheight=0.05)

loggaIn = tk.Button(frame, bg="white", text="Logga in", command=test_function)
loggaIn.config(font=("Courier", 10))
loggaIn.place(rely=0.53, relx=0.35, relwidth=0.3, relheight = 0.1)

skapaLabel = tk.Label(frame, bg="#b8d6de", text="Eller")
skapaLabel.config(font=("Courier", 10))
skapaLabel.place(rely=0.65, relx=0.35, relwidth=0.3, relheight = 0.04)

skapa = tk.Button(frame, bg="white", text="Skapa användare", command=test_function)
skapa.config(font=("Courier", 10))
skapa.place(rely=0.72, relx=0.35, relwidth=0.3, relheight = 0.1)


root.bind("<Configure>", resize)
root.mainloop()