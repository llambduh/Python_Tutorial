"""Lists
a mutable ordered sequence of elements.
Ordered - They maintain the order of elements.
Mutable - Items can be changed after creation.
"""

# Creating lists
empty_list = []
string_list = ["A", "b", "cd", "EfG", "1"]
numbers_list = [1, 2, 3, 4, 5]
mixed_list = [1, "two", 3.0, True]
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # Also called a matrix
list1 = list(1, 2, 3) # list(): Creates a new list

# Creating lists with String methods
# split(separator(optional), maxsplit(optional)) - Breaks down a string into a list of substrings using a chosen separator
name_with_spaces = "L l a m b d u h"
fname = "John"
maybe_you_could = "Like, Share, Subscribe"
hashtags = "#youtube #new_video #python_course"
chars_in_name = name_with_spaces.split() # Whitespace is used as the default delimiter
fname_as_list = fname.split() # Splitting a string with no whitespace will return a new list of that one string
itd_be_nice = maybe_you_could.split(',')
hashtags_as_list = hashtags.split('#', 2)

# rsplit([separator [, maxsplit]]) - Breaks the string at the separator starting from the right and returns a list of strings
rchars_in_name = name_with_spaces.rsplit() # Whitespace is used as the default delimiter
rfname_as_list = fname.rsplit() # Splitting a string with no whitespace will return a new list of that one string
ritd_be_nice = maybe_you_could.rsplit(',')
rhashtags_as_list = hashtags.rsplit('#', 2)

# splitlines([keepends](optional)) - Splits the string at line breaks and returns a list
sentence = "I\nlove\rThis\r\nChannel"
grocery_list = '''Milk
Chicken
Bread
Butter'''
print(sentence.splitlines()) # splitlines works with 11 different escape sequences
print(grocery_list.splitlines()) # splitlines also works on multi-line strings
print(sentence.splitlines(True)) # The [keepends] param takes in either a boolean value or a number
print(sentence.splitlines(0)) # True and 0 both evaluate to True
print(sentence.splitlines(False)) # Any other positive or negative numbers indicate False
print(sentence.splitlines(8))

# List comprehension
squares = [x ** 2 for x in range(10)]
print(squares)

# List comprehension with conditions
even_squares = [x**2 for x in range(1, 6) if x % 2 == 0]
print(even_squares)


# Iterating over a list
for num in numbers:
    print(num)

# Iterating over nested lists (matrices)
for row in matrix:
    for num in row:
        print(num)

# Enumerate adds a counter to an iterable and returns it as an enumerate object.
for index, value in enumerate(squares):
    print(index, value)


# List Operations
list1 = [1, 2, 3]
list2 = [4, 5, 6]
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
first_element = list1[0] # Indexing ([]): Accesses elements by their index.
last_element = list1[-1] # Negative indexing
list1[0] = 10 # Changing values by index
nested_element = nested_list[1][2] # Accessing nested lists
sub_list = list1[1:3] # Slicing ([:]): Retrieves a subset of the list.
shallow_copy = list1[:] # An empty slice is used to create a shallow copy of a list or a sequence.
combined_list = list1 + list2  # Concatenation (+): Combines two lists into one.
repeated_list = list1 * 2  # Repetition (*): Repeats the elements of a list a given number of times.
exists = 2 in list1  # Membership (in, not in): Checks if an element is present in the list.
doesnt_exists = 4 not in list1 


# List Functions
numbers = [1, 2, 3, 4, 5]
length = len(numbers)  # len(iterable): Returns the length of an iterable
minimum = min(numbers)  # min(iterable): Returns the smallest item in an iterable
maximum = max(numbers)  # max(iterable): Returns the largest item in an iterable
total = sum(numbers)  # sum(iterable): Returns the sum of all items in an iterable
sorted_numbers = sorted(numbers)  # sorted(iterable, key=None, reverse=False): Returns a new sorted list from the items in iterable
reversed_numbers = list(reversed(numbers))  # reversed(iterable): Returns an iterator that accesses the given sequence in reverse order


# List Methods
list1 = list(1, 2, 3)
idx = list1.index(2) # index(item): Returns the index of the first occurrence of an item.
list_count = list1.count(2)  # count(item): Returns the number of occurrences of an item.
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
copy_list = list1.copy()  # copy(): Creates a shallow copy
list1.clear() # clear(): Removes all items from the list.
