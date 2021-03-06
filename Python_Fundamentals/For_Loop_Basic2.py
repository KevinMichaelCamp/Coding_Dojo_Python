# For Loop Basic 2

# 1. Biggie Size - Given an array, write a function that changes all positive numbers in the array to "big". Example: makeItBig([-1,3,5,-5]) returns that same array. changed to [-1,"big","big",-5].

# Using FOR loop


def makeItBig(arr):

    for num in range(len(arr)):

        if arr[num] > 0:
            arr[num] = 'big'

    print(arr)
    return arr


# Test Case
makeItBig([-1, 3, 5, -5])

# Using WHILE loop


def makeItBig(arr):

    i = 0

    while i < len(arr):
        if arr[i] > 0:
            arr[i] = 'big'

        i = i + 1

    print(arr)
    return arr


# Test  Case
makeItBig([-1, 2, -3, -5, 6, -7, 8])


# 2. Count Positives - Given an array of numbers, create a function to replace last value with the number of positive values. Example, countPositives([-1,1,1,1]) changes the array to [-1,1,1,3] and returns it. (Note that zero is not considered to be a positive number).

# Using FOR loop
def countPositives(arr):

    count = 0

    for num in range(len(arr)):
        if arr[num] > 0:
            count = count + 1

    arr[len(arr) - 1] = count

    print(arr)
    return arr


# Test Case
countPositives([-1, 1, 1, 1])

# Using WHILE loop


def countPositives(arr):

    count = 0
    i = 0

    while i < len(arr):
        if arr[i] > 0:
            count = count + 1

        i = i + 1

    arr[len(arr) - 1] = count

    print(arr)
    return arr


# Test Case
countPositives([-1, 2, -3, 4, -5, 6, -7, 8, -9])


# 3. SumTotal - Create a function that takes an array as an argument and returns the sum of all the values in the array. For example sumTotal([1,2,3,4]) should return 10.

# Using FOR Loop
def sumTotal(arr):

    total = 0

    for num in range(len(arr)):
        total = total + arr[num]

    print(total)
    return total


# Test Case
sumTotal([1, 2, 3, 4])

# Using WHILE loop


def sumTotal(arr):

    total = 0
    i = 0

    while i < len(arr):
        total = total + arr[i]
        i = i + 1

    print(total)
    return total


# Test Case
sumTotal([1, 2, 3, 4, 5, 6, 7, 8, 9])


# 4. Average - Create a function that takes an array as an argument and returns the average of all values in the array. For example average([1,2,3,4]) should return 2.5.

# Using FOR Loop
def average(arr):

    total = 0

    for num in range(len(arr)):
        total = total + arr[num]

    average = total / len(arr)

    print(average)
    return average


average([1, 2, 3, 4])

# Using WHILE loop


def average(arr):

    total = 0
    i = 0

    while i < len(arr):
        total = total + arr[i]
        i = i + 1

    average = total / len(arr)

    print(average)
    return average


average([1, 2, 3, 4, 5, 6, 7, 8, 9])


# 5. Length - Create a function that takes an array as an argument and returns the length of the array. For example length([1,2,3,4]) should return 4.

# Using FOR loop
def length(arr):

    length = 0

    for num in range(len(arr)):
        length = length + 1

    print(length)
    return length


# Test Case
length([1, 2, 3, 4])

# Using WHILE Loop


def length(arr):

    i = 0
    length = 0

    while i < len(arr):
        length = length + 1
        i = i + 1

    print(length)
    return length


# Test Case
length([1, 2, 3, 4, 5, 6, 7, 8, 9])


# 6. Minimum - Create a function that takes an array as an argument and returns the minimum value in the array. If the passed array is empty, have the function return False. For example, minimum([1,2,3,4]) should return 1; minimum([-1,-2,-3]) should return -3.

# Using FOR Loop
def minimum(arr):

    minimum = arr[0]

    if arr == []:
        return False

    for num in range(len(arr)):
        if arr[num] < minimum:
            minimum = arr[num]

    print(minimum)
    return minimum


# Test Case
minimum([1, 2, 3, 4])
minimum([-1, -2, -3])

# Using WHILE Loop


def minimum(arr):

    minimum = arr[0]
    i = 0

    if arr == []:
        return False

    while i < len(arr):
        if arr[i] < minimum:
            minimum = arr[i]
        i = i + 1

    print(minimum)
    return minimum


# Test Case
minimum([5, 4, 1, 2, 6, 8])

# 7. Maximum - Create a function that takes an array as an argument and returns the maximum value in the array. If the passed array is empty, have the function return False. For example, maximum([1,2,3,4]) should return 4; maximum([-1,-2,-3]) should return -1.

# Using FOR Loop


def maximum(arr):

    maximum = arr[0]

    if arr == []:
        return False

    for num in range(len(arr)):
        if arr[num] > maximum:
            maximum = arr[num]

    print(maximum)
    return maximum


# Test Case
maximum([1, 2, 3, 4])
maximum([-1, -2, -3])

# Using WHILE Loop


def maximum(arr):

    maximum = arr[0]
    i = 0

    if arr == []:
        return False

    while i < len(arr):
        if arr[i] > maximum:
            maximum = arr[i]
        i = i + 1

    print(maximum)
    return maximum


# Test Case
maximum([1, 2, 3, 4, 5, 9, 6, 7, 8])
maximum([-2, -4, -5, -1, -9])


# 8. UltimateAnalyze - Create a function that takes an array as an argument and returns a dictionary that has the sumTotal, average, minimum, maximum, and length of the aray.

# Using FOR Loop
def UltimateAnalyze(arr):

    total = 0
    minimum = arr[0]
    maximum = arr[0]
    count = 0

    if arr == []:
        return False

    for num in range(len(arr)):
        total = total + arr[num]
        count = count + 1

        if arr[num] < minimum:
            minimum = arr[num]
        elif arr[num] > maximum:
            maximum = arr[num]

    average = total / count
    summary = {"Total": total, "Average": average,
               "Minimum": minimum, "Maximum": maximum, "Length": count}

    print(summary)
    return summary


# Test Case
UltimateAnalyze([1, 2, 3, 4, 5, 6, 7, 8, 9])

# Using WHILE Loop


def UltimateAnalyze(arr):

    total = 0
    minimum = arr[0]
    maximum = arr[0]
    count = 0
    i = 0

    if arr == []:
        return False

    while i < len(arr):
        total = total + arr[i]
        count = count + 1

        if arr[i] < minimum:
            minimum = arr[i]
        elif arr[i] > maximum:
            maximum = arr[i]

        i = i + 1

    average = total / count
    summary = {"Total": total, "Average": average,
               "Minimum": minimum, "Maximum": maximum, "Length": count}

    print(summary)
    return summary


# Test Case
UltimateAnalyze([99, 92, 85, 88, 67, 85, 88, 54, 92, 73])

# 9. ReverseList - Create a function that takes an array as an argument and return an array in a reversed order. Do this without creating an empty temporary array. For example reverse([1,2,3,4]) should return [4,3,2,1]. This challenge is known to appear during basic technical interviews.

# Using FOR Loop


def reverseList(arr):

    temp = arr[0]

    for num in range(int(len(arr) / 2)):
        arr[num] = arr[len(arr) - (num + 1)]
        arr[len(arr) - (num + 1)] = temp
        temp = arr[num + 1]

    print(arr)
    return arr


# Test Case
reverseList([1, 2, 3, 4])
# Using WHILE loop


def reverseList(arr):

    temp = arr[0]
    i = 0

    while i < (len(arr) / 2):
        arr[i] = arr[len(arr) - (i + 1)]
        arr[len(arr) - (i + 1)] = temp
        temp = arr[i + 1]
        i = i + 1

    print(arr)
    return arr


# Test Case
reverseList([2, 4, 6, 8])
                                           
