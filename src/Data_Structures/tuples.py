"""Tuples
In mathematics, a tuple is an ordered sequence of values.
In Python a tuple is a collection similar to a list. 
Unlike lists Tuples are Immutable and cannot be 
modified after they're created.
"""

# Creating Tuples
numbers = (1, 2, 3) # Inside parentheses
single_element = (1,) # A single element tuple needs a comma after the element
coordinates = 1, 2, 3 # Without parentheses
nested_tuple = (1, (2, 3), 4) # Nested Tuples: Tuples can contain other tuples


# Accessing Elements
print(numbers[0]) # Access elements using indexing
print(numbers[-1]) # You can also use negative elements, this example gives you the last element in the tuple


# Tuple Unpacking
x, y, z = coordinates # You can assign elements of a tuple to multiple variables
print(x, y, z)


# Slicing Tuples
data = (1, 2, 3, 4)
print(data[1:3])  # [start:end]: You can slice tuples to get a range of elements
print(data[:2])   # Output: (1, 2)
print(data[2:])   # Output: (3, 4)
print(data[:])    # Returns a shallow copy of the tuple


# Iterate through a Tuple
for num in numbers: 
    print(num)


# Tuple Operations
first_tuple = (1, 2)
second_tuple = (3, 4)
combined_tuple = first_tuple + second_tuple  # Concatenation using the + operator
repeat_tuple = (1, 2) * 3  # Repetition using the * operator i.e. (1, 2, 1, 2, 1, 2)


# Tuple Functions
print(len(repeat_tuple))  # len(tuple): returns the length of the tuple
print(first_tuple.count(2))  # count(value): Counts the number of occurrences of a specified value
print(second_tuple.index(4))  # index(value): Finds the first occurrence of a specified value and returns its index
zipped_list = zip(first_tuple, second_tuple)  # zip(tuple, tuple): Combines two sequences into an iterator 


# Converting Tuples
list_of_numbers = [1, 2, 3]
tuple_of_numbers = tuple(list_of_numbers) # tuple(sequence): You can convert other sequences to tuple
back_to_list = list(tuple_of_numbers) # You can also convert tuples to other kinds of sequences 
