"""
This class represents an image model
"""
import copy
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

class ImageModel:

    def __init__(self, imagepath):
        self.ext = imagepath[-3:]
        self.img = Image.open(imagepath)
        self.imgarr = np.asarray(self.img)
        #print self.imgarr;

    def getMatrix(self):
        return self.imgarr;

    def asGrayScale(self):
        '''
        Returns this ImageModel as grayscale
        '''
        gray = self.img.convert('L')
        gray.save('img/gray.' + self.ext)
        return ImageModel('img/gray.' + self.ext)

    def display(self):
        plt.imshow(self.imgarr)
        print self.imgarr
        plt.show()

    def markRegion(self, x, y, length, height):
        drawLine(self, x1, x2, length) #top
        drawLine(self, x1, x2, length) #bottom
        drawLine(self, y1, y2, height) #left
        drawLine(self, y1, y2, height) #right
