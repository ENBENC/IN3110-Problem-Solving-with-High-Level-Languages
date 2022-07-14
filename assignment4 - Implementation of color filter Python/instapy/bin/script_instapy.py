import argparse
import cv2
from instapy import *
import timeit

parser = argparse.ArgumentParser(description='using flags by -fl argument, or -flag argument.')

parser.add_argument('-f','--file', type=str, help='The input filename of file to apply filter to.')
parser.add_argument('-se', '--sepia', type=str, help='Select sepia filter.')
parser.add_argument('-g', '--gray', type=str, help='Select gray filter.')

parser.add_argument('-sc', '--scale', type=int, help='Scale factor to resize image.')
parser.add_argument('-o', '--out', type=str, help='The output filename.')
parser.add_argument('-i', '--implement', type=str, help='{python,numba,numpy} Choose the implementation.')
parser.add_argument('-r', '--runtime', type=bool, help= 'track average runtime, Ture/False')
args = parser.parse_args()

def main():
    """User interface for the instapy packages.
    This function will output a image based on the filter user choose.

    Args: None
    Return: None
    """

    if args.file == None:
        raise Exception("The given file not found, for help use -h or --help.")
    if args.sepia==None and args.gray==None:
        raise Exception("Choose a filter, for help use -h or --help.")
    #assum that if both -se and -g flag are given, then do both

    #if user choose gray filter
    if args.gray != None:
        #If the implementation flag not given then default use numpy
        if args.implement == None:
            gray = color2gray_numpy_Imp(args.file)

            if args.runtime:
                #The start time
                startTime = timeit.default_timer()
                for i in range(3):
                    color2gray_numpy_Imp("rain.jpg")
                #The stop time
                stopTime = timeit.default_timer()
                print("Average time over 3 runs(Numpy gray): " + str(stopTime-startTime))

        elif args.implement == "python":
            gray = color2gray_Python_Imp(args.file)

            if args.runtime:
                #The start time
                startTime = timeit.default_timer()
                for i in range(3):
                    color2gray_Python_Imp("rain.jpg")
                #The stop time
                stopTime = timeit.default_timer()
                print("Average time over 3 runs(Python gray): " + str(stopTime-startTime))


        elif args.implement == "numba":
            gray = color2gray_numba_Imp(args.file)

            if args.runtime:
                #The start time
                startTime = timeit.default_timer()
                for i in range(3):
                    color2gray_numba_Imp("rain.jpg")
                #The stop time
                stopTime = timeit.default_timer()
                print("Average time over 3 runs(Numba gray): " + str(stopTime-startTime))

        else:
            gray = color2gray_numpy_Imp(args.file)

            if args.runtime:
                #The start time
                startTime = timeit.default_timer()
                for i in range(3):
                    color2gray_numpy_Imp("rain.jpg")
                #The stop time
                stopTime = timeit.default_timer()
                print("Average time over 3 runs(Numpy gray): " + str(stopTime-startTime))

        #Output the file
        if args.out == None:
            cv2.imwrite("gray_"+args.file,gray)
        else:
            cv2.imwrite(args.out,gray)

    #if user choose sepia filter
    if args.sepia != None:
        #If the implementation flag not given then default use numpy
        if args.implement == None:
            sepia = color2sepia_numpy_Imp(args.file)

            if args.runtime:
                #The start time
                startTime = timeit.default_timer()
                for i in range(3):
                    color2sepia_numpy_Imp("rain.jpg")
                #The stop time
                stopTime = timeit.default_timer()
                print("Average time over 3 runs(Numpy sepia): " + str(stopTime-startTime))

        elif args.implement == "python":
            sepia = sepia_Python_Imp(args.file)

            if args.runtime:
                #The start time
                startTime = timeit.default_timer()
                for i in range(3):
                    sepia_Python_Imp("rain.jpg")
                #The stop time
                stopTime = timeit.default_timer()
                print("Average time over 3 runs(Python sepia): " + str(stopTime-startTime))

        elif args.implement == "numba":
            sepia = color2sepia_numba_Imp(args.file)

            if args.runtime:
                #The start time
                startTime = timeit.default_timer()
                for i in range(3):
                    color2sepia_numba_Imp("rain.jpg")
                #The stop time
                stopTime = timeit.default_timer()
                print("Average time over 3 runs(Numba sepia): " + str(stopTime-startTime))

        else:
            sepia = color2sepia_numpy_Imp(args.file)

            if args.runtime:
                #The start time
                startTime = timeit.default_timer()
                for i in range(3):
                    color2sepia_numpy_Imp("rain.jpg")
                #The stop time
                stopTime = timeit.default_timer()
                print("Average time over 3 runs(Numpy sepia): " + str(stopTime-startTime))


        #Output the file
        if args.out == None:
            cv2.imwrite("sepia_"+args.file,sepia)
        else:
            cv2.imwrite(args.out,sepia)

if __name__=='__main__':
    main()
