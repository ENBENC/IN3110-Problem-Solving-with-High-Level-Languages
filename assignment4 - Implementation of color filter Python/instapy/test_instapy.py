import instapy
from instapy.python_color2gray import color2gray_Python_Imp
from instapy.numpy_color2gray import color2gray_numpy_Imp
from instapy.numba_color2gray import color2gray_numba_Imp

from instapy.python_color2sepia import sepia_Python_Imp
from instapy.numpy_color2sepia import color2sepia_numpy_Imp
from instapy.numba_color2sepia import color2sepia_numba_Imp

import numpy as np
import cv2
import random

def test_Grey():
    """Test python, numpy and numba implementation of grey filter
    The test include create a random image, then get grey image from all three
    python, numpy and numba implementation of grey filter. Then a for-loop runs 100 times,
    that cheak for a random pixel from each grey image is equal to a cheak_pixel, that is
    from the orginal image and applied weigth on.

    Args: None
    Returns: None
    """
    #index range of first dimention 0-99
    #index range of secound dimention 0-99
    #index range of third dimention 0-2
    #image is a 3D numpy array that have shape(100, 100 ,3)
    #The max value of each pixel is a random int from 0 to 255
    image = np.random.randint(0, 255, size=(100, 100, 3))
    cv2.imwrite("test_grey.jpg",image)

    image = cv2.imread("test_grey.jpg")
    python_Grey = color2gray_Python_Imp("test_grey.jpg")
    numpy_Grey = color2gray_numpy_Imp("test_grey.jpg")
    numba_Grey = color2gray_numba_Imp("test_grey.jpg")

    #weigth of grey filter 0.07(red), 0.72(green) ,0.21(blue)
    #i_third=0 is blue, i_third=1 is green, i_third=2 is red

    for i in range(100):
        i_first = random.randint(0,99)
        i_secound = random.randint(0,99)
        i_third = random.randint(0,2)
        cheak_pixel = 0
        #apply weigth
        cheak_pixel = image[i_first][i_secound][0]*0.07
        cheak_pixel += image[i_first][i_secound][1]*0.72
        cheak_pixel += image[i_first][i_secound][2]*0.21



        cheak_pixel = int(cheak_pixel)
        assert python_Grey[i_first][i_secound][i_third] == cheak_pixel
        assert numpy_Grey[i_first][i_secound][i_third] == cheak_pixel
        assert numba_Grey[i_first][i_secound][i_third] == cheak_pixel

    print("All 100 tests are done in test_Grey!")

        #breakpoint()

def test_sepia():
    """Test python, numpy and numba implementation of sepia filter
    The test include create a random image, then get sepia image from all three
    python, numpy and numba implementation of sepia filter. Then a for-loop runs 100 times,
    that cheak for a random pixel from each sepia image is equal to a cheak_pixel, that is
    from the orginal image and applied weigth on.

    Args: None
    Returns: None
    """
    #index range of first dimention 0-99
    #index range of secound dimention 0-99
    #index range of third dimention 0-2
    #image is a 3D numpy array that have shape(100, 100 ,3)
    #The max value of each pixel is a random int from 0 to 255
    image = np.random.randint(0, 255, size=(100, 100, 3))
    cv2.imwrite("test_sepia.jpg",image)

    image = cv2.imread("test_sepia.jpg")
    python_sepia = sepia_Python_Imp("test_sepia.jpg")
    numpy_sepia = color2sepia_numpy_Imp("test_sepia.jpg")
    numba_sepia = color2sepia_numba_Imp("test_sepia.jpg")

    #weigth of grey filter 0.07(red), 0.72(green) ,0.21(blue)
    #i_third=0 is blue, i_third=1 is green, i_third=2 is red
    color_matrix = [[ 0.393 , 0.769 , 0.189], #for red
                    [ 0.349 , 0.686 , 0.168], #for green
                    [ 0.272 , 0.534 , 0.131]] #for blue

    for i in range(100):
        i_first = random.randint(0,99)
        i_secound = random.randint(0,99)
        i_third = random.randint(0,2)

        cheak_pixel = 0
        #Get the three channels
        r_c = image[i_first][i_secound][2]
        g_c = image[i_first][i_secound][1]
        b_c = image[i_first][i_secound][0]

        if i_third == 0:
            cheak_pixel = r_c*color_matrix[2][0] + g_c*color_matrix[2][1] + b_c*color_matrix[2][2]
        elif i_third == 1:
            cheak_pixel = r_c*color_matrix[1][0] + g_c*color_matrix[1][1] + b_c*color_matrix[1][2]
        else:
            cheak_pixel = r_c*color_matrix[0][0] + g_c*color_matrix[0][1] + b_c*color_matrix[0][2]

        cheak_pixel = min(255,int(cheak_pixel))
        assert python_sepia[i_first][i_secound][i_third] == cheak_pixel
        assert numpy_sepia[i_first][i_secound][i_third] == cheak_pixel
        assert numba_sepia[i_first][i_secound][i_third] == cheak_pixel

    print("All 100 tests are done in test_sepia!")

test_Grey()
test_sepia()
