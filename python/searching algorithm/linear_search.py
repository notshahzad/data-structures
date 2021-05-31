array = [-2, 4, 9, 12, 3, 6]
num = int(input())


def search(num, arr):
    for x in range(len(arr)):
        if(arr[x] == num):
            return x
            break
    return -1


output = search(num, array)
print(output)
