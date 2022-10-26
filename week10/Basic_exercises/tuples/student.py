# Exercise 1
# Create a tuple "cardinal_numbers" with "first", "second" and "third"

tup = ("first", "second", "third")

# Exercise 2
# Display the second object in the tuple
print(tup[1])

# Exercise 3
# unpack the tuple into three string and display them
first,second,third = tup
print(first, second, third)
# Exercise 4
# Create a tuple containing the letters of your name from a string
my_name = tuple('joel')

# Exercide 5
# Check whether or not x is in my_name
print(f"x is {'not' if 'x' not in my_name else ''} in my name")

# Exercise 6
# Create tuple containing all but the first letter in my_name
my_tuple_2 = tuple(my_name[1:])
print(my_tuple_2)