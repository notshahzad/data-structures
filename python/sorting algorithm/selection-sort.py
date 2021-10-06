def selectionSort(arr):
    for i in range(len(arr)):
        sorted = i
        for j in range(sorted, len(arr)):
            if(arr[i] > arr[j]):
                arr[i], arr[j] = arr[j], arr[i]
    return arr


array = [4, 3, 2, 6, 151, 51, 51523]
print(selectionSort(array))
