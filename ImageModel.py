"""
This class represents an image model
"""
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

class ImageModel:

    def __init__(self, imagepath):
        self.img = Image.open(imagepath)
        self.imgarr = np.asarray(self.img)
        print(self.imgarr);

    def getMatrix(self):
        return self.imgarr;

    def display(self):
        plt.imshow(self.imgarr)
        print(self.imgarr)
        plt.show()
