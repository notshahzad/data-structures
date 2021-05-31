array = list(range(1, int(input("Input Array Length :"))))
#array = [-4, -2, 5, 6, 8, 10, 14]


def search(num, arr):
    start = 0
    end = len(arr)
    while True:
        mid = (start + end) // 2
        if(arr[mid] == num):
            return mid
            break
        elif(arr[mid] < num):
            start = mid
        elif(arr[mid] > num):
            end = mid
        if(start == end-1 and arr[0] != num):
            return -1
            break


output = search(int(input("Search :")), array)
print(output)
