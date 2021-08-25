import math
def stdev(data):
    var = variance(data)
    std_dev = math.sqrt(var)
    return std_dev

def variance(data, ddof=0):
    n = len(data)
    mean = sum(data) / n
    return sum((x - mean) ** 2 for x in data) / (n - ddof)

def Task3(input):
    import math
    import numpy as np
    import statistics 
    from PIL import Image
    mFR = 230
    mBR = 75
    sd_FR = 12
    sd_BR = 10
    w_fr = 0.5
    w_br = 0.5

    sub_1 = 0.0
    sub_2 = 0.0
    sub_1_sd = 0.0
    sub_2_sd = 0.0

    img = cv2.imread(input)
    grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    height , width  = grey_img.shape[:2]

    array_d1 = []
    array_d2 = []
    blank_image_r1 = np.zeros((height,width,3), dtype = np.uint8)
    blank_image_2 = np.zeros((height,width,3), dtype = np.uint8)


    while( (abs(mFR - sub_1) > 0.3)  and (abs(mBR - sub_2) > 0.3) and (abs(sd_FR - sub_1_sd) > 0.3) and (abs(sd_BR - sub_2_sd)) > 0.3):
     for i in range (0,width):
        for j in range (0,height):
            k = grey_img[i,j]
            d1_FR = 1/ (math.sqrt(2 * math.pi) * sd_FR) * (math.exp(-1/(2 * sd_FR ** 2)) * (k - mFR) ** 2)
            d2_BR = 1/ (math.sqrt(2 * math.pi) * sd_BR) * (math.exp(-1/(2 * sd_BR ** 2)) * (k - mBR) ** 2)
            r1 = d1_FR * w_fr
            r2 = d2_BR * w_br
            if(r1>r2):
                array_d1.append(r1)
                #blank_image_r1[i,j] = 255
            elif(r2>r1):
                array_d2.append(r2)
                #blank_image_2[i,j] = 255
    
     #r1_mean = np.mean(array_d1)
     #r2_mean = np.mean(array_d2)
     #r1_st_dev = statistics.stdev(array_d1)
     #r2_st_dev = statistics.stdev(array_d2)   

     sum_r1 = 0
     sum_r2 = 0
     for i in range(0,len(array_d1)):
        sum_r1 = sum_r1 + array_d1[i]

     for j in range(0,len(array_d2)):
        sum_r2 = sum_r2 + array_d2[j]
    
     r1_mean = stdev(array_d1)
     r2_mean = stdev(array_d2)

     r1_st_dev = (sum_r1 - r1_mean)**2/len(array_d1)
     r2_st_dev = (sum_r2- r2_mean)**2/len(array_d2)

     w_fr = np.size(array_d1) / np.size(grey_img)
     w_br = np.size(array_d2) / np.size(grey_img)
     sub_1 = abs(mFR - r1_mean)
     sub_2 = abs(mBR - r2_mean)
     sub_1_sd = abs(sd_FR - r1_st_dev)
     sub_2_sd = abs(sd_BR - r2_st_dev)

     mFR = sub_1
     mBR = sub_2
     sd_FR = sub_1_sd 
     sd_BR = sub_2_sd

    for i in range (0,width):
        for j in range (0,height):
            k = grey_img[i,j]
            d1_FR = 1/ (math.sqrt(2 * math.pi) * sd_FR) * (math.exp(-1/(2 * sd_FR ** 2)) * (k - mFR) ** 2)
            d2_BR = 1/ (math.sqrt(2 * math.pi) * sd_BR) * (math.exp(-1/(2 * sd_BR ** 2)) * (k - mBR) ** 2)
            r1 = d1_FR * w_fr
            r2 = d2_BR * w_br
            if(r1>r2):
                array_d1.append(r1)
                blank_image_r1[i,j] = 255
            else:
                array_d2.append(r2)
                blank_image_2[i,j] = 255

    cv2.imwrite( 'fr.jpg', blank_image_r1)
    cv2.imwrite( 'br.jpg', blank_image_2)

Task3()