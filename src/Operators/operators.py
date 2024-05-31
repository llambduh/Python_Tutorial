"""Operator Types Examples
Operators are special symbols or keywords that are 
used to perform operations on variables and values.
"""

"""Arithmetic operators
used to perform basic arithmetic operations.
"""
add = 10 + 5
subtract = 10 - 5
multiply = 10 * 5
divide = 10 / 5
modulo = 10 % 3 # return the remainder
power = 10 ** 2
floor_division = 10 // 3 # rounds the result down to the nearest whole number


"""Comparison operators
compare two values and return 
a boolean result (True or False).
"""
a = 10
b = 5
print(a == b)  # Is Equal To
print(a != b)  # Not Equal To
print(a > b)   # Greater Than
print(a < b)   # Less Than
print(a >= b)  # Greater Than or Equal To
print(a <= b)  # Less Than or Equal To


"""Logical operators
symbols or words that connect two or more 
expressions to produce a compound expression
"""
a = True
b = False
print(a and b)  # Returns True if both statements are true
print(a or b)   # Returns True if one of the statements is true
print(not a)    # Reverse the result, returns False if the result is true


"""Assignment operators
assigns a value to a variable or property 
based on the value of another operand.
"""
a = 10
a += 5  # a = a + 5
a -= 3  # a = a - 3
a *= 2  # a = a * 2
a /= 4  # a = a / 4
a %= 6  # a = a % 6
a **= 7 # a = a ** 7


"""Bitwise operators
operates on a bit string, a bit array or a binary numeral at the 
level of its individual bits. It is a fast and simple action, 
basic to the higher-level arithmetic operations and directly 
supported by the processor.
"""
a = 12  # 1100 in binary
b = 10  # 1010 in binary
print(a & b)  # Bitwise AND
print(a | b)  # Bitwise OR
print(a ^ b)  # Bitwise XOR
print(~a)     # Bitwise NOT
print(a << 2) # Bitwise LEFT SHIFT
print(a >> 2) # Bitwise RIGHT SHIFT


"""Identity operators
Identity operators allow you to determine if 
two variables or objects reference the 
same memory location. 
"""
x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
print(x1 is not y1)  # prints False
print(x2 is y2)  # prints True


"""Membership operators
used to check if a value is part of a sequence, 
such as a string, list, tuple, or set
"""
message = 'Hello world'
print('world' in message)  # check if 'world' is present in message string
print('hello' not in message)  # check if 'hello' is not present in message string
