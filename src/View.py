from Tkinter import *
from tkFileDialog import *
import tkMessageBox
from PIL import Image, ImageTk


from ImageModel import ImageModel
from ImageUtil import *
from ImageStat import *


from LocalSearch import LocalSearch
from TestAlgorithm import TestAlgorithm
import matplotlib.pyplot as plt
import copy

top = Tk()
top.title('Image Search - BA')

imgfilename = 'img/noimg.png'
tmpfilename = 'img/noimg.png'

def load_image():
    imgfilename = askopenfilename(parent=top)
    img = Image.open(imgfilename)
    imagecanvas.config(width=img.width, height=img.height)
    imagecanvas.image = ImageTk.PhotoImage(img)
    imagecanvas.create_image(0,0,image=imagecanvas.image, anchor='nw')
    imagecanvas.pack()
    top.update()

def load_template():
    templatefilename = askopenfilename(parent=top)
    tmp = Image.open(templatefilename)
    templatecanvas.config(width=tmp.width, height=tmp.height)
    templatecanvas.image = ImageTk.PhotoImage(tmp)
    templatecanvas.create_image(0,0,image=templatecanvas.image, anchor='nw')
    templatecanvas.pack()
    top.update()

def search():
    ### Create Image Model Objects
    subModel = ImageModel(tmpfilename)
    imgModel = ImageModel(imgfilename)

    ### Convert Image to Matrix
    iarr = imgModel.getMatrix()
    siarr = subModel.getMatrix()

    ### Instantiate a LocalSearch Object
    local_search = LocalSearch(iarr, siarr)

    ### Instantiate Algorithm
    test_algo = TestAlgorithm()

    ### Pass Algorithm to local search function
    local_search.search(test_algo)


# Canvas
im = Image.open(imgfilename)
imagecanvas = Canvas(top, height=im.height, width=im.width)
imagecanvas.image = ImageTk.PhotoImage(im)
imagecanvas.create_image(0,0,image=imagecanvas.image, anchor='nw')
imagecanvas.pack()

# Button
imageButton = Button(top, text="Image", command=load_image)
imageButton.pack()

tmp = Image.open(tmpfilename)
templatecanvas = Canvas(top, height=tmp.height, width=tmp.width)
templatecanvas.image = ImageTk.PhotoImage(tmp)
templatecanvas.create_image(0,0,image=templatecanvas.image, anchor='nw')
templatecanvas.pack()

templateButton = Button(top, text="Template Image", command=load_template)
templateButton.pack()

# Search Button
searchButton = Button(top, text="Search", command=search)
searchButton.pack()

top.mainloop()
