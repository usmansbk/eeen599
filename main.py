"""
App entry point
"""
import sys
sys.path.insert(0, 'src')
from ImageModel import ImageModel

path = 'img/dot.png'
demo = ImageModel(path)
#temp = demo.asGrayScale()
#temp.display()
demo.display()
