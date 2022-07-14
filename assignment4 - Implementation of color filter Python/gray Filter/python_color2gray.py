import cv2
import timeit

def color2gray_Python_Imp(imageName):
    """This function is a pure python implementation of grayscale a image in order of
    blue green and red (BGR). Weigth for blue 0.07, green 0.72, red 0.21. That is applied to each
    pixel of the image. The function will save a grayscale image under the name, greyscale_python_imageName.

    Args: String, a file name to the image

    Returns: a 3D numpy array (represent a gray image)
    """
    #Open the image and turn it ta a 3D array
    image = cv2.imread(imageName)

    #The first for-loop get every rows in the image 3d array
    #The second for-loop get every columns in the iamge 3d array
    #The third for-loop get every channels in the image 3d array
    #c=0 is blue, c=1 is green, c=2 is red

    for heigth_i in range(len(image)):
        for width_i in range(len(image[heigth_i])):
            greyScale = 0
            for c in range(3):
                #Check which channel current are, and the apply the correct weigth on it
                #Sum up the grayscale and set the pixel we current are
                if c == 0:
                    greyScale += image[heigth_i][width_i][c]*0.07
                elif c == 1:
                    greyScale += image[heigth_i][width_i][c]*0.72
                else:
                    greyScale += image[heigth_i][width_i][c]*0.21

            image[heigth_i][width_i] = (greyScale,greyScale,greyScale)
    #save the image that is grey
    cv2.imwrite("greyscale_python_"+imageName,image)

    return image

n = 3
#The start time
startTime = timeit.default_timer()
for i in range(n):
    color2gray_Python_Imp("rain.jpg")
#The stop time
stopTime = timeit.default_timer()
print("RunTime(Total): " + str(stopTime-startTime))
print("RunTime(Per run): " + str((stopTime-startTime)/n))
