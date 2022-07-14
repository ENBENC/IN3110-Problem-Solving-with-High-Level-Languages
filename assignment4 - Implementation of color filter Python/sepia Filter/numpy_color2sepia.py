import cv2
import timeit
import numpy as np
def color2sepia_numpy_Imp(imageName):
    """This function is a numpy implementation of sepia image with a color_matrix in order of
    red, grenn and blue (RGB). Weigth for red [0.393, 0.769, 0.189], green [0.349, 0.686, 0.168],
    blue [0.272, 0.534, 0.131].
    The function will save a sepia image under the name, sepia_numpy_imageName.
    Instead of working with the pixels one by one, here comput with vector operations.

    Args: String, a file name to the image

    Returns: a 3D numpy array (represent a sepia image)
    """
    #Open the image and turn it to a 3D array
    image = cv2.imread(imageName)
    #This is sepia matrix that give us the sepia color to the image
    color_matrix = [[ 0.393 , 0.769 , 0.189], #for red
                    [ 0.349 , 0.686 , 0.168], #for green
                    [ 0.272 , 0.534 , 0.131]] #for blue
    #get channels
    r_c = image[:,:,2]
    g_c = image[:,:,1]
    b_c = image[:,:,0]
    #apply weigth on each channel
    red = r_c*color_matrix[0][0] + g_c*color_matrix[0][1] + b_c*color_matrix[0][2]
    green = r_c*color_matrix[1][0] + g_c*color_matrix[1][1] + b_c*color_matrix[1][2]
    blue = r_c*color_matrix[2][0] + g_c*color_matrix[2][1] + b_c*color_matrix[2][2]

    #set the new channel and for each pixel the size cannot be over 255
    image[:,:,2] = np.minimum(255,red)
    image[:,:,1] = np.minimum(255,green)
    image[:,:,0] = np.minimum(255,blue)
    #save the image that is sepia
    cv2.imwrite("sepia_numpy_"+imageName,image)
    return image

n = 3
#The start time
startTime = timeit.default_timer()
for i in range(n):
    color2sepia_numpy_Imp("rain.jpg")
#The stop time
stopTime = timeit.default_timer()
print("RunTime(Total): " + str(stopTime-startTime))
print("RunTime(Per run): " + str((stopTime-startTime)/n))
