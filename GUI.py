import cv2
import numpy as np
import matplotlib.pyplot as plt
import Tkinter as tk
from Tkinter import *
from tkFileDialog import askopenfilename
from PIL import Image, ImageTk
import shapeMatcherUIComm

def client_exit():
    exit()

def test_function():
    global matched_images
    matched_images = []
    matched_images = shapeMatcherUIComm.shapeMatcher(query)
    cv2.imshow('tes', matched_images[0])
    for i in matched_images:
        cv2.imshow('tes', i)

def read_image(img):
    #Rearrang the color channel
    b,g,r = cv2.split(img)
    img = cv2.merge((r,g,b))
    # Convert the Image object into a TkPhoto object
    im = Image.fromarray(img)
    imgtk = ImageTk.PhotoImage(image=im) 
    return imgtk

def get_image():
    global res
    global query
    img= askopenfilename()
    query=img
    im2 = cv2.imread(query)
    res = read_image(im2)
    w1 = tk.Label(frame, image=res).grid(padx= 10, pady = 10,row=1,column=0)

root = tk.Tk()
#size of the window
#root.geometry("1000x600")

frame = tk.Frame(root, borderwidth=1)#,highlightbackground="black", highlightthickness=1)
frame.grid(row=0,column=0)

# creating a button instance
getImageButton = Button(frame, text="Upload Query Image",command=get_image)
getImageButton.grid(padx= 10, pady = 10,row=0,column=0)

shapeMButton = Button(frame, text="Shape Matcher",command=test_function)
shapeMButton.grid(padx= 10, pady = 10, row=2,column=0)

shapeMatcherResult = tk.Frame(root, borderwidth=1,highlightbackground="black", highlightthickness=1)
shapeMatcherResult.grid(padx= 10, pady = 10,row=0,column=1,sticky=N)

label = tk.Label(shapeMatcherResult, text= "Results will be showing here.")
label.grid(row=0,column=0)
root.mainloop()
