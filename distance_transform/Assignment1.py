from PIL import Image

# DISTANCE TRANSFORM ALGORITHM
def city_block(img):
    image = Image.open(img)
    image_copy = image.copy()
    image_copy = image_copy.convert("L")
    width, height = image_copy.size

    # Step one. Change 0's to infinity and 255 to 0.
    for i in range (0, width):
        for j in range (0, height):
            pixel_value = image_copy.getpixel((i, j))
            if(pixel_value == 255):
                image_copy.putpixel((i,j), 0)
            else:
                image_copy.putpixel((i,j), 255)
    
    #First pass
    distance_array = [0,0,0,0]
    for i in range(1, width):
        for j in range(1, height-1):
            center_pixel_value = image_copy.getpixel((i,j))
            distance_array[0] = image_copy.getpixel((i-1, j-1)) + 2
            distance_array[1] = image_copy.getpixel((i, j-1)) + 1
            distance_array[2] = image_copy.getpixel((i-1, j)) + 1
            distance_array[3] = image_copy.getpixel((i-1,j+1)) + 2
            selected_value = min(min(distance_array), center_pixel_value)
            image_copy.putpixel((i,j), selected_value)

    image_copy.show()
    image_copy_first_pass = image_copy.copy()
    for i in range(width-2,-1, -1):
        for j in range(height-2, 0, -1):
            center_pixel_value = image_copy_first_pass.getpixel((i,j))
            distance_array[0] = image_copy_first_pass.getpixel((i+1, j+1)) + 2
            distance_array[1] = image_copy_first_pass.getpixel((i, j+1)) + 1
            distance_array[2] = image_copy_first_pass.getpixel((i+1, j)) + 1
            distance_array[3] = image_copy_first_pass.getpixel((i+1,j-1)) + 2
            selected_value = min(min(distance_array), center_pixel_value)
            image_copy_first_pass.putpixel((i,j), selected_value)

    image_copy_first_pass.show()
    return image_copy_first_pass

def AverageFilter(image):
    
    img_gray = cv2.imread(image, cv2.IMREAD_GRAYSCALE)
    height,width = img_gray.shape

    outputimg = img_gray.copy()
    filterx = np.ones([2, 2], dtype = int)

    for i in range(1,height,2):
            for j in range (1,width,2):
                numberavg=(outputimg[i,j]*filterx[0,1]+(outputimg[i-1,j-1]*filterx[0,1])+(outputimg[i-1,j]*filterx[1,0])+(outputimg[i,j-1]*filterx[1,1]))
                numberavg=numberavg//4
                outputimg[i,j]=numberavg
                outputimg[i,j-1]=numberavg
                outputimg[i-1,j]=numberavg
                outputimg[i-1,j-1]=numberavg

    cv2.imshow('image', outputimg)

    cv2.waitKey(0)
    cv2.destroyAllWindows()  

#AverageFilter('grayscaleImage.bmp')

#city_block("Dolphin.bmp")