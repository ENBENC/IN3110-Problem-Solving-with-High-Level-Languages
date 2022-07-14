gray Filter:
    Solution of task 4.1, each file can be run directly. 
    The program will save the gray image and print out the runtime after 3 runs.
    Report of each implementation in ../gray Filter/Reports.

sepia Filter:
    Solution of task 4.2, each file can be run directly.
    The program will save the sepia image and print out the runtime after 3 runs.
    Report of each implementation in ../sepia Filter/Reports.

instapy:
    Solution of task 4.3, 4.4, 4.6.
    setutp.py, setup file to package instapy (Solution to 4.3).
    test_instapy.py, run with pytest, by tast directly "pytest" on terminal (Solution to 4.3).

../instapy/instapy:
    Path of solution to task 4.3.
    Python package, with all implementation of gray and sepia filter.
    __init__.py contains implemetation of "grayscale_image" and "sepia_image"

../instapy/bin:
    Solution of task 4.4, 4.6.
    script_instapy.py, reason I changed name of this file is because I got import problem when I want to import instapy package.
    By trying out of diffrent solutions, it works when I changed the name of the script file.
    This file is a script of user interface to the package "instapy". It can be run directly with flags:

    Ex: python script_instapy -f "filename" -se "whatever input" -g "whatever input" -i "python/numpy/numba" -o "output_filename" -r "True/False"

    Solution to 4.6 runtime is also implemented in script_instapy.py.



