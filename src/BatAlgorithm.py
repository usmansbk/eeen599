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
        self.data = {'mean': self.mean, 'stddev': self.stddev, 'median': self.median}
        self.setParams()

    def search(self):
        found = False
        should_display = False
        for itr in range(self.iterations):
            r = self.location['x'] * self.subimgheight
            c = self.location['y'] * self.subimglength
            print 'row', r, ',col', c
            region = getregion(self.gray, r, c, self.subimglength,self.subimgheight, self.imgHeight,self.imglength)
            self.cur_mean = get_mean(region)
            self.cur_stddv = stddeviation(region)
            found = fitness(region, self.data)
            if (found):
                should_display = True
                print 'Found at location X:', c, 'Y:',r
                markRegion(self.imgcopy, r, c, self.subimglength, self.subimgheight)
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
        n_fitness = s_fitness = w_fitness = e_fitness = False
        sublen = self.subimglength
        subhigh = self.subimgheight
        imglen = self.imglength
        imghigh = self.imgHeight
        if row > 0:
            north = getregion(self.gray, (row-self.loudness)*subhigh, col*sublen, sublen, subhigh, imghigh, imglen)
            n_fitness = fitness(north, self.data)
        if row < self.rows:
            south = getregion(self.gray, ((row+self.loudness)%self.rows)*subhigh, col*sublen, sublen, subhigh, imghigh, imglen)
            s_fitness = fitness(south, self.data)
        if col < self.cols:
            east = getregion(self.gray, row*subhigh, ((col+self.loudness)%self.cols)*sublen, sublen, subhigh, imghigh, imglen)
            e_fitness = fitness(east, self.data)
        if col > 0:
            west = getregion(self.gray, row*subhigh, (col-self.loudness)*sublen, sublen, subhigh, imghigh, imglen)
            w_fitness = fitness(west, self.data)

        #get best region
        if n_fitness:
            return [True, {'x':-1, 'y':0}]
        elif s_fitness:
            return [True, {'x':1, 'y': 0}]
        elif e_fitness:
            return [True, {'x':0, 'y':1}]
        elif w_fitness:
            return [True, {'x':0, 'y':-1}]
        return [False, {'x':0, 'y':0}]

    def moveBat(self, x_vel, y_vel):
        self.location['x'] = (self.location['x'] + x_vel) % self.rows
        self.location['y'] = (self.location['y'] + y_vel) % self.cols
