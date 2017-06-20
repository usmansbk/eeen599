"""
App entry point
"""
import sys
sys.path.insert(0, 'src')
from ImageModel import ImageModel
#from TestAlgo import *
from ImageUtil import *
from ImageStat import *
import matplotlib.pyplot as plt
import copy


img = 'img/img.jpg'
#subimg = 'img/demo3.jpg'
iarr = ImageModel(img).getMatrix()
imgModel = ImageModel(img)
imgdemo = copy.deepcopy(iarr)
markRegion(imgdemo,15, 40, 50, 50)
imgModel.display(imgdemo)
