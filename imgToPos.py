from PIL import Image
import sys

def readImg(img):
    image = Image.open(img)
    image = image.convert('RGB')
    width, height = image.size
    firstW = 0
    firstH = 0
    firstFlag = True

    for y in range(height):
        for x in range(width):
            r, g, b = image.getpixel((x, y))
            if r == 0 and g == 0 and b == 0:
                if firstFlag == True:
                    firstW = x
                    firstH = y
                    firstFlag = False
                print('(%3d,%3d)' % (x - firstW, y - firstH))

    del image

imgPath = sys.argv[1]
readImg(imgPath)
