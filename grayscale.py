from PIL import Image
import sys

def readImg(img):
    image = Image.open(img)
    image = image.convert('RGB')
    width, height = image.size
    newImage = Image.new('RGB', (width, height))
    newImagePixels = newImage.load()
    
    for y in range(height):
        for x in range(width):
            r, g, b = image.getpixel((x, y))
            if r == b and g == b and b <= 40:
                newImagePixels[x, y] = (0, 0, 0)
            else:
                newImagePixels[x, y] = (255, 255, 255)

    newImage.save(img[:-4] + "_resolve.png")
    del image

imgPath = sys.argv[1]
readImg(imgPath)
