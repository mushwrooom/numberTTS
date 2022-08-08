from cgitb import text
from genericpath import exists
from multiprocessing.connection import wait
from tkinter import *
from gtts import gTTS
import random
import os

from requests import delete


root = Tk()
root.title('Number Memorizer')
root.geometry('400x400')

rangeMin = 10
rangeMax = 10000
number = random.randint(rangeMin, rangeMax)

myLabel = Label(root, text='Put in a guess')
myLabel.grid(row=0, column=1)

def speak(text):
    tts = gTTS(text=str(text), lang='hu')

    file = "tts.mp3"
    tts.save(file)
    os.system("mpg123 " + file)

def randomize():
    global number
    number = random.randint(rangeMin, rangeMax)


def enter(event):
    guess()

def guess():
    global myLabel
    n = int(e.get())
    if n == number:
        myLabel.config(text='Correct!')
        randomize()
    else:
        myLabel.config(text='Wrong!')
    e.delete(0, 'end')

def speakButton():
    speak(number)
    myLabel.config(text='Put in a guess')

e = Entry(root, width=20)
e.grid(row=0, column=0)
e.focus()
e.bind("<Return>", enter)

mySpeakButton = Button(root, text='Speak', width=20, height=10, command=speakButton)
mySpeakButton.grid(row=1, column=0)

myGuessButton = Button(root, text='Guess', command=guess)
myGuessButton.grid(row=0, column=2)

myRandomizeButton = Button(root, text='Randomize', width=20, height=10, command=randomize)
myRandomizeButton.grid(row=1, column=1)


root.mainloop()
if os.path.exists('tts.mp3'):
    os.remove('tts.mp3')