"""
This class represents an image model
"""
import copy
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

class ImageModel:

    def __init__(self, imagepath):
        self.img = Image.open(imagepath)
        self.imgarr = np.asarray(self.img)
        #print self.imgarr;

    def getMatrix(self):
        return self.imgarr;

    def asGrayScale(self):
        '''
        Returns this ImageModel as grayscale
        '''
        self.img.convert('L')
        self.img.save('img/gray.jpg')
        return ImageModel('img/gray.jpg')

    def display(self):
        plt.imshow(self.imgarr)
        print self.imgarr
        plt.show()

    def setBounds(self, x, y, length, height):
        drawLine(self, x1, x2, length) #top
        drawLine(self, x1, x2, length) #bottom
        drawLine(self, y1, y2, height) #left
        drawLine(self, y1, y2, height) #right
