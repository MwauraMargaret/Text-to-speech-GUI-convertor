import tkinter as tk
from tkinter import *
import pyttsx3
from gtts import gTTS
import os

engine = pyttsx3.init()

#Get available voices
voices = engine.getProperty('voices')

#Function to speak
def speaknow():
    text = textv.get()  # Get the actual text input
    if text.strip():  # Avoid speaking empty input
        engine.setProperty('rate', speed_var.get)
        engine.setProperty('voice', voices[voice_var.get()].id)
        engine.say(text)
        engine.runAndWait()
    engine.stop()

#Function to Save Audio File
def save_audio():
    text = textv.get()
    if text.strip():
        tts = gTTS(text=text, lang=lang_var.get())  # Use selected language
        filename = "output.mp3"
        tts.save(filename)
        os.system("start " + filename)  # Open audio file (Windows)
        # Use "afplay" on Mac or "mpg321" on Linux

root = Tk()
root.title("Text to Speech")
root.geometry("500x350")
root.resizable(False,False)

textv = StringVar()

#Frame
obj = LabelFrame(root, text="Text to speech", font=20, bd=1)
obj.pack(fill="both", expand="yes", padx=10, pady=10)

#Label & Text Entry
lbl = Label(obj, text="Text", font=30)
lbl.pack(side=tk.LEFT, padx=5)

text = Entry(obj, textvariable=textv, font=30, width=25, bd=5)
text.pack(side=tk.LEFT, padx=10)

# Voice Selection (Male/Female)
voice_var = IntVar(value=0)  # Default to first voice
voice_label = Label(root, text="Select Voice:")
voice_label.pack()
voice_menu = OptionMenu(root, voice_var, *range(len(voices)))  # Dynamic voice list
voice_menu.pack()

# Speed Control
speed_var = IntVar(value=150)  # Default speed
speed_label = Label(root, text="Speech Speed:")
speed_label.pack()
speed_scale = Scale(root, from_=50, to=300, orient=HORIZONTAL, variable=speed_var)
speed_scale.pack()

# Language Selection (for saving audio)
lang_var = StringVar(value="en")  # Default English
lang_label = Label(root, text="Select Language:")
lang_label.pack()
lang_menu = OptionMenu(root, lang_var, "en", "es", "fr", "de")  # English, Spanish, French, German
lang_menu.pack()

#Buttons
btn_speak = Button(obj, text="Speak", font=20, bg="black", fg="white", command=speaknow)
btn_speak.pack(pady = 10)

btn_save = Button(root, text="Save as MP3", font=20, bg="green", fg="white", command=save_audio)
btn_save.pack(pady=10)

root.mainloop()