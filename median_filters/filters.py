from PIL import Image
import numpy as np


####################################################################
#### TEST CASE LIKE ASSIGNMENT EXAMPLE ####
a = [[4,0,3,2,1],[0,1,3,2,3],[2,1,4,5,4],[3,3,7,8,9]]
#test
def apply_on_list(list):
    np_a = np.asarray(list)
    weight_median_filter = [1, 3, 1, 3, 5, 3, 1, 3, 1]
    for i in range (1, np_a.shape[0]-1):
        for j in range (1, np_a.shape[1]-1):
            vector = []    
            working_array = np_a[i-1:i+2, j-1:j+2]
            working_array = working_array.flatten()
            for k in range (0,len(working_array)):          
                vector += weight_median_filter[k] * [working_array[k]]
            vector.sort()
            np_a[i,j] = vector[10]
    print(np_a)
    return np_a

#apply_on_list(a)
#### TEST CASE LIKE ASSIGNMENT EXAMPLE ####
####################################################################

# Weighted Median Filter 
def apply_weighted_median_filter(img):   
    image = Image.open(img)
    image_copy = image.copy()
    pic = np.array(image_copy)
    weight_median_filter = [1, 3, 1, 3, 5, 3, 1, 3, 1]
    for i in range (1, pic.shape[0]-1):
        for j in range (1, pic.shape[1]-1):
            vector = []    
            working_array = pic[i-1:i+2, j-1:j+2]
            working_array = working_array.flatten()
            for k in range (0,len(working_array)):          
                vector += weight_median_filter[k] * [working_array[k]]
            vector.sort()
            pic[i,j] = vector[10]
    pic = Image.fromarray(pic)
    pic.show()
    pic.save("BarCodeWeightedMedian.jpg")
    return pic

#apply_weighted_median_filter('BarCode2.jpg')
####################################################################

#Median Filter 
def apply_median_filter(img):   
    image = Image.open(img)
    image_copy = image.copy()
    pic = np.array(image_copy)
    for i in range (1, pic.shape[0]-1):
        for j in range (1, pic.shape[1]-1):
            vector = []    
            working_array = pic[i-1:i+2, j-1:j+2]
            working_array = working_array.flatten()       
            vector = working_array
            vector.sort()
            pic[i,j] = vector[4]
           
    pic = Image.fromarray(pic)
    pic.show()
    pic.save("BarCodeMedian.jpg")
    return pic

apply_median_filter('BarCode2.jpg')


####################################################################
## COMMENT 
## Both outputs are blurry but weighted median blur is better because it takes into consideration 
## the weights of surrounding pixels with maximum weight to pixel in the middle, meanwhile median filter
## is blurrier because it does not account to the weights of the pixels. All are given the same weight.
## Weighted Median is better