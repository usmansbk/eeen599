# Copyright 2017 Babakolo Usman Suleiman
# This program is distributed under the terms of the GNU
# General Public License (GPL).

import math

def get_mean(img):
    '''Get the mean of the image pixels'''
    count = 0
    total = 0
    for row in img:
        for pixel in row:
            for dot in pixel:
                total += dot
                count += 1
    return total / count

def stddeviation(img):
    '''get the standard deviation'''
    mean = get_mean(img)
    result = 0
    count = 0
    for row in img:
        for pixel in row:
            for dot in pixel:
                result += (dot - mean)**2
                count += 1
    variance = result / count
    return math.sqrt(variance)

def mode(img):
    '''get the mode'''
    pass

def fitness(region, data):
    mean = get_mean(region)
    stddev = stddeviation(region)
    print 'mean of region is ', mean
    print 'mean of image is ', data['mean']
    print 'standard deviation of region is ', stddev
    print 'standard deviation of image is ', data['stddev']
    mean_diff = abs(mean - data['mean'])
    std_diff = abs(stddev - data['stddev'])
    if ( (mean_diff >= -2 and mean_diff <= 2) and
         (std_diff >= -2 and std_diff <= 2) ):
        return True
    else:
        return False
