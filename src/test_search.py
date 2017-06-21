from ImageStat import *
from ImageUtil import *
import copy

class Test:
    def __init__(self, img, subimg):
        self.img = img
        self.subimg = subimg
        self.config()

    def config(self):
        self.mean = get_mean(self.img)
        self.stddev = stddeviation(self.img)
        self.imglength = len(self.img[0])
        self.imgHeight = len(self.img)
        self.subimglength = len(self.subimg[0])
        self.subimgheight = len(self.subimg)

    def search(self):
        rows = self.imgHeight/self.subimgheight
        cols = self.imglength/self.subimglength
        print 'sub region'
        for row in range(rows):
            for col in range(cols):
                # get region
                r = row * self.subimgheight
                c = col * self.subimglength
                self.getregion(self.img, r, c, self.subimglength, self.subimgheight)
            return
                # compare analysis to saved analysis
                # if matched mark region and log found
                # else log 'not found'

    def getregion(self, img, row, col, length, height):
        region = copy.deepcopy(self.subimg)
        for r in range(height):
            if (row+r < self.imgHeight and col+length < self.imglength):
                print img[row+r][col:col+length]
            return
        #print region
