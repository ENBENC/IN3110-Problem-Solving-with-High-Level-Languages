from numba import jit
import cv2
import timeit
#Because the numba cannot compiling imread()
#So I took out the path of bottelneck of my code as a function that
#have the tag jit on, so that path run with numba
@jit(nopython=True)
def adding(image):
    """Turn a color image to a sepia image, and using numba to speed up the process.

    Args: a 3D numpy array

    Returns: a 3D numpy array (represent a sepia image)

    """
    #This is sepia matrix that give us the sepia color to the image
    color_matrix = [[ 0.393 , 0.769 , 0.189], #for red
                    [ 0.349 , 0.686 , 0.168], #for green
                    [ 0.272 , 0.534 , 0.131]] #for blue

    for heigth_i in range(len(image)):
        for width_i in range(len(image[heigth_i])):
            #get each channel
            r_c = image[heigth_i][width_i][2]
            g_c = image[heigth_i][width_i][1]
            b_c = image[heigth_i][width_i][0]
            #applay weigth to each channel
            red = r_c*color_matrix[0][0] + g_c*color_matrix[0][1] + b_c*color_matrix[0][2]
            green = r_c*color_matrix[1][0] + g_c*color_matrix[1][1] + b_c*color_matrix[1][2]
            blue = r_c*color_matrix[2][0] + g_c*color_matrix[2][1] + b_c*color_matrix[2][2]
            # Set the new pixel, and min(255, channel) give 255 if the value of channel is over 255
            image[heigth_i][width_i] = (min(255,blue),min(255,green),min(255,red))
    return image

def color2sepia_numba_Imp(imageName):
    """This is a numba implementation of sepia a image, but with numba that speed
    up the process. Instead of running loops with python, all the loops runs with numba.

    Args: String, a file name to the image

    Returns: a 3D numpy array (represent a sepia image)

    """
    #Open the image and turn it ta a 3D array
    image = cv2.imread(imageName)

    #apply weigth on each channel
    image = adding(image)
    #Save the sepia image
    cv2.imwrite("sepia_numba_"+imageName,image)
    return image

n = 3
#The start time
startTime = timeit.default_timer()
for i in range(n):
    color2sepia_numba_Imp("rain.jpg")
#The stop time
stopTime = timeit.default_timer()
print("RunTime(Total): " + str(stopTime-startTime))
print("RunTime(Per run): " + str((stopTime-startTime)/n))
