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
subimg = 'img/subimg2.jpg'

subModel = ImageModel(subimg)
imgModel = ImageModel(img)

iarr = imgModel.getMatrix()
siarr = subModel.getMatrix()
test = Test(iarr, siarr)
result = test.search()
