

def convert_cel_to_far(temp_cel):
    """Return the Celsius temperature temp_cel converted to Fahrenheit."""
    return temp_cel * 1.8 + 32
    

def convert_far_to_cel(temp_far):
    """Return the Fahrenheit temperature temp_far converted to Celsius."""
    return (temp_far - 32) / 1.8
    


# Prompt the user to input a Fahrenheit temperature.
    """write code here"""

temp_far = int(input("Geef een temp in Fahrenheit: "))

# Convert the temperature to Celsius.
# Note that `temp_far` must be converted to a `float`
# since `input()` returns a string.
"""write code here"""

convert_value = convert_far_to_cel(float(temp_far))

# Display the converted temperature
"""write code here"""

print(f"{convert_value:.2f}")

# You could also use `round()` instead of the formatting mini-language:
# print(f"{temp_far} degrees F = {round(temp_cel, 2)} degrees C"")
"""write code here"""

# Prompt the user to input a Celsius temperature.
"""write code here"""
temp_cel = float(input("Geef een temp in celius: "))
# Convert the temperature to Fahrenheit.
"""write code here"""
convert_value = convert_cel_to_far(temp_cel)
# Display the converted temperature
"""write code here"""
print(f"{convert_value}")