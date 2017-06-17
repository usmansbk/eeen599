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

def twobytwo(matrix):
    a = matrix[0][0]
    b = matrix[0][1]
    c = matrix[1][0]
    d = matrix[1][1]
    A = (a * d) - (b * c)
    return A

def threebythree(matrix):
    a = matrix[0][0]
    b = matrix[0][1]
    c = matrix[0][2]
    matA = [
            matrix[1][1:],
            matrix[2][1:]
            ]
    matB = [
            [matrix[1][0], matrix[1][2]],
            [matrix[2][0], matrix[2][2]]
            ]
    matC = [
            matrix[1][:-1],
            matrix[2][:-1]
            ]
    A = a * twobytwo(matA) - b * twobytwo(matB) + c * twobytwo(matC)
    return A

def det(matrix):
    '''calculates the determinant of a 4*4 matrix'''
    a = matrix[0][0]
    b = matrix[0][1]
    c = matrix[0][2]
    d = matrix[0][3]
    matA = [
            matrix[1][1:],
            matrix[2][1:],
            matrix[3][1:]
            ]
    matB = [
            [matrix[1][0], matrix[1][2], matrix[1][3]],
            [matrix[2][0], matrix[2][2], matrix[2][3]],
            [matrix[3][0], matrix[3][2], matrix[3][3]]
            ]
    matC = [
            [matrix[1][0], matrix[1][1], matrix[1][3]],
            [matrix[2][0], matrix[2][1], matrix[2][3]],
            [matrix[3][0], matrix[3][1], matrix[3][3]]
            ]
    matD = [
            matrix[1][:-1],
            matrix[2][:-1],
            matrix[3][:-1]
            ]
    A = a * threebythree(matA)-b * threebythree(matB)+c * threebythree(matC)-d * threebythree(matD)
    return A
