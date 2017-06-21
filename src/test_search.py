from ImageStat import *
from ImageUtil import *

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
        for row in range(0, rows, self.subimgheight):
            for col in range(0, cols, self.subimglength):
                # get region
                # analyze region
                # compare analysis to saved analysis
                # if matched mark region and log found
                # else log 'not found'
