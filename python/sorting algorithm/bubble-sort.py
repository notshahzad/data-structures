array = [5, 4, 6, 8, 7, 3, 0, 1, 9, 2]


def sort(arr):
    for x in range(len(arr)):
        for y in range(len(arr)):
            if(arr[x] < arr[y]):
                arr[x], arr[y] = arr[y], arr[x]
    return arr


sorted = sort(array)
print(sorted)
