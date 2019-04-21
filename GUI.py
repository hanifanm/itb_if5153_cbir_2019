import cv2
import numpy as np
import matplotlib.pyplot as plt
from Tkinter import *

class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)               
        self.master = master

root = Tk()
app = Window(root)
root.mainloop()
