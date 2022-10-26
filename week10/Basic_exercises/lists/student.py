# Exercise 1
# Create a list named food with two elements "rice" and "beans".
l = ["rice", "beans"]

# Exercise 2
# Append the string "broccoli" to the food list using .append()
l.append("broccoli")

# Exercise 3
# Add the strings "bread" and "pizza" to food using .extend()
l.extend(["bread", "pizza"])

# Exercise 4
# Print the first two items in food using slicing notation
print(l[:3])
# NOTE: The following is also acceptable


# Exercise 5
# Print the last item in food using index notation
print(l[-1])

# Exercise 6
# Create a list called breakfast from the string "eggs, fruit, orange juice"
breakfast = list("eggs, fruit, orange juice".split(','))

# Exercise 7
# Verify that breakfast has three items using len()
print(len(breakfast))

# Exercise 8
# Create a new list called `lengths` using a list
# comprehension that contains the lengths of each
# string in the `breakfast` list.
lengths =  [len(s) for s in breakfast]
print(lengths)