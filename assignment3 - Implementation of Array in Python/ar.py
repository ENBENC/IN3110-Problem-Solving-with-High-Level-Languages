class Array:
    def __init__(self, shape, *values):
        """

        Initialize an array of 1-dimensionality. Elements can only be of type:
        - int
        - float
        - bool

        Make sure that you check that your array actually is an array, which means it is homogeneous (one data type).
        Args:
            shape (tuple): shape of the array as a tuple. A 1D array with n elements will have shape = (n,).
            *values: The values in the array. These should all be the same data type. Either numeric or boolean.
        Raises:
            ValueError: If the values are not all of the same type.
            ValueError: If the number of values does not fit with the shape.
        """

        # Check if the values are of valid type
        #Cheack that the length of the array is same as the shape
        if len(values) != shape[0]:
            print("The length of array does not match with the given shape")
            raise ValueError

        #Cheack every element is the same type
        for element in values:
            if type(element) != type(values[0]):
                print("The array contains values of different type")
                raise ValueError

        self._array = values
        self._shape = shape
        self._type = type(values[0])


    def __str__(self):
        """Returns a nicely printable string representation of the array.
        Returns:
            str: A string representation of the array.
        """
        stringArray = str(self._array)
        stringArray = stringArray.replace("(", "[")
        stringArray = stringArray.replace(")", "]")
        #This will print a 1D array and look something like [value1, ..., valueN]
        return stringArray

    def __add__(self, other):
        """Element-wise adds Array with another Array or number.
        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.
        Args:
            other (Array, float, int): The array or number to add element-wise to this array.
        Returns:
            Array: the sum as a new array.
        """
        if type(other) != Array and type(other) != int and type(other) != float:
            return NotImplemented
        # check that the method supports the given arguments (check for data type and shape of array)
        if type(other) == float or type(other) == int:
            lst = list()
            for value in self._array:
                lst.append(other + value)
            return Array(self._shape,*lst)

        elif self._shape[0] != other.getShape()[0]:
            return NotImplemented
        else:
            lst = list()
            for i in range(len(self._array)):
                lst.append(other[i] + self._array[i])
            return Array(self._shape,*lst)


    def __radd__(self, other):
        """Element-wise adds Array with another Array or number.
        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.
        Args:
            other (Array, float, int): The array or number to add element-wise to this array.
        Returns:
            Array: the sum as a new array.
        """
        return self.__add__(other)

    def __sub__(self, other):
        """Element-wise subtracts an Array or number from this Array.
        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.
        Args:
            other (Array, float, int): The array or number to subtract element-wise from this array.
        Returns:
            Array: the difference as a new array.
        """
        if type(other) != Array and type(other) != int and type(other) != float:
            return NotImplemented
        # check that the method supports the given arguments (check for data type and shape of array)
        if type(other) == float or type(other) == int:
            lst = list()
            for value in self._array:
                lst.append(value - other)
            return Array(self._shape,*lst)

        elif self._shape[0] != other.getShape()[0]:
            return NotImplemented
        else:
            lst = list()
            for i in range(len(self._array)):
                lst.append(self._array[i] - other[i])
            return Array(self._shape,*lst)

    def __rsub__(self, other):
        """Element-wise subtracts this Array from a number or Array.
        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.
        Args:
            other (Array, float, int): The array or number being subtracted from.
        Returns:
            Array: the difference as a new array.
        """
        if type(other) != Array and type(other) != int and type(other) != float:
            return NotImplemented
        # check that the method supports the given arguments (check for data type and shape of array)
        if type(other) == float or type(other) == int:
            lst = list()
            for value in self._array:
                lst.append(other - value)
            return Array(self._shape,*lst)

        elif self._shape[0] != other.getShape()[0]:
            return NotImplemented
        else:
            lst = list()
            for i in range(len(self._array)):
                lst.append(other[i] - self._array[i])
            return Array(self._shape,*lst)

    def __mul__(self, other):
        """Element-wise multiplies this Array with a number or array.
        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.
        Args:
            other (Array, float, int): The array or number to multiply element-wise to this array.
        Returns:
            Array: a new array with every element multiplied with `other`.
        """
        if type(other) != Array and type(other) != int and type(other) != float:
            return NotImplemented
        # check that the method supports the given arguments (check for data type and shape of array)
        if type(other) == float or type(other) == int:
            lst = list()
            for value in self._array:
                lst.append(value * other)
            return Array(self._shape,*lst)

        elif self._shape[0] != other.getShape()[0]:
            return NotImplemented
        else:
            lst = list()
            for i in range(len(self._array)):
                lst.append(self._array[i] * other[i])
            return Array(self._shape,*lst)

    def __rmul__(self, other):
        """Element-wise multiplies this Array with a number or array.
        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.
        Args:
            other (Array, float, int): The array or number to multiply element-wise to this array.
        Returns:
            Array: a new array with every element multiplied with `other`.
        """
        # Hint: this solution/logic applies for all r-methods
        return self.__mul__(other)

    def __eq__(self, other):
        """Compares an Array with another Array.
        If the two array shapes do not match, it should return False.
        If `other` is an unexpected type, return False.
        Args:
            other (Array): The array to compare with this array.
        Returns:
            bool: True if the two arrays are equal (identical). False otherwise.
        """
        #Check the other is Array and the shape match with the shape of this array
        if type(other) != Array:
            return False
        if self._shape[0] != len(other.getArray()):
            return False
        #Check to arrays element-wise equal
        for i in range(len(other.getArray())):
            if self._array[i] != other[i]:
                return False
        return True

    def is_equal(self, other):
        """Compares an Array element-wise with another Array or number.
        If `other` is an array and the two array shapes do not match, this method should raise ValueError.
        If `other` is not an array or a number, it should return TypeError.
        Args:
            other (Array, float, int): The array or number to compare with this array.
        Returns:
            Array: An array of booleans with True where the two arrays match and False where they do not.
                   Or if `other` is a number, it returns True where the array is equal to the number and False
                   where it is not.
        Raises:
            ValueError: if the shape of self and other are not equal.
        """
        #Check that other is a Array or int or float, and check that other have same shape with this array if other is a array
        if type(other) != Array and type(other) != int and type(other) != float:
            raise TypeError
        if type(other) == Array :
            if self._shape[0] != len(other.getArray()):
                raise ValueError

        booleanList = list()
        #if other is int or float, check this array one by one with other
        #else check element-wise two arrays
        #save the resualt in booleanList
        if type(other) == int or type(other) == float:
            for value in self._array:
                if value == other:
                    booleanList.append(True)
                else:
                    booleanList.append(False)
        else:
            for i in range(len(other.getArray())):
                if self._array[i] == other[i]:
                    booleanList.append(True)
                else:
                    booleanList.append(False)
        return Array(self._shape,*booleanList)

    def getArray(self):
        return self._array
    def getShape(self):
        return self._shape
    def getType(self):
        return self.type

    def min_element(self):
        """Returns the smallest value of the array.
        Only needs to work for type int and float (not boolean).
        Returns:
            float: The value of the smallest element in the array.
        """
        if self._type != bool:
            min = self._array[0]
            for value in self._array:
                if value <= min:
                    min = value
            return float(min)
        else:
            print("This is a array that only contains boolean")
            raise TypeError

    def __getitem__(self, i):
        """
        Return element in the index i
        Args: int(index)
        Returns: int, float, boolean
        """
        return self._array[i]
