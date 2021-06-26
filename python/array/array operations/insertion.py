array = [2,4,6,5,7,9]
def insert(pos,num):
    print(f'before {array}')
    array.append(None)
    for i in range(len(array)-1 , pos-1 , -1):
        array[i] = array [i-1]
    array[pos] = num
    print(f'after {array}')
position = int(input('specify the position of where you want to insert the element :'))
number = int(input(f'specify the number that you want to insert at index {position} :'))
insert(position,number)