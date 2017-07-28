"""
This class represents an image model
"""
import copy
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

class ImageModel:

    def __init__(self, imagepath='null'):
        if (imagepath != 'null'):
            self.ext = imagepath[-3:]
            self.filename = imagepath[:-4]
            self.img = Image.open(imagepath)
            self.imgarr = np.asarray(self.img)

    def getMatrix(self):
        return self.imgarr;

    def display(self, arr=[]):
        if (len(arr) == 0):
            plt.imshow(self.imgarr)
        else:
            plt.imshow(arr)
        plt.ion()
        plt.draw()
        plt.show()
