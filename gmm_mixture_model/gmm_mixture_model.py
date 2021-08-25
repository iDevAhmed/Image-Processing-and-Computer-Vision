import cv2
import numpy as np

def getHeight(video):
    videoFrames = cv2.VideoCapture(video)
    height = 0
    if (videoFrames.isOpened()):
       height = videoFrames.get(4)
    return height

def getWidth(video):
    videoFrames = cv2.VideoCapture(video)
    width = 0 
    if (videoFrames.isOpened()):
       width = videoFrames.get(3)
    return width

def getFPS(video):
    videoFrames = cv2.VideoCapture(video)
    fps = 0
    if (videoFrames.isOpened()):
       fps = videoFrames.get(5)
    return fps


def Task1():
    #open video file
    videoFrames = cv2.VideoCapture('rouen_video.avi')

    #get video dimensions
    frame_width = getWidth('rouen_video.avi')
    frame_height = getHeight('rouen_video.avi')
    fourcc = cv2.VideoWriter_fourcc(*'XVID')

    #create new video stream
    out = cv2.VideoWriter('output2.avi', fourcc, getFPS('rouen_video.avi'), (int(frame_width),int(frame_height)))

    i = False
    ret, frame = videoFrames.read()
    #img = cv2.imwrite('Frame1.jpg', frame)
    frame1_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame1_gray = cv2.imwrite('Frame1.jpg', frame1_gray)

    y = False
    while True:
            ret, frame = videoFrames.read()
            if ret == False:
                break    
            # flag y is true after subtracting 2nd frame from 1st frame, then loop continues normally
            # subtracting frame i and i+1
            if(y==True):
             img1 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
             img1 = cv2.imwrite('Framei.jpg', img1)
             img1 = cv2.imread(r'C:\Users\amjad\OneDrive\Documents\Advaned Video Processing\AdvancedVideoProcessing\Assignment_1\Framei.jpg')
             new_image = cv2.subtract(img1, img2)
             out.write(new_image)
             img2 = img1
          
             # subtracting frame 2 - frame 1           
            if(y==False):
             #cv2.imwrite('Framei.jpg', frame)
             img2 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
             img2 = cv2.imwrite('Framei.jpg', frame)
             img2 = cv2.imread(r'C:\Users\amjad\OneDrive\Documents\Advaned Video Processing\AdvancedVideoProcessing\Assignment_1\Frame1.jpg')           
             new_image = cv2.subtract(frame1_gray, img2)
             out.write(new_image)
             y = True


    videoFrames.release()
    out.release()
    cv2.destroyAllWindows

#Task1()


def Task2():
    import cv2

    videoFrames = cv2.VideoCapture('rouen_video.avi')
    frame_width = getWidth('rouen_video.avi')
    frame_height = getHeight('rouen_video.avi')
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output3.avi', fourcc, getFPS('rouen_video.avi'), (int(frame_width),int(frame_height)))

    i = 1
    ret, frame = videoFrames.read()
    avgValue = np.float32(frame)

    while True:
          ret, frame = videoFrames.read()
          if ret == False:
               break  
          cv2.accumulateWeighted(frame, avgValue, 0.05)          
          new_frame = cv2.convertScaleAbs(avgValue)
          new_frame_gray = cv2.cvtColor(new_frame, cv2.COLOR_BGR2GRAY)
          new_frame_gray = cv2.imwrite('task2Frame.jpg', new_frame_gray)
          new_frame_gray = cv2.imread(r'C:\Users\amjad\OneDrive\Documents\Advaned Video Processing\AdvancedVideoProcessing\Assignment_1\task2Frame.jpg')              
          out.write(new_frame_gray)

    videoFrames.release()
    out.release()
    cv2.destroyAllWindows
    

#Task2()

import math
def stdev(data):
    var = variance(data)
    std_dev = math.sqrt(var)
    return std_dev

def variance(data, ddof=0):
    n = len(data)
    mean = sum(data) / n
    return sum((x - mean) ** 2 for x in data) / (n - ddof)

def Task3():
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

    img = cv2.imread(r'C:\Users\amjad\OneDrive\Documents\Advaned Video Processing\AdvancedVideoProcessing\Assignment_1\original.jpg');
    grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    height , width  = grey_img.shape[:2]

    array_d1 = []
    array_d2 = []
    blank_image_r1 = np.zeros((height,width,3), dtype = np.uint8)
    blank_image_2 = np.zeros((height,width,3), dtype = np.uint8)


    while( (abs(mFR - sub_1) > 0.3)  and (abs(mBR - sub_2) > 0.1) and (abs(sd_FR - sub_1_sd) > 0.1) and (abs(sd_BR - sub_2_sd)) > 0.1):
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
    
     r1_mean = sum(array_d1)/len(array_d1)
     r2_mean = sum(array_d2)/len(array_d2)
   
     r1_st_dev = stdev(array_d1)
     r2_st_dev = stdev(array_d2)

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

#Task3()
