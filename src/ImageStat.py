# Copyright 2017 Babakolo Usman Suleiman
# This program is distributed under the terms of the GNU
# General Public License (GPL).

import math

upper_threshold = 0.4
lower_threshold = 1

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

def get_sum(img):
    result = 0
    for row in img:
        for pixel in row:
            for dot in pixel:
                result += dot
    return result

def get_median(img):
    lst = []
    for row in img:
        for pixel in row:
            for dot in pixel:
                lst.append(dot)
    lst = sorted(lst)
    n = len(lst)
    is_odd = n % 2 == 1
    index = None
    if is_odd:
        mid = (n + 1)/2
        return lst[mid]
    else:
        mid = n / 2
        return (lst[mid] + lst[mid+1]) / 2

def fitness(region, data):
    mean = get_mean(region)
    stddev = stddeviation(region)
    median = get_median(region)
    mean_diff = abs(mean - data['mean'])
    std_diff = abs(stddev - data['stddev'])
    median_diff = (median == data['median'])
    found = False
    if (  mean_diff <=lower_threshold and std_diff <= upper_threshold and median_diff):
        found = True
    return found
