from numba import jit
import cv2
import timeit
#Because the numba cannot compiling imread()
#So I took out the path of bottelneck of my code as a function that
#have the tag jit on, so that path run with numba
@jit(nopython=True)
def adding(image):
    """Turn a color image to a grey image, and using numba to speed up the process.

    Args: a 3D numpy array

    Returns: a 3D numpy array (represent a gray image)

    """
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
    return image

def color2gray_numba_Imp(imageName):
    """This is a pure python implementation of grayscale a image, but with numba that speed
    up the process. Instead of running loops with python, all the loops runs with numba.

    Args: String, a file name to the image

    Returns: a 3D numpy array (represent a gray image)

    """
    #Open the image and turn it ta a 3D array
    image = cv2.imread(imageName)

    #apply weigth on each channel
    greyImage = adding(image)
    #Save the greyScale image
    cv2.imwrite("greyscale_numba_"+imageName,greyImage)
    return greyImage

n = 3
#The start time
startTime = timeit.default_timer()
for i in range(n):
    color2gray_numba_Imp("rain.jpg")
#The stop time
stopTime = timeit.default_timer()
print("RunTime(Total): " + str(stopTime-startTime))
print("RunTime(Per run): " + str((stopTime-startTime)/n))
