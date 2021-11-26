def quicksort(l, r):
    if l >= r:
        return
    p = partition(l, r)
    quicksort(l, p-1)
    quicksort(l+1, r)


def partition(l, r):
    pivot = arr[r]
    i = l - 1
    for j in range(l, r):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[r] = arr[r], arr[i+1]
    return i + 1


arr = [456, 32426, 3456234, 67, 856785, 657, 456, 73]
quicksort(0, len(arr)-1)
print(arr)
