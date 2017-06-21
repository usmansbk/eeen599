"""
App entry point
"""
import sys
sys.path.insert(0, 'src')
from ImageModel import ImageModel
#from TestAlgo import *
from ImageUtil import *
from ImageStat import *
from test_search import Test
import matplotlib.pyplot as plt
import copy


img = 'img/img.jpg'
subimg = 'img/subimg.jpg'

subModel = ImageModel(subimg)
imgModel = ImageModel(img)

iarr = imgModel.getMatrix()
siarr = subModel.getMatrix()

imgdemo = copy.deepcopy(iarr)

#markRegion(imgdemo,15, 40, 50, 50)
#imgModel.display(imgdemo)
test = Test(iarr, siarr)
test.search()
#imgdemo.display()
