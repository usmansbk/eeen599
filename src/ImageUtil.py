def markRegion(img, row, col, length, height):
    '''Mark a region in an image with yellow boundary'''
    drawHLine(img, row, col, length)
    drawHLine(img, row+height-1, col, length)
    drawVLine(img, row, col, height-1)
    drawVLine(img, row, col+length-1, height-1)

def drawHLine(img, row, col, length):
    '''Draw horizontal line'''
    for c in range(length):
        colorYellow(img[row][col+c])

def drawVLine(img, row, col, height):
    '''Draw vertical line'''
    for r in range(height+1):
        colorYellow(img[row+r][col])

def colorYellow(pixel):
    '''Change a pixel color to yellow'''
    pixel[0] = 255
    pixel[1] = 255
    pixel[2] = 0

def embedImage(src, dest):
    # embedd src image in destination image
    pass

def getregion(img, row, col, length, height, imgHeight, imglength):
    region = []
    for r in range(height):
        if (row+r <= imgHeight and col+length <= imglength):
            region.append(img[row+r][col:col+length])
    return region
