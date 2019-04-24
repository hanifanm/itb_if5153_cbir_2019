import cv2
import numpy as np
import matplotlib.pyplot as plt
import Tkinter as tk
from Tkinter import *
from tkFileDialog import askopenfilename
from PIL import Image, ImageTk
import shapeMatcherUIComm
import imageManipulator
import histogramMatcher



def client_exit():
    exit()

def show_results(results):
    x = 0
    y = 0
    counter = 0
    global reslut
    reslut = []
    for i in matched_images:
        im2res = imageManipulator.image_resize(i, height=100)
        reslut.append(read_image(im2res))
        r1 = tk.Label(shapeMatcherResult, image=reslut[counter]).grid(padx= 10, pady = 10,row=y,column=x)
        counter = counter + 1
        x = x + 1
        if x == 6:
            y = y+1
            x = 0

def shape_match():
    global matched_images
    matched_images = []
    matched_images = shapeMatcherUIComm.shapeMatcher(query)
    show_results(matched_images)

def histogram_match():
    if not matched_images:
        print "no matched image"
##        histogramMatcher.histogram_match_from_beginning(query)
    else:
        print "image has been matched"
        histogramMatcher.histogram_match(cv2.imread(query),matched_images,0)
##    show_results(matched_images)

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
    im2res = imageManipulator.image_resize(im2, height=100)
    res = read_image(im2res)
    w1 = tk.Label(frame, image=res).grid(padx= 10, pady = 10,row=1,column=0)


root = tk.Tk()

frame = tk.Frame(root, borderwidth=1)#,highlightbackground="black", highlightthickness=1)
frame.grid(row=0,column=0, sticky=N)
global matched_images
matched_images = []

# creating a button instance
getImageButton = Button(frame, text="Upload Query Image",command=get_image)
getImageButton.grid(padx= 10, pady = 10,row=0,column=0)

shapeMButton = Button(frame, text="Shape Matcher",command=shape_match)
shapeMButton.grid(padx= 10, pady = 10, row=2,column=0)

shapeMButton = Button(frame, text="Histogram Matcher",command=histogram_match)
shapeMButton.grid(padx= 10, pady = 10, row=3,column=0)

shapeMatcherResult = tk.Frame(root, borderwidth=1,highlightbackground="black", highlightthickness=1)
shapeMatcherResult.grid(padx= 10, pady = 10,row=0,column=1,sticky=N)

root.mainloop()
