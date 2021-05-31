array = list(range(1, int(input("Input Array Length :"))))
#array = [-4, -2, 5, 6, 8, 10, 14]


def search(num):
    start = 0
    end = len(array)
    while True:
        mid = (start + end) // 2
        if(array[mid] == num):
            print("found at index "+str(mid))
            break
        elif(array[mid] < num):
            start = mid
        elif(array[mid] > num):
            end = mid
        if(start == end-1 and array[0] != num):
            print("element not present in array")
            break


search(int(input("Search :")))
