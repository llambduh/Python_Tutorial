"""Lists
a mutable ordered sequence of elements.
Ordered - They maintain the order of elements.
Mutable - Items can be changed after creation.
"""

# Creating lists
empty_list = []
string_lists = ["A", "b", "cd", "EfG", "1"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "two", 3.0, True]
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


# Iterating over a list
for num in numbers:
    print(num)

# Iterating over nested lists (matrices)
for row in matrix:
    for num in row:
        print(num)

# Enumerate over a list
for index, mixed in enumerate(mixed):
    print(index, mixed)

# Zip multiple lists
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(name, age)

# List comprehension
squares = [x ** 2 for x in range(10)]
print(squares)


# List Operations
list1 = [1, 2, 3]
list2 = [4, 5, 6]
first_element = list1[0] # Indexing ([]): Accesses elements by their index.
sub_list = list1[1:3] # Slicing ([:]): Retrieves a subset of the list.
combined_list = list1 + list2  # Concatenation (+): Combines two lists into one.
repeated_list = list1 * 2  # Repetition (*): Repeats the elements of a list a given number of times.
exists = 2 in list1  # Membership (in, not in): Checks if an element is present in the list.
not_exists = 4 not in list1 


# List Methods
list1 = [1, 2, 3]
idx = list1.index(2) # index(item): Returns the index of the first occurrence of an item.
count = list1.count(2)  # count(item): Returns the number of occurrences of an item.
list1.append(4)  # append(item): Adds an item to the end of the list.
list1.extend([4, 5, 6])  # extend(iterable): Extends the list by appending elements from an iterable.
list1.insert(1, 1.5)  # insert(index, item): Inserts an item at a specified index.
list1.remove(2)  # remove(item): Removes the first occurrence of an item.
item = list1.pop()  # pop([index]): Removes and returns an item at a given index (or the last item if no index is specified).
item = list1.pop(0)  # Removes and returns the first item in the list
list1.reverse()  # reverse(): Reverses the elements of the list in place.
list1.sort()  # sort(key=Function(optional), reverse=True/False(optional)): Default sorts the list in place in acending order.
list1.sort(key=len) # Sorting elements in the list by their length
list1.sort(reverse=True)  # Sorting in Descending Order
list1.sort(key=len, reverse=True) # Sorting by Length in Descending Order
list1.clear() # clear(): Removes all items from the list.
