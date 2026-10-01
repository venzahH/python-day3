"""
Author: Venzah Hamilton
Date: June 18, 2025
Summary: When ran, this code will take arguments of varying numbers and data structures and print them out, skipping
any integers
"""

"""
Function name: skip_integers
Arguments: Takes any number of arguments of any/variable type(s)
Returns: None
Summary: This function will loop through all the arguments passed into the function and will only print out values
that are not integers
"""
def skip_integers(*args):
    for value in args:
        if type(value) is int:
            continue
        else:
            print(value)


# Test you code here
print("--- Test 1 ---")
skip_integers(3, 5.2, "value", 6.0)

print("\n--- Test 2 ---")
skip_integers(3, 5.2, "value", 6.0, 0, 90, True, "0")

print("\n--- Test 3 ---")
skip_integers()

print("\n--- Test 4 ---")
skip_integers(True)

print("\n--- Test 3 ---")
skip_integers([12], -2, 109.0, False, 38, -0.0, -0, 0, {"number": 19}, -910, 12, -0.3, ("char"))