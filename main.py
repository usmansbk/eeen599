"""
App entry point
"""
import sys
sys.path.insert(0, 'src')
from ImageModel import ImageModel

path = 'img/demo.jpg'
dummy = ImageModel(path)
temp = dummy.asGrayScale()
temp.display()
