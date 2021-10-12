def insertionSort(array):
    for i in range(1, len(array)):
        j = i
        crnt = array[i]
        while j > 0 and crnt < array[j-1]:
            array[j] = array[j-1]
            j -= 1
        array[j] = crnt
    return arr


arr = [8, 727, 69, 420, 1]
sortedarr = insertionSort(arr)
print(sortedarr)
