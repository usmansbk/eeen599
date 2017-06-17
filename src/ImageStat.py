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
    meansqr = get_meansqr(img, mean)
    print mean, meansqr

def get_meansqr(img, mean):
    '''calculate mean square value'''
    result = 0
    count = 0
    for row in img:
        for pixel in row:
            for dot in pixel:
                result += (dot - mean)**2
                count += 1
    variance = result / count
    return math.sqrt(variance)

def det(img):
    '''calculate the determinant of the matrix'''
