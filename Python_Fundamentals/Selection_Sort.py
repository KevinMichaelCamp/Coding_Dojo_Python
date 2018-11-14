# Selection Sort
arr = [50,32,2,77,25]


def selectionSort(arr):
    for i in range(len(arr)):
        minIndex = i

        for j in range(i + 1, len(arr)):
            if arr[minIndex] > arr[j]:
                minIndex = j
        arr[i], arr[minIndex] = arr[minIndex], arr[i]

    print(arr)
    return arr

selectionSort(arr)
