import cv2
import timeit
def color2gray_numpy_Imp(imageName):
    """This function is a numpy implementation of grayscale a image in order of
    blue green and red (BGR). Weigth for blue 0.07, green 0.72, red 0.21. That is applied to each
    pixel of the image. The function will save a grayscale image under the name, greyscale_numpy_imageName.
    Instead of working with the pixels one by one, here comput with vector operations.

    Args: String, a file name to the image

    Returns: a 3D numpy array (represent a gray image)
    """
    #Open the image and turn it to a 3D array
    image = cv2.imread(imageName)


    blue = image[:,:,0:1]
    green = image[:,:,1:2]
    red = image[:,:,2:3]

    #apply weigth on each channel
    image[:,:,:] = blue*0.07 + green*0.72 + red*0.21
    #Save the greyScale image
    cv2.imwrite("greyscale_numpy_"+imageName,image)
    return image
n = 3
#The start time
startTime = timeit.default_timer()
for i in range(n):
    color2gray_numpy_Imp("rain.jpg")
#The stop time
stopTime = timeit.default_timer()
print("RunTime(Total): " + str(stopTime-startTime))
print("RunTime(Per run): " + str((stopTime-startTime)/n))
