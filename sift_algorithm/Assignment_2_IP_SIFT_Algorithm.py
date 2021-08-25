from PIL import Image
from numpy.core.defchararray import asarray
from numpy.core.fromnumeric import ndim
from scipy import ndimage
import cv2
import numpy as np
from matplotlib import pyplot as plt
import math

def sift(img, s, threshold):
    #Read image, convert to Greyscale
    image = Image.open(img).convert('L')
    #Read as NumpyArray
    np_image = np.array(image)
    #Divide by 255 to normalize image
    np_image = np.divide(np_image, 255.0)
    height, width = image.size
    #Final image
    new_image = np.asarray(image)

    #Keypoins storage array
    keypoints = []
    #counter for blobs
    counter = 0

    #loop from 1 to maximum sigmas
    for i in range(1,s,1):
        #Image 1
        #Apply Laplacian of Gaussian
        laplacian_previous = ndimage.gaussian_laplace(np_image, sigma=i-1)
        #Take Absolute
        laplacian_previous = np.abs(laplacian_previous)
        #Multiply by sigma squared
        laplacian_previous = np.multiply(laplacian_previous, math.pow(i-1,2))  

        #Image 2
        laplacian_current = ndimage.gaussian_laplace(np_image, sigma=i)
        laplacian_current = np.abs(laplacian_current)
        laplacian_current = np.multiply(laplacian_current, math.pow(i,2))

        #Image 3
        laplacian_next = ndimage.gaussian_laplace(np_image, sigma=i+1)
        laplacian_next = np.abs(laplacian_next) 
        laplacian_next = np.multiply(laplacian_next, math.pow(i+1,2))

        #Loop over 3 sigmas and compare pixels
        for x in range(1,width-1):
            for y in range(1,height-1):
                #Current pixel
                current_pixel = laplacian_current[x,y] 
                #Current 3x3 Kernel Filter  
                kernel_current = laplacian_current[x-1:x+2,y-1:y+2]
                #Previous
                kernel_previous = laplacian_previous[x-1:x+2,y-1:y+2]
                #Next
                kernel_next = laplacian_next[x-1:x+2, y-1:y+2]
                #Compare pixel with 26 neighbors
                if(compare_pixel(kernel_current) == True):
                    if(compare_pixel_kernel(current_pixel,kernel_previous) == True and compare_pixel_kernel(current_pixel,kernel_next) == True):
                        #Compare threshold
                        if current_pixel >= threshold:
                            counter+=1
                            keypoints.append((x,y,i))
                            break
                        break
    #Draw Keypoints
    for i in range(len(keypoints)):
        x,y,sigma = keypoints[i]
        new_image = cv2.circle(np_image,(y,x), int(math.sqrt(2) * sigma), (255,0,0), 1)

    print(counter)
    cv2.imshow('Blobs', new_image)
    cv2.waitKey(0)
    return new_image

def compare_pixel(kernel):
    greater = True
    for i in range(3):
        for j in range(3):
            if(i!=1 and j!=1):
                if kernel[1][1] <= kernel[i][j]:
                    greater = False
    return greater

def compare_pixel_kernel(pixel, kernel):
    greater = True
    for i in range(3):
        for j in range(3):
            if(pixel <= kernel[i][j]):
                greater = False
    return greater


#image = Image.open('Giraffe.jpg').convert('L')
#np_image = np.array(image)           
#log_1 = ndimage.gaussian_laplace(np_image, sigma=1)
#log_5 = ndimage.gaussian_laplace(np_image, sigma=5)

#giraffe_1 = Image.fromarray(log_1)
#giraffe_5 = Image.fromarray(log_5)
#giraffe_1.save("Giraffe_1.jpg")
#giraffe_5.save("Giraffe_5.jpg")

#No Threshold
sift('Giraffe.jpg', 20, 0)

#Threshold = 0.01
sift('Giraffe.jpg', 20, 0.01)

#Threshold = 0.02
sift('Giraffe.jpg', 20, 0.02)
