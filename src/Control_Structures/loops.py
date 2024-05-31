"""Loops
a sequence of instructions that is continually 
repeated until a certain condition is reached.
"""

# while loops
i = 0
while i < 5:
    print(i)
    i += 1

# while loop with else
number = 10
while number <= 20:
    if number % 7 == 0:
        print("Found a number divisible by 7:", number)
        break
    number += 1
else:
    print("No number divisible by 7 found between 10 and 20")

# for loops
for j in range(5):
    print(j)

for i in range(1, 11):
    print("Number:", i)

# for loop with else
for number in range(1, 11):
    if number % 2 == 0:
        print("Found an even number:", number)
        break
else:
    print("No even number found between 1 and 10")


# break, continue, pass statements
for number in range(1, 11):
    if number <= 5:
        continue  # Skip numbers less than or equal to 5
    elif number > 8:
        pass  # Placeholder, does nothing
    else:
        print("Processing number:", number)

    if number > 5 and number <= 8:
        print("The first number greater than 5 is", number)
        break # Ends loop when this condition is met. 
    elif number > 8:
        print("Number greater than 8 found:", number)


# nested loops
rows = 5
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end="")
    print()
