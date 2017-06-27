from ImageStat import *
from ImageUtil import *
from ImageModel import ImageModel
import copy

class Test:
    def __init__(self, img, subimg):
        self.img = img
        self.subimg = subimg
        self.subgray = asGrayScale(subimg)
        self.gray = asGrayScale(img)
        self.imgcopy = copy.deepcopy(self.img)
        self.config()

    def config(self):
        self.mean = get_mean(self.subgray)
        self.stddev = stddeviation(self.subgray)
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
                #print 'Location X:', c, 'Y:', r
                region = getregion(self.gray, r, c, self.subimglength,
                                    self.subimgheight, self.imgHeight,
                                    self.imglength)
                found = self.analyze(region)
                if (found):
                    should_display = True
                    print 'Found at location X:', c, 'Y:',r
                    markRegion(self.imgcopy, r, c, self.subimglength, self.subimgheight)
                #print '\n'

        model = ImageModel()
        if should_display:
            model.display(self.imgcopy)
        else:
            print 'Image not found!'
            model.display(self.gray)

    def analyze(self, region):
        mean = get_mean(region)
        stddev = stddeviation(region)
        print 'mean of region is ', mean
        print 'mean of image is ', self.mean
        print 'standard deviation of region is ', stddev
        print 'standard deviation of image is ', self.stddev
        mean_diff = abs(mean - self.mean)
        std_diff = abs(stddev - self.stddev)
        if ( (mean_diff >= -2 and mean_diff <= 2) and
             (std_diff >= -2 and std_diff <= 2) ):
            return True
        else:
            return False
