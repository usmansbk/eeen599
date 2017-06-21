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

    def display(self, arr=[]):
        if (len(arr) == 0):
            plt.imshow(self.imgarr)
            print self.imgarr
            plt.show()
        else:
            plt.imshow(arr)
            plt.show()
