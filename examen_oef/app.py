a = [1,2,3]
b = [4,5,6]

def exercise1(array1, array2):
    c = []
    for i in range(0, len(array1)): 
        c.append(array1[i] + array2[i])
    return c

print(exercise1(a,b))

def exercise2():
    n = 5
    for i in range(5):
        for j in range(i):
            print('*', end=' ')
        print('')

    for i in range(5,0,-1):
        for j in range(i):
            print('*', end=' ')
        print('')

exercise2()

def exercise3():
    array = []
    for i in range (5,8):
        sArray = []
        for j in range(3):
            sArray.append(i)
        array.append(sArray)
    print(array)

exercise3()

def exercise4(array):
    result = []
    for i in range(1, len(array)):
        for j in range(0,len(array[i]) - 1):
            if array[i][j] == 'x' and array[i-1][j+1] == 1:
                result.append((i,j))
    return result


array = [[1, 0, 1, 1, 0],
         [0,'x','x',0,0],
         [1,0,1,1,'x'],
         [0,'x',0,1,0]
         ]
        
            
print(exercise4(array))

