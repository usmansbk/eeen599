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
            r = self.location['x'] * self.subimgheight
            c = self.location['y'] * self.subimglength
            print 'row', r, ',col', c
            region = getregion(self.gray, r, c, self.subimglength,self.subimgheight, self.imgHeight,self.imglength)
            data = {'mean': self.mean, 'stddev': self.stddev, 'median': self.median}
            found = fitness(region, data)
            if (found):
                should_display = True
                print 'Found at location X:', c, 'Y:',r
                markRegion(self.imgcopy, r, c, self.subimglength, self.subimgheight)
                print 'Number of iterations', (itr+1)
                break
            else:
                echo = self.emitSonar(self.location['x'], self.location['y'])
                detected = echo[0]
                if detected:
                    new_velocity = echo[1]
                    x_vel = new_velocity['x']
                    y_vel = new_velocity['y']
                else:
                    x_vel = random.randrange(self.cols)
                    y_vel = random.randrange(self.rows)
                self.moveBat(x_vel, y_vel)
        return [should_display, self.imgcopy]

    def emitSonar(self, row, col):
        #get regions
        west = east = north = south = None
        sublen = self.subimglength
        subhigh = self.subimgheight
        imglen = self.imglength
        imghigh = self.imgHeight
        if row > 0:
            north = getregion(self.gray, row-self.loudness, col, sublen, subhigh, imglen, imghigh)
        if row < self.rows:
            south = getregion(self.gray, row+self.loudness, col, sublen, subhigh, imglen, imghigh)
        if col > 0:
            east = getregion(self.gray, row, col-self.loudness, sublen, subhigh, imglen, imghigh)
        if col < self.cols:
            west = getregion(self.gray, row, col+self.loudness, sublen, subhigh, imglen, imghigh)

        #get best solution
        best_solution = self.get_bestregion(north, south, east, west)
        is_detected = best_solution[0]
        location = best_solution[1]

        echo = [is_detected, {'x': location[0], 'y': location[1]}]
        return echo

    def get_bestregion(self, north, south, east, west):
        if north != None:
            north_data = getData(north, 'n')
            print 'North', north_data
        if south != None:
            south_data = getData(south, 's')
            print 'South', south_data
        if east != None:
            east_data = getData(east, 'e')
            print 'East', east_data
        if west != None:
            west_data = getData(west, 'w')
            print 'West', west_data
        return [True, [0, 2]]

    def moveBat(self, x_vel, y_vel):
        self.location['x'] = (self.location['x'] + x_vel) % self.rows
        self.location['y'] = (self.location['y'] + y_vel) % self.cols
