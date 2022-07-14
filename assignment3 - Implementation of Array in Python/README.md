ar.py contains solution to task 3.1 and test_Array.py contains solution to task 3.2. 
ar2d.py contains both solution to 1d array and 2d array and test_Array2d.py contains test to both 1d array and 2d array. 


testFile test_Array2d.py 
You can run the test file with pytest or just as a python file, both ways works.
The test file have 7 tests, that test add, sub, mult, eq, is_equal and min_element.

Implementation of 2d array
The self._array only contains a flat array, beacuse it is easier operate with.
When the user print out the or getting values out of the 2d array. Then the array is
translated to a 2d array with buildArray function based on the flat array self._array.

Implementation of the __mul__ function in 2d array. I assumed that the multiplication operation is element wise.
The multiplication is not implemented as a matrix operation.

To get the item out of a 2D array my_array[row, col]