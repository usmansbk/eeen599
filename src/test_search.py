from ImageStat import *
from ImageUtil import *
from ImageModel import ImageModel
import copy

class Test:
    def __init__(self, img, subimg):
        self.img = img
        self.subimg = subimg
        self.imgcopy = copy.deepcopy(self.img)
        self.config()

    def config(self):
        self.mean = get_mean(self.subimg)
        self.stddev = stddeviation(self.subimg)
        self.imglength = len(self.img[0])
        self.imgHeight = len(self.img)
        self.subimglength = len(self.subimg[0])
        self.subimgheight = len(self.subimg)

    def search(self):
        rows = self.imgHeight/self.subimgheight
        cols = self.imglength/self.subimglength
        r = 0
        c = 0
        found = False
        should_display = False
        for row in range(rows):
            for col in range(cols):
                r = row * self.subimgheight
                c = col * self.subimglength
                print 'row', r, 'col', c
                region = getregion(self.img, r, c, self.subimglength,
                                    self.subimgheight, self.imgHeight,
                                    self.imglength)
                found = self.analyze(region)
                if (found):
                    should_display = True
                    print 'found at location x:', c, ',y:', r
                    markRegion(self.imgcopy, r, c, self.subimglength, self.subimgheight)

        if should_display:
            model = ImageModel()
            model.display(self.imgcopy)
        else:
            print 'Image not found!'

    def analyze(self, region):
        mean = get_mean(region)
        stddev = stddeviation(region)
        print 'mean of region is ', mean
        print 'mean of image is ', self.mean
        print 'standard deviation of region is ', stddev
        print 'standard deviation of image is ', self.stddev

        if ( mean/self.mean >= 1 and stddev/self.stddev >= 1):
            return True
        else:
            return False
