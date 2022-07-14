from ar import Array

#Check that the __str__ in Array give a string representation of Array
def test_print():
    testArray1 = Array((5 ,) , 1, 2, 0, 4, 5)
    testArray2 = Array((5 ,) , 6, 7, 8, 9, 5)
    testArray3 = Array((5 ,) , 1, 2, 0, 4, 5)

    assert testArray1.__str__() == "[1, 2, 0, 4, 5]"
    assert testArray2.__str__() == "[6, 7, 8, 9, 5]"
    assert testArray3.__str__() == "[1, 2, 0, 4, 5]"

#Check adding element-wise and the return value
def test_adding():
    testArray1 = Array((5 ,) , 1, 2, 0, 4, 5)
    testArray2 = Array((5 ,) , 6, 7, 8, 9, 5)
    testArray3 = Array((5 ,) , 1, 2, 0, 4, 5)
    #test with 2 arrays
    assert (testArray1+testArray3) == Array((5 ,), 2, 4, 0, 8 ,10)
    assert (testArray3+testArray1) == Array((5 ,), 2, 4, 0, 8 ,10)
    #test with 1 array and 1 int
    assert (testArray3+10) == Array((5 ,), 11, 12, 10, 14 ,15)
    assert (10+testArray3) == Array((5 ,), 11, 12, 10, 14 ,15)

#Check substractiong element-with and the return
def test_sub():
    testArray1 = Array((5 ,) , 1, 2, 0, 4, 5)
    testArray2 = Array((5 ,) , 6, 7, 8, 9, 5)
    testArray3 = Array((5 ,) , 1, 2, 0, 4, 5)
    testArray4 = Array((5 ,) , 0.0, 0.0, 0.0, 0.0, 0.0)
    #test with 2 arrays
    assert (testArray1-testArray3) == Array((5 ,), 0, 0, 0, 0 ,0)
    assert (testArray3-testArray1) == Array((5 ,), 0, 0, 0, 0 ,0)
    assert (testArray3-testArray4) == Array((5 ,), 1.0, 2.0, 0.0, 4.0 ,5.0)
    #test with 1 array and 1 int
    assert (testArray3-10) == Array((5 ,), 1-10, 2-10, 0-10, 4-10 ,5-10)
    assert (10-testArray3) == Array((5 ,), 10-1, 10-2, 10-0, 10-4 ,10-5)

#Check multiplying element-with and the return
def test_mult():
    testArray1 = Array((5 ,) , 1, 2, 0, 4, 5)
    testArray2 = Array((5 ,) , 6, 7, 8, 9, 5)
    testArray3 = Array((5 ,) , 1, 2, 0, 4, 5)
    testArray4 = Array((5 ,) , 1.3, 2.1, 0.1, 4.6, 5.9)
    #test with 2 arrays
    assert (testArray1*testArray3) == Array((5 ,), 1, 4, 0, 16 ,25)
    assert (testArray3*testArray1) == Array((5 ,), 1, 4, 0, 16 ,25)
    #test with 1 array and 1 int
    assert (testArray3*10) == Array((5 ,), 10, 20, 0, 40 ,50)
    assert (10*testArray3) == Array((5 ,), 10, 20, 0, 40 ,50)
    assert (10*testArray4) == Array((5 ,), 13.0, 21.0, 1.0, 46.0 ,59.0)

#Check comparing to arrays and return a boolean. "__eq__"
def test_eq():
    testArray1 = Array((5 ,) , 1, 2, 0, 4, 5)
    testArray2 = Array((5 ,) , 6, 7, 8, 9, 5)
    testArray3 = Array((5 ,) , 1, 2, 0, 4, 5)
    testArray4 = Array((5 ,) , 1.3, 2.1, 0.1, 4.6, 5.9)
    assert (testArray1 == testArray3) == True
    assert (testArray1 == testArray2) == False
    assert (testArray1 == testArray4) == False

#Check comparing to arrays element-with. "is_equal"
def test_is_equal():
    testArray1 = Array((5 ,) , 1, 2, 0, 4, 5)
    testArray2 = Array((5 ,) , 6, 7, 8, 9, 5)
    testArray3 = Array((5 ,) , 1, 2, 0, 4, 5)
    returnArray = testArray1.is_equal(testArray2)
    check = (False, False, False, False, True)
    i = 0
    for value in returnArray.getArray():
        assert value == check[i]
        i+=1

#Check the smallest value. "min_element"
def test_min_element():
    testArray1 = Array((5 ,) , 1, 2, 0, 4, 5)
    testArray2 = Array((5 ,) , 6, 7, 8, 9, 5)
    testArray3 = Array((5 ,) , 1, 2, 0, 4, 5)
    testArray4 = Array((5 ,) , 1.3, 2.1, 0.1, 4.6, 5.9)
    assert testArray1.min_element() == 0
    assert testArray2.min_element() == 5
    assert testArray3.min_element() == 0
    assert testArray4.min_element() == 0.1

def main():
    test_print()
    test_adding()
    test_sub()
    test_mult()
    test_eq()
    test_is_equal()
    test_min_element()
    print("all tests passed!")

main()
