"""Conditional statements
statements where a hypothesis is followed by a conclusion.
"""

# if, elif, else statements
age = 18
if age < 18:
    print("Minor")
elif age >= 21:
    print("Just became an adult")
else:
    print("Adult")


# Nested conditons
num = 10
if num > 0:
    if num < 20:
        print("Number is positive and less than 20")
        