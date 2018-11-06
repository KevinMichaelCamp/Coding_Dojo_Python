# Functions Basic 2

## 1. - Countdown - Create a function that accepts a number as an input. Return a new array that counts down by one, from the number (as array's 'zero'th element) down to 0 (as the last element). For example countDown(5) should return [5,4,3,2,1,0].

def countDown(num):
    arr = []


    for i in range(0, num + 1):
        arr.append(num - i)

    print(arr)

countDown(5)

## 2. - Print & Return - Your function will receive an array with two numbers. Print the first value, and return the second.

def printReturn(arr):
    print(arr[0])
    return arr[1]

printReturn([4,7])

## 3. - First Plus Length - Given an array, return the sum of the first value in the array, plus the array's length.

def firstPlusLength(arr):
    print(arr[0] + len(arr))
    return (arr[0] + len(arr))

firstPlusLength([1,2,3,4,5,6])

## 4. - Values Greater Than Second - Write a function that accepts any array, and returns a new array with the array values that are greater than its 2nd value. Print how many values this is. If the array is only one element long, have the function return False.

def greaterThanSecond(arr):
    newArr = []

    if len(arr) <= 1:
        return False

    for i in range(len(arr)):
        if arr[i] > arr[1]:
            newArr.append(arr[i])

    print("There are " + str(len(newArr)) + " values greater than " + str(arr[1]))
    print(newArr)

greaterThanSecond([1,2,3,4,5,6,7,8,9])


## 5. - This Length, That Value - Write a function called lengthAndValue which accepts two parameters, size and value. This function should take two numbers and return a list of length size containing only the number in value. For example, lengthAndValue(4,7) should return [7,7,7,7].

def lengthAndValue(size, val):
    arr = []

    for i in range(0, size):
        arr.append(val)

    print(arr)

lengthAndValue(4,7)
