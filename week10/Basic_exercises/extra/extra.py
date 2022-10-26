
for i in range(2000, 3201):
    if i % 7 == 0 and i % 5 != 0:
        print(i, end=',')



def square():
    square = []
    for i in range(1, 21):
        square.append(i ** 2)
    print(square)

square()


arr = [
       [ 12 , 12 , 12 , 13 ] ,
       [ 43 , 43 , 43 , 54 ] ,
       [ 44 , 44 , 44 , 23 ] ,
       [ 99 , 34 , 12 , 12 ] 
    ]


def calculate_sum(arr):
    sum = 0
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if i == 0 or i == len(arr) -1 or j == 0 or j == len(arr[0]) -1:
                sum += arr[i][j]
    return sum

print(calculate_sum(arr))

import itertools

my_list = [1, 2, 3, 4, 5, 6, 7, 8]

my_list = itertools.takewhile(lambda x: x < 5, my_list)

print(list(my_list))