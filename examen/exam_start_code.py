
def exercise1(array2D):
    sum = 0
    for sub_arr in array2D:
        for nr in sub_arr:
            sum += nr
    return sum 


def exercise2():
    result = []
    for i in range(1,21):
        result.append(i**2)
    print(result)
    


def exercise3(x, y, z):
    if x == y or y == z or x == z:
        return 0
    else:
        return x + y + z


def exercise4(array1, array2):
    result = [0] * len(array1)
    for i in range(len(array1)):
        result[i] = array1[i] + array2[i]
    return result
    


def exercise5(array):
    result = []
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] % 3 == 0:
                result.append((i,j))
    return result

    
array = [[1, 3, 1, 1, 4],
         [2, 4, 3, 1, 2],
         [3, 5, 4, 1, 1],
         [4, 6, 2, 1, 4]]



arr_ex_1 = [ [1, 2, 3], [4, 5]]
print(exercise1(arr_ex_1))
print("=======================================================")
exercise2()
print("=======================================================")
x = y = 1
z = 2
print(exercise3(x,y,z))
x = 1
y = 2
z = 3
print(exercise3(x,y,z))
print("=======================================================")
array1 = [1, 2, 3, 4]
array2 = [5, 6, 7, 8]
print(exercise4(array1, array2))
print("=======================================================")
print(exercise5(array))
