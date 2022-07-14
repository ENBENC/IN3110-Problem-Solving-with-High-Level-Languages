import cv2
import timeit

def sepia_Python_Imp(imageName):
    """This function is a pure python implementation of sepia image with a color_matrix in order of
    red, grenn and blue (RGB). Weigth for red [0.393, 0.769, 0.189], green [0.349, 0.686, 0.168],
    blue [0.272, 0.534, 0.131].
    That is applied to each pixel of the image.
    The function will save a sepia image under the name, sepia_python_imageName.

    Args: String, a file name to the image

    Returns: a 3D numpy array (represent a sepia image)
    """
    #Open the image and turn it ta a 3D array
    #As a note the imread open and return in order of BGR
    image = cv2.imread(imageName)

    #This is sepia matrix that give us the sepia color to the image
    color_matrix = [[ 0.393 , 0.769 , 0.189], #for red
                    [ 0.349 , 0.686 , 0.168], #for green
                    [ 0.272 , 0.534 , 0.131]] #for blue
    #The first for-loop get every rows in the image 3d array
    #The second for-loop get every columns in the iamge 3d array

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
    #save the image that is sepia
    #cv2.imwrite("sepia_python_"+imageName,image)
    return image
