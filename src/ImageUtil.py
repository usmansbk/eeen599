def markRegion(img, row, col, length, height):
    '''Mark a region in an image with yellow boundary'''
    drawHLine(img, row, col, length)
    drawHLine(img, row+height, col, length)
    drawVLine(img, row, col, height)
    drawVLine(img, row, col+length, height)

def drawHLine(img, row, col, length):
    '''Draw horizontal line'''
    for c in range(length+1):
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
