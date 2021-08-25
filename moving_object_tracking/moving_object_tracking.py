import cv2
import numpy as np
import math
from PIL import Image as im

video = cv2.VideoCapture("rouen_video.avi")

meanFG = 60 
sdFG = 3
varFG = sdFG ** 2

meanBG = 200
sdBG = 2
varBG = sdBG ** 2

wFG = 0.5
wBG = 0.5

t = 100
alpha = 1 / (t + 0.0000001)

fps = int(video.get(cv2.CAP_PROP_FPS))

fourcc = cv2.VideoWriter_fourcc(*'XVID')

ret, frame = video.read()
grayscale_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
height, width = grayscale_img.shape
         
output = cv2.VideoWriter('Output_Video.avi',fourcc, 30, (width, height))

gaussian1 = np.zeros((height, width))

wFG_matrix = np.full((height, width), wFG)
wBG_matrix = np.full((height, width), wBG)

varFG_matrix = np.full((height, width), varFG)
varBG_matrix = np.full((height, width), varBG)

meanFG_matrix = np.full((height, width), meanFG)
meanBG_matrix = np.full((height, width), meanBG)

oFG = np.zeros((height, width))
oBG = np.zeros((height, width))
deltaBG = 0
deltaFG = 0

while(video.isOpened()):
    ret, frame = video.read()
    if(ret == True):
        grayscale_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    sdBG = varBG_matrix ** (0.5)
    # Place current pixel value in first Gaussian distribution
    xBG = (1 / ((((2 * np.pi) ** 0.5) * sdBG) + 0.0000001)) * np.exp((-1 / ((2 * sdBG ** 2) + 0.0000001)) * (grayscale_img - meanBG_matrix) ** 2)

    sdFG = varFG_matrix ** (0.5)
    # Place current pixel value in second Gaussian distribution
    xFG = (1 / ((((2 * np.pi) ** 0.5) * sdFG) + 0.0000001)) * np.exp((-1 / ((2 * sdFG ** 2) + 0.0000001)) * (grayscale_img - meanFG_matrix) ** 2)

    rBG = xBG * wBG_matrix
    rFG = xFG * wFG_matrix

    gaussian1[rBG > rFG] = 255
    gaussian1[rBG <= rFG] = 0

    oBG[rBG > rFG] = 1
    oBG[rBG <= rFG] = 0

    oFG[rFG > rBG] = 1
    oFG[rFG <= rBG] = 0

    deltaBG = grayscale_img - meanBG
    deltaFG = grayscale_img - meanFG

    wBG_matrix = wBG_matrix + alpha + (oBG - wBG_matrix)
    meanBG_matrix = meanBG_matrix + ((alpha / (wBG_matrix + 0.0000001)) * (oBG * deltaBG))
    varBG_matrix = varBG_matrix + oBG * ((alpha / (wBG_matrix + 0.0000001)) * ((((oBG * deltaBG) ** 2) - (varBG_matrix))))

    wFG_matrix = wFG_matrix + alpha + (oFG - wFG_matrix)
    meanFG_matrix = meanFG_matrix + ((alpha / (wFG_matrix + 0.0000001)) * (oFG * deltaFG))
    varFG_matrix = varFG_matrix + oFG * ((alpha / (wFG_matrix + 0.0000001)) * ((((oFG * deltaFG) ** 2) - (varFG_matrix))))

    weightBG = wBG_matrix / (wBG_matrix + wFG_matrix)
    weightFG = wFG_matrix / (wBG_matrix + wFG_matrix)

    wBG_matrix = weightBG
    wFG_matrix = weightFG  

    gaussian1 = cv2.imwrite('task2Frame.jpg', gaussian1)
    gaussian1 = cv2.imread('task2Frame.jpg')           
         
    output.write(gaussian1)
    #cv2.imshow("current_frame", gaussian1)

    if (ret == False):
        break
    if (cv2.waitKey(fps) and 0xFF == ord('q')):
        cv2.destroyAllWindows()
        break

video.release()
output.release()
cv2.destroyAllWindows()








