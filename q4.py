"""
Task 1
    - Create a function that reverses a given string (s).
    - s must be a string.
    - Return the reversed string.
"""

def string_reverse(s):

    if not isinstance(s, str):
        return "Error: Input must be a string"

    return s[::-1]	# slicing trick to reverse


# Task 2 
# Invoke the function "string_reverse" using the following scenarios: 
# - "Hello World" 
# - "Python"

print(string_reverse("Hello World"))  # Output: "dlroW olleH"
print(string_reverse("Python"))       # Output: "nohtyP"