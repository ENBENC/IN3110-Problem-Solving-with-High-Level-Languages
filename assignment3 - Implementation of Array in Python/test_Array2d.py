from ar2d import Array
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

    #test 2d
    #------------------------------------------------------------

    testArray5 = Array((6 ,) , 1, 2, 3, 4, 5,6)
    testArray6 = Array((3 ,2) , 1, 1, 1, 1, 1, 1)
    testArray7 = Array((3 ,2) , 8, 3, 4, 1, 6, 1)

    testArray4 = Array((6 ,) , 1, 0, 0, 1, 1, 1)
    #test with 2 arrays
    assert (testArray5+testArray4) == Array((6 ,), 2, 2, 3, 5 ,6,7)
    assert (testArray6+testArray7) == Array((3 ,2), 9, 4, 5, 2 ,7 ,2)
    #test with 1 array and 1 int
    assert (testArray6+10) == Array((3 ,2), 11, 11, 11, 11 ,11, 11)
    assert (10+testArray6) == Array((3 ,2), 11, 11, 11, 11 ,11, 11)

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
    #test 2d
    #------------------------------------------------------------
    testArray5 = Array((6 ,) , 1, 2, 3, 4, 5,6)
    testArray6 = Array((3 ,2) , 1, 1, 1, 1, 1, 1)
    testArray7 = Array((3 ,2) , 8, 3, 4, 1, 6, 1)

    #test with 2 arrays
    assert (testArray6-testArray7) == Array((3 ,2), 1-8, 1-3, 1-4, 1-1 ,1-6,1-1)
    assert (testArray7-testArray6) == Array((3 ,2), 8-1, 3-1, 4-1, 1-1 ,6-1, 1-1)
    #test with 1 array and 1 int
    assert (testArray7-10) == Array((3 ,2), 8-10, 3-10, 4-10, 1-10, 6-10, 1-10)
    assert (10-testArray7) == Array((3 ,2), 10-8, 10-3, 10-4, 10-1, 10-6, 10-1)

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
    #test 2d
    #------------------------------------------------------------
    testArray5 = Array((6 ,) , 1, 2, 3, 4, 5,6)
    testArray6 = Array((3 ,2) , 1, 1, 1, 1, 1, 1)
    testArray7 = Array((3 ,2) , 8, 3, 4, 1, 6, 1)
    testArray8 = Array((3 ,2) , 1, 1, 1, 1, 1, 1)
    assert (testArray6 == testArray8) == True
    assert (testArray6 == testArray7) == False
    assert (testArray7 == testArray8) == False

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
    #test 2d
    #------------------------------------------------------------
    testArray5 = Array((6 ,) , 1, 2, 3, 4, 5,6)
    testArray6 = Array((3 ,2) , 1, 1, 1, 1, 1, 1)
    testArray7 = Array((3 ,2) , 8, 3, 4, 1, 6, 1)
    testArray8 = Array((3 ,2) , 1, 1, 1, 1, 1, 1)
    returnArray2 = testArray7.is_equal(testArray8)
    check = (False, False, False, True, False, True)
    i = 0
    for value in returnArray2.getArray():
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
    #test 2d
    #------------------------------------------------------------
    testArray5 = Array((6 ,) , 1, 2, 3, 4, 5, 6)
    testArray6 = Array((3 ,2) , 1, 1, 1, 1, 1, 1)
    testArray7 = Array((3 ,2) , 8, 3, 4, 1, 6, 1)
    testArray8 = Array((3 ,2) , 1, 1, 1, 1, 1, 1)
    assert testArray5.min_element() == 1
    assert testArray6.min_element() == 1
    assert testArray7.min_element() == 1
    assert testArray8.min_element() == 1

def main():
    test_print()
    test_adding()
    test_sub()
    test_mult()
    test_eq()
    test_is_equal()
    test_min_element()
    print("all tests passed!")
    testArray7 = Array((3 ,2) , 8, 3, 4, 1, 6, 1)


main()
