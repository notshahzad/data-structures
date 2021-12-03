def radixSort(arr):
    max1 = max(arr)
    index = 10
    while int(max1) > 0:
        countingSort(arr, index)
        index *= 10
        max1 = max1/10


def countingSort(arr, index):
    sortedarr = [0]*len(arr)
    rangearr = [0]*10
    for i in arr:
        rangearr[i % index // (index//10)] += 1
    for i in range(1, len(rangearr)):
        rangearr[i] += rangearr[i-1]
    for i in range(len(arr)-1, -1, -1):
        sortedarr[rangearr[arr[i] % index // (index//10)]-1] = arr[i]
        rangearr[arr[i] % index//(index//10)] -= 1
    for i in range(0, len(arr)):
        arr[i] = sortedarr[i]


arr = [420, 69, 727, 234, 43, 54, 141, 1345]
radixSort(arr)
print(arr)
