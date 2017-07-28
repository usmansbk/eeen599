# Copyright 2017 Babakolo Usman Suleiman
# This program is distributed under the terms of the GNU
# General Public License (GPL).

from ImageStat import *
from ImageUtil import *
from ImageModel import ImageModel
import copy

class BatAlgorithm:
    def __init__(self):
        #bat params config
        pass

    def setImage(self, img):
        self.img = img
        self.gray = asGrayScale(img)
        self.imgcopy = copy.deepcopy(self.img)

    def setTemplate(self, subimg):
        self.subimg = subimg
        self.subgray = asGrayScale(subimg)

    def computeFitness(self):
        self.mean = get_mean(self.subgray)
        self.stddev = stddeviation(self.subgray)
        self.imglength = len(self.img[0])
        self.imgHeight = len(self.img)
        self.subimglength = len(self.subimg[0])
        self.subimgheight = len(self.subimg)

    def search(self):
        pass
