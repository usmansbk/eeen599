"""
App entry point
"""
import sys
sys.path.insert(0, 'src')
from ImageModel import ImageModel

path = 'img/demo.jpg'
demo = ImageModel(path)
temp = demo.asGrayScale()
temp.display()
