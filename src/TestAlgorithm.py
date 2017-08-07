# Copyright 2017 Babakolo Usman Suleiman
# This program is distributed under the terms of the GNU
# General Public License (GPL).

from ImageStat import *
from ImageUtil import *
from ImageModel import ImageModel
import copy

class TestAlgorithm:
    def __init__(self):
        print 'Initializing Brute Force Search Algorithm'

    def computeFitness(self):
        self.mean = get_mean(self.subgray)
        self.stddev = stddeviation(self.subgray)
        self.median = get_median(self.subgray)
        self.imglength = len(self.img[0])
        self.imgHeight = len(self.img)
        self.subimglength = len(self.subimg[0])
        self.subimgheight = len(self.subimg)

    def setImage(self, img):
        self.img = img
        self.gray = asGrayScale(img)
        self.imgcopy = copy.deepcopy(self.img)

    def setTemplate(self, subimg):
        self.subimg = subimg
        self.subgray = asGrayScale(subimg)

    def search(self):
        rows = self.imgHeight/self.subimgheight
        cols = self.imglength/self.subimglength
        found = False
        should_display = False
        for row in range(rows):
            for col in range(cols):
                print 'row = ', row, 'col = ', col
                r = row * self.subimgheight
                c = col * self.subimglength
                region = getregion(self.gray, r, c, self.subimglength,
                                    self.subimgheight, self.imgHeight,
                                    self.imglength)
                data = {'mean': self.mean, 'stddev': self.stddev, 'median': self.median}
                found = fitness(region, data)
                if (found):
                    should_display = True
                    print 'Found at location X:', c, 'Y:',r
                    markRegion(self.imgcopy, r, c, self.subimglength, self.subimgheight)
                if found: break
            if found: break
        return [should_display, self.imgcopy]
