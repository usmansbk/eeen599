"""
App entry point
"""
import sys
sys.path.insert(0, 'bin')
from ImageModel import ImageModel
from ImageUtil import *
from ImageStat import *
from LocalSearch import LocalSearch
from TestAlgorithm import TestAlgorithm
import matplotlib.pyplot as plt
import copy

### Handle commandline arguments
imgpath = 'img/'
img = imgpath + sys.argv[1]
subimg = imgpath + sys.argv[2]

### Create Image Model Objects
subModel = ImageModel(subimg)
imgModel = ImageModel(img)

### Convert Image to Matrix
iarr = imgModel.getMatrix()
siarr = subModel.getMatrix()

### Instantiate a LocalSearch Object
local = LocalSearch(iarr, siarr)

### Instantiate Algorithm
test_algo = TestAlgorithm()

### Pass Algorithm to local search function
local.search(test_algo)
