"""Strings
a sequence of characters and can contain letters, numbers, symbols and even spaces. 
It must be enclosed in quotation marks for it to be recognized as a string.
"""

# Create String variables
name = "Llambduh" # Create a string using double quotes
first_name = 'John' # Create a string using single quotes
multiline_string = """
You can create multiline strings
with both single and double quotes.
Does this look familiar? 
I won't 'comment'.
"""


# Iterate through a String
for letter in name:
    print(letter)


# String slicing and indexing
first_str = "Hello, World!"
print(first_str[0])     # 'H'
print(first_str[7:12])  # 'World'
print(first_str[-1])    # '!'


# String formatting
age = 32
print('Hello, ' + name) # Concatenation using the '+" operator
print("Name:", name, "Age:", age) # Using Comma-Separated Values to print variables

# f-strings (formatted string literals)
print(f"Name: {name}, Age: {age}")  # Literal prefix f tells Python to restore the value of two string variable name and age inside braces {}

# String format method
txt1 = "My name is {name}, I'm {age}\n".format(name = "John", age = 32) # format(p0, p1, ..., k0=v0, k1=v1, ...)
txt2 = "My name is {0}, I'm {1}\n".format("John", 32) # p0, p1 are positional arguments and, k0, k1 are keyword arguments with values v0, v1 respectively.
txt3 = "My name is {}, I'm {}\n".format("John", 32) # format() returns the formatted string.
txt4 = "I'm {1}, and my name is {0}\n".format("John", 32)
print("The number is:{:d}".format(156147)) # integer arguments
print("The float number is:{:f}".format(178165.5147)) # float arguments
print("bin: {0:b}, oct: {0:o}, hex: {0:x}".format(22)) # octal, binary and hexadecimal format
print("{:5d}".format(32)) # integer numbers with minimum width
print("{:2d}".format(1234)) # width doesn't work for numbers longer than padding
print("{:8.3f}".format(12.2346)) # padding for float numbers
print("{:05d}".format(12)) # integer numbers with minimum width filled with zeros
print("{:08.3f}".format(12.2346)) # padding for float numbers filled with zeros

# String formatting with % Operator
print("Hello, %s!" % name) # %s: Strings
print("Age: %d" % age) # %d: Decimal integers (base-10).

pi = 3.141592653589793
print("Pi: %f" % pi) # %f: Floating point numbers. 
print("Pi: %.2f" % pi) # %.<num_digits>f: Floating point numbers with a fixed number of digits.

number = 255
print("Hex: %x" % number)  # %x: Integers in hexadecimal representation (lowercase).
print("Hex: %X" % number)  # %X: Integers in hexadecimal representation (uppercase).
print("Octal: %o" % number)  # %o: Integers in octal representation.
print("Unsigned: %u" % number)  # %u: Unsigned decimal integer.

char = 65
print("Character: %c" % char) # %c: Single character. Output: Character: A

print("Discount: 50%%") # %%: A literal % character. Output: Discount: 50%

number = 123
print("Number: %5d" % number) # Output: Number: 123 (padded with spaces)
print("Number: %-5d" % number) # Output: Number: 123  (left-justified)

pi = 3.141592653589793
print("Pi: %.4f" % pi) # Output: Pi: 3.1416 (4 digits after the decimal)
print("Pi: %8.4f" % pi) # Output: Pi: 3.1416 (minimum width 8, padded with spaces)

text = "Hello, world!"
print("%.5s" % text) # Output: Hello (first 5 characters)
print("%10.5s" % text) # Output: Hello (first 5 characters, minimum width 10)


# Escape sequences
new_line = "Hello\nWorld"
carriage_return = "Hello\rWorld"
backslash = "Hello\\World"
single_quote = 'It\'s a test'
double_quote = "She said \"Hello\""
backspace = "Hello\bWorld"
tab = "Hello\tWorld"
vertical_tab = "This is a vertical tab: \vVertical Tab"
formfeed = "Hello\fWorld"
octal_value = "\101"  # 'A'
hex_value = "\x41"    # 'A'
bell = "This is an bell: \a"
unicode_16bit = "This is a Unicode character with 16-bit hex value 03B1: \u03B1"
unicode_32bit = "This is a Unicode character with 32-bit hex value 0001F600: \U0001F600"
char_8bit_hex = "This is a character with 8-bit hex value 41: \x41"
raw_string = r"This is a raw string: \n will not be interpreted as a newline"


# String functions
string_value = str(123) # str(Number): Converts the number 123 to a string
text_input = input("Enter something: ") # input(String): Prompts the user for input and returns it as a string
length = len("hello") # len("hello"): Returns the length of the string
result = eval("len('hello')") # eval(String): Evaluates the string expression, result == 5
repr_value = repr("hello") # repr(String): Returns a string representation of the string
ascii_string = ascii("helloäöü") # ascii(String): Returns a string with non-ASCII characters escaped
char = chr(97) # chr(Integer): Returns the string representing the character 'a'
unicode_point = ord('a') # ord(String): Returns the Unicode code point of 'a'
byte_text = bytes("hello", 'utf-8') # bytes(String, Encoding): Converts the string to bytes
bytearray_text = bytearray("hello", 'utf-8') # bytearray(String, Encoding): Converts the string to bytearray


# String methods
text = "hello, World!"
print(text.capitalize()) # capitalize() - Capitalizes the first character of the string.
print(text.casefold()) # casefold() - Converts the string to lowercase for caseless matching.
print(text.center(20, '*')) # center(width, fillchar) - Centers the string with the specified width, padded with fillchar.
print(text.count('o')) # count(substring) - Returns the number of non-overlapping occurrences of the substring.
print(text.encode('utf-8')) # encode(encoding, errors) - Encodes the string using the specified encoding.
print(text.endswith('!')) # endswith(suffix) - Returns True if the string ends with the specified suffix.
print(text.find('World')) # find(substring) - Returns the lowest index of the substring, or -1 if not found.
print(text.rfind('o')) # rfind(sub[, start[, end]]) - Return the highest index in where the substring is found
print(text.rfind('l', 6, -1))
print(text.index('World')) # index(substring) - Returns the lowest index of the substring, raises ValueError if not found. 
print(text.rindex('o')) # rindex(sub[, start[, end]]) - Return the highest index in where the substring is found
print(text.rindex('l', 6, -1)) # index and rindex raises a ValueError if the substring is not found, while find and rfind returns -1.
print(text.isalpha()) # isalpha() - Returns True if all characters in the string are alphabetic.
print(text.isascii()) # isascii() - Returns True if all characters in the string are ASCII.
print(text.isupper()) # isupper() - Returns True if all characters in the string are uppercase.
print(text.islower()) # islower() - Returns True if all characters in the string are lowercase.
print(text.isprintable()) # isprintable() - Returns True if all characters in the string are printable.
print(text.istitle()) # istitle() - Returns True if the string is titlecased.
print(text.replace('World', 'Llambduh')) # replace(old, new [, count]) - replaces each matching occurrence of a substring with another string
print(text.replace('l', 'k', 1)) # Replaces only the first l
print(text.swapcase()) # swapcase() - Converts all the characters to their opposite letter case
print(text.zfill(5)) # zfill(width) - Returns a copy of the string with 0 filled to the left based, it's size depends on the width. 

numeric_text = "12345"
print(numeric_text.isdecimal()) # isdecimal() - Returns True if all characters in the string are decimal characters.
print(numeric_text.isdigit()) # isdigit() - Returns True if all characters in the string are digits.
print(numeric_text.isnumeric()) # isnumeric() - Returns True if all characters in the string are numeric.

alphanumeric_text = "HelloWorld123"
print(alphanumeric_text.isalnum()) # isalnum() - Returns True if all characters in the string are alphanumeric.

identifier_text = "hello_world" # An identifier starts with a letter or underscore, followed by letters, digits, or underscores, and cannot be a reserved word.
print(identifier_text.isidentifier())  # isidentifier() - Returns True if the string is a valid identifier.

space_text = "   "
print(space_text.isspace()) # isspace() - Returns True if all characters in the string are whitespace.

tabbed_text = "Hello\tWorld"
print(tabbed_text.expandtabs(4)) # expandtabs(tabsize) - Expands tabs in the string to multiple spaces, default tabsize is 8.

al = 'abc'
num = '123'
alnum = al.join(num) # join(iterable) - Returns a string by joining all the elements of an iterable (list, string, tuple), separated by the given separator.

alnum.ljust(5) # ljust(width, fillchar(optional)) - returns the left-justified string within the given minimum width.
alnum.ljust(5, '*') # If fillchar is defined, it also fills the remaining space with the defined character.
alnum.rjust(6) # rjust(width, fillchar(optional)) - returns the right-justified string within the given minimum width.
alnum.rjust(6, '<') # If fillchar is defined, it also fills the remaining space with the defined character.

alnum.strip() # strip([chars](optional)) - removes any leading and trailing whitespaces from a given string
alnum.strip('a') # char specifies the set of characters to be removed from both the left and right parts of a string
alnum.lstrip() # string.lstrip([chars](optional)) - removes characters from the left based on the argument
alnum.lstrip('b') # char specifies the set of characters to be removed from the left part of a string
alnum.rstrip() # string.rstrip([chars](optional)) - removes characters from the right based on the argument
alnum.rstrip('c') # char specifies the set of characters to be removed from the right part of a string

# Strings are Immutable
friends_name = 'Joe'
friends_name[0] = 'M' # TypeError: 'str' object does not support item assignment

