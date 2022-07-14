from .numpy_color2gray import color2gray_numpy_Imp
from .numpy_color2sepia import color2sepia_numpy_Imp
from .numba_color2gray import color2gray_numba_Imp
from .numba_color2sepia import color2sepia_numba_Imp
from .python_color2gray import color2gray_Python_Imp
from .python_color2sepia import sepia_Python_Imp
import cv2

def grayscale_image(input_filename, output_filename=None):
    """This is a function that return and save a grey image.
    This function takes a input filename and then turn the image to a grey image
    with the numpy implementation from numpy_color2gray.py.
    output_filename by default is None, but if output_filename is not None, then save the
    grey image in the given path. When sending output_filename the "\" must be replaced with "/".

    Args: input_filename(String), output_filename(String optional)

    Return: a 3D numpy array (reoresent a grey image)

    """
    image = color2gray_numpy_Imp(input_filename)
    #Save the greyScale image
    if output_filename == None:
        cv2.imwrite("greyScale_"+input_filename,image)
    else:
        cv2.imwrite(output_filename +'/greyScale_'+input_filename, image)

    return image

def sepia_image(input_filename, output_filename=None):
    """This is a function that return and save a sepia image.
    This function takes a input filename and then turn the image to a sepia image
    with the numpy implementation from numpy_color2sepia.py.
    output_filename by default is None, but if output_filename is not None, then save the
    sepia image in the given path. When sending output_filename the "\" must be replaced with "/".

    Args: input_filename(String), output_filename(String optional)

    Return: a 3D numpy array (reoresent a sepia image)

    """
    image = color2sepia_numpy_Imp(input_filename)
    #Save the greyScale image
    if output_filename == None:
        cv2.imwrite("sepia_"+input_filename,image)
    else:
        cv2.imwrite(output_filename +'/sepia_'+input_filename, image)

    return image
