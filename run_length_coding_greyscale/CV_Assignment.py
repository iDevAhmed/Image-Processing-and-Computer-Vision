from PIL import Image

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

imOpen("BarCode2.jpg")

#Input, gray scaled image
def toStrH(img):
    image_copy = img.copy()
    width, height = image_copy.size
    rle_h = "H " + str(width) + " " + str(height)
    i = 0
    j = 0 
    count = 1
    while(i<height-1):
     rle_h += "\n"
     while (j<width-1):
         currentPix = image_copy.getpixel((j,i))
         nextPix = image_copy.getpixel((j+1,i))
         start = j
         count = 1
         while(currentPix == nextPix and j<width-2):
             count+=1
             j+=1
             nextPix = image_copy.getpixel((j+1,i))
         rle_h += " " + str(currentPix) + " " + str(start) + " " + str(count + start - 1) 
         j+=1
     j=0 
     start = j
     i+=1 
    return (rle_h)


def transpose(img):
    image_copy = img.copy()
    width, height = image_copy.size
    transpose_img = Image.new("L", (height, width), color="black")
    for i in range(width):
        for j in range (height):
            pixel = image_copy.getpixel((i,j))
            transpose_img.putpixel((j,i), (int)(pixel))
    return transpose_img
def toStrV(img):
    image_copy = img.copy()
    image_copy = transpose(image_copy)
    width, height = image_copy.size
    rle_v = "V " + str(width) + " " + str(height)
    i = 0
    j = 0 
    count = 1
    while(i<=height-1):
     rle_v += "\n"
     while (j<=width-1):
         currentPix = image_copy.getpixel((j,i))
         nextPix = image_copy.getpixel((j+1,i))
         start = j
         count = 1
         while(currentPix == nextPix and j<=width):
             count+=1
             j+=1
             nextPix = image_copy.getpixel((j+1,i))
         rle_v += str(currentPix) + " " + str(start) + " " + str(count + start - 1) + " "
         j+=1
     j=0 
     start = j
     i+=1
     
    return (rle_v)

def toFile(txt,txt2):
    txtout = open(txt+".txt","w")
    txtout.write(txt2)
    txtout.close()


def toImg(txt):
    with open(txt,"r") as f:
     string = f.readlines()
     string2 = f.read()

    print(len(string))
    rle = string[0].split()
    width = int(rle[1])
    height = int(rle[2])
    if(rle[0] == "H"):
         new_image = Image.new("L", (int(height), int(width)), color="black")
         i = 0
         j = 1
         currentPixel = 0
         lastIndex = 0
         startIndex = 0

         while (i<width):
          while(j<height):
            rle = string[j].split()
            row = 0
            for k in range(0,len(rle)):       
             count = 0
             if (k%3==0):
              currentPixel = int(rle[k])
             if (k%3==1):
              startIndex = int(rle[k])
             if(k%3==2):                  
               lastIndex = int(rle[k])
               repetitions = (lastIndex - startIndex) + 1
               while (count<repetitions):   
                 new_image.putpixel((i,row), int(currentPixel))
                 row+=1
                 count+=1        
            j+=1
          j=1
          i+=1

    if(rle[0] == "V"):
         new_image = Image.new("L", (int(height), int(width)), color="black")
         i = 0
         j = 1
         currentPixel = 0
         lastIndex = 0
         startIndex = 0

         while (i<height):
          while(j<width):
            rle = string[j].split()
            row = 0
            for k in range(0,len(rle)):       
             count = 0
             if (k%3==0):
              currentPixel = int(rle[k])
             if (k%3==1):
              startIndex = int(rle[k])
             if(k%3==2):                  
               lastIndex = int(rle[k])
               repetitions = (lastIndex - startIndex) + 1
               while (count<repetitions):   
                 new_image.putpixel((i,row), int(currentPixel))
                 row+=1
                 count+=1        
            j+=1
          j=1
          i+=1
    new_image.show()

    return new_image

def toImg2(txt):
    with open(txt,"r") as f:
     string = f.read()

    print(len(string))
    rle = string.split()
    width = int(rle[1])
    height = int(rle[2])
    if(rle[0] == "H"):
         print("here")
         new_image = Image.new("L", (int(width), int(height)), color="black")
         i = 0
         j = 1
         currentPixel = 0
         print(width)
         lastIndex = 0
         startIndex = 0
         while (i<width):
          row = 0             
          while(j<height):
             count = 0
             if (j%3==0):
              currentPixel = int(rle[j])
             if (j%3==1):
              startIndex = int(rle[j])
             if(j%3==2):                  
               lastIndex = int(rle[j])
               repetitions = (lastIndex - startIndex) + 1
               while (count<repetitions and row<height-1):   
                 new_image.putpixel((i,row), int(currentPixel))
                 count+=1
                 row+=1
             j+=1
          j=3
          i+=1
    if(rle[0] == "V"):
         new_image = Image.new("L", (int(height), int(width)), color="black")
         i = 0
         j = 3
         count = 0
         currentPixel = 0
         lastIndex = 0
         startIndex = 0
         while (i<height):
          row = 0                               
          while(j<width):
             count = 0
             if (j%3==0):
              currentPixel = int(rle[j])
             if (j%3==1):
              startIndex = int(rle[j])
             if(j%3==2):                  
               lastIndex = int(rle[j])
               repetitions = (lastIndex - startIndex) + 1
               while (count<repetitions and row<height):   
                 new_image.putpixel((i,row), int(currentPixel))                
                 count+=1
                 row+=1          
             j+=1
          j=3
          i+=1
    new_image.show()

    return new_image

         