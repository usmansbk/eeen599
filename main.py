"""
App entry point
"""
import sys
sys.path.insert(0, 'src')
from ImageModel import ImageModel
from ImageUtil import *
import matplotlib.pyplot as plt
import copy


#path = 'img/dot.png'
#path = 'img/demo3.jpg'
path = 'img/demo2.png'
demo = ImageModel(path)
#temp = demo.asGrayScale()
#temp.display()
img = copy.deepcopy(demo.getMatrix())
markRegion(img, 4, 4, 100, 50)
#demo.display()
plt.imshow(img)
plt.show()
