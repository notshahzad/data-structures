def mergesort(arr):
    larr = []
    rarr = []
    mid = len(arr)//2
    if len(arr) < 2:
        return
    for i in range(0, mid):
        larr.append(arr[i])
    for i in range(mid, len(arr)):
        rarr.append(arr[i])
    mergesort(larr)
    mergesort(rarr)
    merge(larr, rarr, arr)


def merge(larr, rarr, arr):
    left = 0
    right = 0
    index = 0
    while(left < len(larr) and right < len(rarr)):
        if larr[left] <= rarr[right]:
            arr[index] = larr[left]
            left += 1
        else:
            arr[index] = rarr[right]
            right += 1
        index += 1
    while(left < len(larr)):
        arr[index] = larr[left]
        left += 1
        index += 1
    while(right < len(rarr)):
        arr[index] = rarr[right]
        right += 1
        index += 1


array = [8, 423, 727, 69, 420, 1]
print(f'unsorted array : {array}')
mergesort(array)
print(f'sorted array : {array}')
