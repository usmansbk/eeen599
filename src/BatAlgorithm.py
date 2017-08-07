# Copyright 2017 Babakolo Usman Suleiman
# This program is distributed under the terms of the GNU
# General Public License (GPL).

from ImageStat import *
from ImageUtil import *
from ImageModel import ImageModel
import copy

class BatAlgorithm:
    def __init__(self):
        print 'Initializing local search BAT Algorithm'
        #bat params config
        self.frequency = None
        self.velocity = None
        self.location = (0, 0)
        self.bat_population = 1
        self.pulse_rate_emmision = None
        self.loudness = None
        self.max_iterations = 1000


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
        found = False
        should_display = False
        for itr in range(max_iterations):
            row = self.location[0]
            col = self.location[1]
            region = getregion(self.gray, row, col, self.subimglength,
                                self.subimgheight, self.imgHeight,
                                self.imglength)
            data = {'mean': self.mean, 'stddev': self.stddev, 'median': self.median}
            found = fitness(region, data)
            if (found):
                should_display = True
                print 'Found at location X:', col, 'Y:',row
                markRegion(self.imgcopy, row, col, self.subimglength, self.subimgheight)
                break
            else:
                self.location[]
        return [should_display, self.imgcopy]
