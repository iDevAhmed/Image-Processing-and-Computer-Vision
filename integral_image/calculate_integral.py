from PIL import Image
import numpy as np


## greyscale image
def imOpen(img):
    image = Image.open(img)
    image_copy = image.copy()
    width, height = image_copy.size
    image_grayscale = Image.new("L", (width, height), color="black")
    for i in range(0,width):
        for j in range(0,height):
            r, g, b = image_copy.getpixel((i, j))
            gray_pixel = ((0.3 * r) + (0.59 * g) + (0.11 * b))
            image_grayscale.putpixel((i,j), (int)(gray_pixel))

    #image_grayscale.show()
    return image_grayscale


def CalculateIntegral(img):
    image = Image.open(img)
    image_copy = image.copy()
    width, height = image_copy.size
    print(image_copy.size)
    integral_image_s = Image.new("L", (width, height), color="black")
    print(integral_image_s.shape)
    for i in range(width-1):
        for j in range(height-1):
             sum = image_copy.getpixel((i, j)) + image_copy.getpixel((i, j+1))
             integral_image_s.putpixel((i,j), (int)(sum))
             
    return integral_image_s

CalculateIntegral("./L4.jpg")
