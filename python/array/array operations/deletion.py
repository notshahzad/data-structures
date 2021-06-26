array = [3,4,7,4,5,10,23]
def delete(pos):
    print(f'array before : {array}')
    for i in range(pos , len(array)-1):
        array [i] = array[i+1]
    array[len(array)] = None
    print(f'array after : {array}')
position = int(input('input index :'))
delete(position)