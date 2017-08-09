# Copyright 2017 Babakolo Usman Suleiman
# This program is distributed under the terms of the GNU
# General Public License (GPL).

from ImageStat import *
from ImageUtil import *
from ImageModel import ImageModel
import random
import copy

class BatAlgorithm:
    def __init__(self):
        print 'Initializing local search BAT Algorithm'

    def setParams(self):
        self.rows = self.imgHeight / self.subimgheight
        self.cols = self.imglength / self.subimglength
        self.iterations = self.rows * self.cols
        self.location = { 'x':0, 'y': 0}
        self.loudness = 1

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
        self.median = get_median(self.subgray)
        self.imglength = len(self.img[0])
        self.imgHeight = len(self.img)
        self.subimglength = len(self.subimg[0])
        self.subimgheight = len(self.subimg)
        self.setParams()

    def search(self):
        found = False
        should_display = False
        for itr in range(self.iterations):
            r = self.location['x']
            c = self.location['y']
            print 'row', r, ',col', c
            region = getregion(self.gray, r, c, self.subimglength,self.subimgheight, self.imgHeight,self.imglength)
            data = {'mean': self.mean, 'stddev': self.stddev, 'median': self.median}
            found = fitness(region, data)
            if (found):
                should_display = True
                print 'Found at location X:', c, 'Y:',r
                markRegion(self.imgcopy, r, c, self.subimglength, self.subimgheight)
                print 'Number of iterations', itr
                break
            else:
                #x_vel = random.randrange(self.cols)
                #y_vel = random.randrange(self.rows)
                self.moveBat(x_vel, y_vel)
        return [should_display, self.imgcopy]

    def moveBat(self, x_vel, y_vel):
        self.location['x'] = (self.location['x'] + x_vel) % self.rows
        self.location['y'] = (self.location['y'] + y_vel) % self.cols
        print self.location
