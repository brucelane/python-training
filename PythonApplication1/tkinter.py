import tkinter as tk

from tkinter import *

root = tk.Tk()
app = tk.Frame(root)
app.pack()

def bonjour():
    print("hi")

bouton = tk.Button(app, text="yo", command=bonjour)
bouton.pack(side="top")

quitter = tk.Button(app, text="QUIT", fg="red", command=app.destroy)
quitter.pack(side="bottom")

app.mainloop()