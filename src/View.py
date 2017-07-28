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

class View:
    def __init__(self, title):
    	self.top = Tk()
    	self.top.title(title)
        self.top.iconbitmap('assets/icon.ico')
    	self.imgfilename = 'assets/noimg.png'
    	self.tmpfilename = 'assets/noimg.png'
    	self.initialize()

    def load_image(self):
        filename = askopenfilename(parent=self.top)
        if (filename != ''):
            self.imgfilename = filename
            img = Image.open(self.imgfilename)
            self.imagecanvas.config(width=img.width, height=img.height)
            self.imagecanvas.image = ImageTk.PhotoImage(img)
            self.imagecanvas.create_image(0,0,image=self.imagecanvas.image, anchor='nw')
            self.imagecanvas.pack()
            self.top.update()

    def load_template(self):
    	filename = askopenfilename(parent=self.top)
        if (filename != ''):
            self.tmpfilename = filename
            tmp = Image.open(self.tmpfilename)
            self.templatecanvas.config(width=tmp.width, height=tmp.height)
            self.templatecanvas.image = ImageTk.PhotoImage(tmp)
            self.templatecanvas.create_image(0,0,image=self.templatecanvas.image, anchor='nw')
            self.templatecanvas.pack()
            self.top.update()

    def search(self):
        ### Create Image Model Objects
        print self.tmpfilename
        print self.imgfilename
        if (self.tmpfilename == 'assets/noimg.png' or self.imgfilename == 'assets/noimg.png'):
            self.var.set("SELECT IMAGE AND TEMPLATE")
        elif (self.tmpfilename != '' and self.imgfilename != ''):
            self.var.set('SEARCHING...')
            self.top.update()
            subModel = ImageModel(self.tmpfilename)
            imgModel = ImageModel(self.imgfilename)

            ### Convert Image to Matrix
            iarr = imgModel.getMatrix()
            siarr = subModel.getMatrix()

            ### Instantiate a LocalSearch Object
            local_search = LocalSearch(iarr, siarr)

            ### Instantiate Algorithm
            test_algo = TestAlgorithm()

            ### Pass Algorithm to local search function
            found = local_search.search(test_algo)
            if found:
                self.var.set('TEMPLATE MATCH FOUND')
            else:
                self.var.set('TEMPLATE MATCH NOT FOUND')
        else:
            self.var.set('ENCOUNTERED ERROR!')
        self.top.update()

    def initialize(self):
    	im = Image.open(self.imgfilename)
    	self.imagecanvas = Canvas(self.top, height=im.height, width=im.width)
    	self.imagecanvas.image = ImageTk.PhotoImage(im)
    	self.imagecanvas.create_image(0,0,image=self.imagecanvas.image, anchor='nw')
    	self.imagecanvas.pack()

    	# Button
    	self.imageButton = Button(self.top, text="Image", command=self.load_image)
    	self.imageButton.pack()

    	tmp = Image.open(self.tmpfilename)
    	self.templatecanvas = Canvas(self.top, height=tmp.height, width=tmp.width)
    	self.templatecanvas.image = ImageTk.PhotoImage(tmp)
    	self.templatecanvas.create_image(0,0,image=self.templatecanvas.image, anchor='nw')
    	self.templatecanvas.pack()

    	self.templateButton = Button(self.top, text="Template Image", command=self.load_template)
    	self.templateButton.pack()

         # Search Button
    	self.searchButton = Button(self.top, text="Search", command=self.search)
    	self.searchButton.pack()

        self.var = StringVar()
        self.status = Label(self.top, textvariable=self.var)
        self.var.set('IDLE')
        self.status.pack()

    	self.top.mainloop()
