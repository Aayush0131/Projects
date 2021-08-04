from tkinter import *
import tkinter as tk
from tkinter import messagebox
import cv2
import os
from PIL import Image, ImageTk
import numpy as np
from image_model import Image_Model
from audio_detection import Audio_model
from rasa.jupyter import chat
import nest_asyncio
import webbrowser
import emoji



window=tk.Tk()
window.title("MOOD DETECTOR")
window.geometry("800x800")
window.configure(bg='black')


l1=tk.Label(window, text= "What Do You Want to do   ;) ",font=("Algerian", 20),bg='black', fg='white' )
l1.grid(row=0,column=0,padx=10, pady=10)

############### Functions
im = Image_Model()
am=Audio_model()


def emojify(x):
    if x =='HAPPY':
        em = (emoji.emojize(":beaming_face_with_smiling_eyes:"))
        return em
    if x =='FEAR':
        em=(emoji.emojize(":worried_face:"))
        return em
    if x =='CALM':
        em=(emoji.emojize(":smiling_face_with_halo:"))
        return em
    if x =='SURPRISE':
        em=(emoji.emojize(":flushed_face:"))
        return em
    if x =='NEUTRAL':
        em=(emoji.emojize(":grinning_face_with_big_eyes:"))
        return em
    if x =='SAD':
        em=(emoji.emojize(":pensive_face:"))
        return em
    if x =='ANGRY':
        em=(emoji.emojize(":exploding_head:"))
        return em
    if x =='DISGUST':
        em=(emoji.emojize(":grimacing_face:"))
        return em
def chat_bot():
    nest_asyncio.apply()
    endpoints = "endpoints.yml"
    chat(r"C:\Users\Piyush\Desktop\Bharat\chatbot\models\20210425-234947.tar.gz", endpoints)
def voice():
    am.voice_input()
    AUDIO_RESULT=am.predict()
    ar=AUDIO_RESULT.upper()
    emoj = emojify(ar)
    final_string = ar + emoj
    show_answer(final_string)
    everything(ar)
def image():
    im.camera_input()
    IMAGE_RESULT=im.predict_image()
    ir=IMAGE_RESULT.upper()
    emoj = emojify(ir)
    final_string = ir + emoj
    show_answer(final_string)
    everything(ir)

def openweb_memes():
    webbrowser.open(url="https://br.pinterest.com/levato/meme/",new=1)

def openweb_songs(x):
    if x =='HAPPY':
        playlist="https://open.spotify.com/playlist/0deORnapZgrxFY4nsKr9JA"
    if x =='FEAR':
        playlist='https://open.spotify.com/playlist/2b3dA71D3hboLuPCJIcrvT?si=qwL2N6UeTjm04xPsv9ta5g&nd=1'
    if x =='CALM':
        playlist="https://open.spotify.com/playlist/0deORnapZgrxFY4nsKr9JA"
    if x =='SURPRISE':
        playlist="https://open.spotify.com/playlist/0deORnapZgrxFY4nsKr9JA"
    if x =='NEUTRAL':
        playlist="https://open.spotify.com/playlist/0deORnapZgrxFY4nsKr9JA"
    if x =='SAD':
        playlist="https://open.spotify.com/playlist/2w3VZH1WYFz2oHscFcCYay?si=xzhxNuJmSgS3YRzasmpIOw&nd=1"
    if x =='ANGRY':
        playlist="https://open.spotify.com/playlist/1c73hxx0X23lIP0B5S9O1h?si=OTqoXh2PQTyyDUwdGt8q1w&nd=1"
    if x =='DISGUST':
        playlist = "https://open.spotify.com/playlist/4gUPJbQtKVMRMUR70ILsxQ?si=EMSd8kfNRxyM5_WiiEFCew&nd=1"
    webbrowser.open(url=playlist,new=1)

def openweb_games():
    webbrowser.open(url="https://www.retrogames.cz/?language=EN",new=1)
####################

b1=tk.Button(window, text="    CLICK A PHOTO    ",font=("Algerian", 20),bg='black', fg='white', command=image)
b1.grid(row=2,column=0,padx=10, pady=10)

b2=tk.Button(window, text="    RECORD AUDIO    ",font=("Algerian",20),bg='black', fg='white', command=voice)
b2.grid(row=3,column=0,padx=10, pady=10)

def show_answer(x):
    # if you want the button to disappear:
    # button.destroy() or button.pack_forget()
    label = Label(window, text= "YOU SEEMS TO BE "+ x,font=("Algerian", 20),bg='black', fg='white')
    #this creates a new label to the GUI
    label.grid(row=4,column=0,padx=50,pady=50) 


def everything(x):
    memes=tk.Button(window, text="    WANNA SEE MEMES    ",font=("Algerian", 20),bg='black', fg='white',command = openweb_memes)
    memes.grid(row=5,column=0,padx=10, pady=10)

    songs=tk.Button(window, text="    WANNA LISTEN SONGS    ",font=("Algerian",20),bg='black', fg='white',command = lambda: openweb_songs(x))
    songs.grid(row=5,column=1,padx=10, pady=10)

    games=tk.Button(window, text="    WANNA PLAY RETRO GAMES    ",font=("Algerian",20),bg='black', fg='white',command= openweb_games)
    games.grid(row=6,column=0,padx=10, pady=10)

    chat_button=tk.Button(window, text="    CHATBOT    ",font=("Algerian",20),bg='black', fg='white', command=chat_bot )
    chat_button.grid(row=6,column=1,padx=10, pady=10)

window.mainloop()