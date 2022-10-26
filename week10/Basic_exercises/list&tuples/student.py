


# # Exercise 1
# # Create a tuple called data with two values, (1, 2) and (3, 4)
# data = ((1,2), (3,4))

# # Exercise 2
# # Loop over data and print the sum of each nested tuple
# for t in data:
#     print(t[0] + t[1])

# import itertools

# def add(a,b):
#     return a + b

# iets = itertools.starmap(add, data)
# print(list(iets))


# # Exercise 3
# # Create the list [4, 3, 2, 1] and assign it to variable numbers
# l = [4, 3, 2, 1]

# # Exercise 4
# # Create a copy of the number list using [:]
# l2 = l[:]

# # Exercise 5
# # Sort the numbers list in numerical order
# l2.sort()
# print(l2)


l3 = [1, 3, 4, 6, 8, 77]

it = iter(l3)
while a:= next(it, None):
    print(a)
