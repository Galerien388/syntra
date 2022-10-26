
# Exercise 1
# Create an empty dictionary
map = dict()


# Exercise 2
# Add some key-value pairs to the dictionary
map["vrt"] = 1
map["vtm"] = 2


# Exercise 3
# Check if "Enterprise" and "Discovery" exist; if not, add them
enterprise = map.get("Enterprise", None)
if not enterprise:
    map["Enterprise"] = 3
discovery = map.get("Discovery", None)
if not discovery:
    map["Discovery"] = 4


# Bonus points: you could instead loop over a list of names to check
for k,v in map.items():
    if k == "Enterprise" or k == "Discovery":
        print(k, " = ", v)



# Exercise 4
# Display the contents of the dictionary, one pair at a time
for k,v in map.items():
    print(k, ": ", v)


# Exercise 5
# Remove "Discovery"
del map["Discovery"]

# Exercise 6 (Bonus)
# Create dictionary by passing a list to dict()
list_to_map = dict([('vrt', 1), ('vtm', 2), ('discovery', 3)])

print(list_to_map)