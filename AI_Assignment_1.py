import numpy as np


class Stack(object):
    def __init__(self):
        self.items = []
        self.item_count = 0

    def __str__(self):
        if self.item_count == 0:
            return 'Your STACK is empty'
        else:
            return self.items

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)
        self.item_count += 1

    def pop(self):
        self.item_count -= 1
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


class Visited(object):
    def __init__(self):
        self.items = []

    def __str__(self):
        if len(self.items) == 0:
            return "You haven't visited any state yet"
        else:
            return self.items


class Frontier(object):
    def __init__(self):
        self.temp = Stack()

    def __str__(self):
        if self.temp.is_empty():
            return 'Frontier is Empty'
        else:
            return self.temp

    def push_to_frontier(self, item):
        self.temp.push(item)

    def pop_from_frontier(self):
        self.temp.pop()


def print_cube(x):
    print("             ",x[0,0:3])
    print("             ",x[1,0:3])
    print("             ",x[2,0:3])
    print(x[3,0:3],x[6,0:3],x[9,0:3],x[12,0:3])
    print(x[4,0:3],x[7,0:3],x[10,0:3],x[13,0:3])
    print(x[5,0:3],x[8,0:3],x[11,0:3],x[14,0:3])
    print("             ",x[15,0:3]," "," "," ")
    print("             ",x[16,0:3]," "," "," ")
    print("             ",x[17,0:3]," "," "," ")


def front_cw(x): # action 1
    x[6:9,0:3]=np.fliplr(x[6:9,0:3].transpose())
    temp1=np.array(x[2, 0:3])
    temp2=np.array(x [9:12,0])
    temp3=np.array(x[15,0:3])
    temp4=np.array(x[3:6,2])
    x[2, 0:3]=np.fliplr([temp4])[0]
    x[9:12,0]=temp1
    x[15,0:3]=np.fliplr([temp2])[0]
    x[3:6,2]=temp3


def up_cw(x): # action 3
    x[0:3,0:3]=np.fliplr(x[0:3,0:3].transpose())
    temp1=np.array(x[12, 0:3])
    temp2=np.array(x [9,0:3])
    temp3=np.array(x[6,0:3])
    temp4=np.array(x[3,0:3])
    x[12, 0:3]=temp4
    x[9,0:3]=temp1
    x[6,0:3]=temp2
    x[3,0:3]=temp3


def down_cw(x):# action 5 Front down clock wise
    x[15:18,0:3]=np.fliplr(x[15:18,0:3].transpose())
    temp1=np.array(x[8, 0:3])
    temp2=np.array(x [11,0:3])
    temp3=np.array(x[14,0:3])
    temp4=np.array(x[5,0:3])
    x[8, 0:3]=temp4
    x[11,0:3]=temp1
    x[14,0:3]=temp2
    x[5,0:3]=temp3


rubik_cube_file = open('input.txt')
rubik_cube_file = rubik_cube_file.read()

temp = rubik_cube_file
# temp = np.array(rubik_cube_file)
np_arr = np.array(
    [
        ['A', 'A', 'A'],
        ['A', 'A', 'A'],
        ['A', 'A', 'A'],
        ['A', 'A', 'A'],
        ['A', 'A', 'A'],
        ['A', 'A', 'A'],
        ['A', 'A', 'A'],
        ['A', 'A', 'A'],
        ['A', 'A', 'A'],
        ['A', 'A', 'A'],
        ['A', 'A', 'A'],
        ['A', 'A', 'A'],
        ['A', 'A', 'A'],
        ['A', 'A', 'A'],
        ['A', 'A', 'A'],
        ['A', 'A', 'A'],
        ['A', 'A', 'A'],
        ['A', 'A', 'A']

    ]
)
x_n = 0
y_n = 0



for i in range(0, 348):
    # vempo = temp[i]
    if temp[i] in [chr(x) for x in range(ord('A'), ord('Z') + 1)]:
        # vempo = temp[i]
        if y_n < 3:
            # vempo = temp[i]
            np_arr[x_n, y_n] = temp[i]
            y_n += 1
        else:
            # vempo = temp[i]
            y_n = 0
            x_n += 1
            np_arr[x_n, y_n] = temp[i]
            y_n += 1
    # print(i, ' index: ', temp[i])
# print_cube(np_arr)
# print('SPACESSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS')
# front_cw(np_arr)
# print_cube(np_arr)