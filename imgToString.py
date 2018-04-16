from PIL import Image
import os
import struct

positionDataPath = './position'

def imgToString(image):
    filelist = []
    image = image.convert('RGB')
    convertList = []

    (width, height) = image.size
    # print('(w, h) = (%d, %d)' % (width, height))

    for filename in os.listdir(positionDataPath):
        filelist.append(filename)

    for filename in filelist:
        point = []
        fullFilePath = positionDataPath + '/' + filename
        openFile = open(fullFilePath, 'r')
        (maxX, maxY) = (0, 0)
        (minX, minY) = (0, 0)

        for line in openFile:
            (x, y) = struct.unpack('1x3s1x3s2x', line)
            (x, y) = (int(x), int(y))
            if x > maxX:
                maxX = x
            if y > maxY:
                maxY = y
            if x < minX:
                minX = x
            if y < minY:
                minY = y
            point.append((x, y))    

        for y in range(0 - minY, height - maxY):
            for x in range(0 - minX, width - maxX):
                # print('(x, y) = (%d, %d)' % (x, y))
                flag = True
                for (pX, pY) in point:
                    # print('(x + pX, y + pY) = (%d, %d)' % (x + pX, y + pY))
                    (r, g, b) = image.getpixel((x + pX, y + pY))
                    if (r, g, b) == (255, 255, 255):
                    #     if (x, y) == (114, 14) and filename == 'a.pos':
                    #         print('(pX, pY) = (%d, %d)' % (pX, pY))
                    #         print('(x + pX, y + pY) = (%d, %d)' % (x + pX, y + pY))
                        flag = False
                        break
                    # else:
                    #     if filename == 'g.pos':
                    #         print('(pX, pY) = (%d, %d)' % (pX, pY))
                    #         print('(x + pX, y + pY) = (%d, %d)' % (x + pX, y + pY))
                if flag == True:
                    convertList.append((x, filename[:-4].upper()))

    convertList.sort(key = lambda x : int(x[0]))
    (oldpX, oldChar) = convertList[0]
    for index, (pX, char) in enumerate(convertList[1:]):
        if abs(pX - oldpX) <= 3:
            if char == oldChar:
                del convertList[index]
            elif oldChar == 'L' and char == 'B':
                convertList.remove((oldpX, oldChar))
                oldpX = pX
                oldChar = char
            elif oldChar == 'B' and char == 'P':
                convertList.remove((pX, char))
            elif oldChar == 'P' and char == 'R':
                convertList.remove((oldpX, oldChar))
                oldpX = pX
                oldChar = char
            elif oldChar == 'R' and char == 'F':
                convertList.remove((pX, char))
        else:
            oldpX = pX
            oldChar = char
    result = ''
    for (index, char) in convertList:
        result += char
    # print(convertList)
    return result

for filename in os.listdir('./img/nonResolve'):
    image = Image.open('./img/nonResolve/' + filename)
    print('(file, resolve) = (%s, %s)' % (filename, imgToString(image)))

# image = Image.open('./img/nonResolve/883FGY.png')
# print('(file, resolve) = (%s, %s)' % ('883FGY', imgToString(image)))
