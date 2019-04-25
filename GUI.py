from __future__ import division
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

global true_positive
global false_positive
global false_negative
global result_wanted
global button_shown
result_wanted = 12

def client_exit():
    exit()

def show_results(results):
    x = 0
    y = 0
    counter = 0
    global reslut
    reslut = []
    for widget in shapeMatcherResult.winfo_children():
        widget.destroy()
    for i in results:
        im2res = imageManipulator.image_resize(i, height=100)
        reslut.append(read_image(im2res))
        r1 = tk.Label(shapeMatcherResult, image=reslut[counter]).grid(padx= 10, pady = 10,row=y,column=x)
        counter = counter + 1
        x = x + 1
        if x == 6:
            y = y+1
            x = 0

def get_precision():
    if true_positive == 0 and false_positive == 0:
        prec = 0
        ptext = "Precision:\n0"
    else:
        prec = true_positive/(true_positive+false_positive)
        ptext = "Precision:\n{:1.2f}".format(prec)
    msg = tk.Message(frame, text=ptext)
    msg.grid(row=6,column=0, sticky=W)
    msg.config(font=('times', 15, 'italic'))
    return prec

def get_recall():
    if true_positive == 0 and false_negative == 0:
        rec = 0
        ptext = "Recall: \n0"
    else:
        rec = true_positive/(true_positive+false_negative)
        ptext = "Recall: \n{:1.2f}".format(rec)
    msg2 = tk.Message(frame, text=ptext)
    msg2.grid(row=7,column=0,sticky=W)
    msg2.config(font=('times', 15, 'italic'))
    return rec

def get_f_measure():
    precision = get_precision()
    recall = get_recall()
    if precision == 0 and recall == 0:
        ptext = "F1-Score\n0"
    else:
        fmeas = 2 * (precision * recall) / (precision + recall);
        ptext = "F1-Score:\n{:1.2f}".format(fmeas)
    msg2 = tk.Message(frame, text=ptext)
    msg2.grid(row=8,column=0,sticky=W)
    msg2.config(font=('times', 15, 'italic'))

def get_tp_fp_fn(relevant_data, result_codes):
    global true_positive
    global false_positive
    global false_negative
    true_positive = 0
    false_positive = 0
    false_negative = 0
    for result_code in result_codes:
        #print ("Query: ", query.split('images/',1)[1][0:4], " result: ",result_code )
        if query.split('images/',1)[1][0:4] == result_code:
            true_positive = true_positive + 1
        else:
            false_positive = false_positive + 1
    false_negative = relevant_data - true_positive
    get_f_measure()

def shape_match():
    global matched_images
    matched_images = []
    matched_images = shapeMatcherUIComm.shapeMatcher(query,number_of_result.get())
    show_results(matched_images)
    codenames = shapeMatcherUIComm.get_codenames()
    relevant = shapeMatcherUIComm.get_relevant_data()
    print "Relevant data: ",relevant
    get_tp_fp_fn(relevant, codenames)
##    print("Precision: ",get_precision())
##    print("Recall: ",get_recall())

def histogram_match():
    global final_images
    final_images = []
    final_images = histogramMatcher.histogram_match_from_beginning(query,number_of_result.get())
    show_results(final_images)
    codenames = histogramMatcher.get_codenames()
    relevant = histogramMatcher.get_relevant_data()
    print "Relevant data: ",relevant
    get_tp_fp_fn(relevant, codenames)
##    print("Precision: ",get_precision())
##    print("Recall: ",get_recall())

def all_matcher():
    global matched_images
    matched_images = []
    matched_images = shapeMatcherUIComm.shapeMatcher(query,30)
    codenames = shapeMatcherUIComm.get_codenames()
    relevant = shapeMatcherUIComm.get_relevant_data()
    global final_images
    final_images = []
    final_images = histogramMatcher.histogram_match(cv2.imread(query),matched_images,number_of_result.get(),codenames)
    show_results(final_images)
    codenames = histogramMatcher.get_codenames()
    print "Relevant data: ",relevant
    get_tp_fp_fn(relevant, codenames)
##    print("Precision: ",get_precision())
##    print("Recall: ",get_recall())

def read_image(img):
    #Rearrang the color channel
    b,g,r = cv2.split(img)
    img = cv2.merge((r,g,b))
    # Convert the Image object into a TkPhoto object
    im = Image.fromarray(img)
    imgtk = ImageTk.PhotoImage(image=im) 
    return imgtk

def show_buttons():
    global button_shown
    button_shown = 1
    global number_of_result
    number_of_result = Scale(frame, from_=1, to=30, orient=HORIZONTAL)
    number_of_result.grid(row=1,column=0)

    shapeMButton = Button(frame, text="Shape Matcher",command=shape_match)
    shapeMButton.grid(padx= 5, pady = 5, row=3,column=0)

    shapeMButton = Button(frame, text="Histogram Matcher",command=histogram_match)
    shapeMButton.grid(padx= 5, pady = 5, row=4,column=0)

    shapeMButton = Button(frame, text="UltiMatcher",command=all_matcher)
    shapeMButton.grid(padx= 5, pady = 5, row=5,column=0)

def get_image():
    global res
    global query
    img= askopenfilename()
    query=img
    im2 = cv2.imread(query)
    im2res = imageManipulator.image_resize(im2, height=100)
    res = read_image(im2res)
    w1 = tk.Label(frame, image=res).grid(padx= 10, pady = 10,row=2,column=0)
    if button_shown==0:
        show_buttons()


root = tk.Tk()
root.title('Rider Finder')
frame = tk.Frame(root, borderwidth=1)#,highlightbackground="black", highlightthickness=1)
frame.grid(row=0,column=0, sticky=N)
global query
global matched_images
matched_images = []
global number_of_result
button_shown = 0

# creating a button instance
getImageButton = Button(frame, text="Upload Query Image",command=get_image)
getImageButton.grid(padx= 50, pady = 10,row=0,column=0)

shapeMatcherResult = tk.Frame(root, borderwidth=1,highlightbackground="black", highlightthickness=1)
shapeMatcherResult.grid(row=0,column=1,sticky=N)

root.mainloop()
