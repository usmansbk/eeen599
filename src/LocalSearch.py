# Copyright 2017 Babakolo Usman Suleiman
# This program is distributed under the terms of the GNU
# General Public License (GPL).

'''
A local image search algorithm implemented using
BAT algorithm and local random walk
'''
from ImageModel import ImageModel
import copy

class LocalSearch:
    def __init__(self, img, subimg):
        self.img = img
        self.subimg = subimg

    def search(self, algo):
        algo.setImage(self.img)
        algo.setTemplate(self.subimg)
        algo.computeFitness()
        result = algo.search() # returns a list [boolean(hit), Image]
        found = result[0]
        if found:
            img = result[1]
            model = ImageModel()
            model.display(img)
        else:
            print 'Template image not found'
        return found
