def CountingSort(arr):
    rangedarr = [0]*9
    for i in arr:
        rangedarr[i] += 1
    for i in range(1, len(rangedarr)):
        rangedarr[i] += rangedarr[i-1]
    sortedarr = [0]*len(arr)
    for i in arr:
        sortedarr[rangedarr[i]-1] = i
        rangedarr[i] -= 1
    return sortedarr


array = [1, 3, 2, 5, 4]
sortedarray = CountingSort(array)
print(sortedarray)
