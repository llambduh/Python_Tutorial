"""Strings
a sequence of characters and can contain letters, numbers, symbols and even spaces. 
It must be enclosed in quotation marks for it to be recognized as a string.
"""

# String Formatting options
# Review of basics
name = "Llambduh"
age = 32
print('Hello, ' + name) # Concatenation using the '+" operator
print("Name:", name, "Age:", age) # Using Comma-Separated Values to print variables

# String Formatting with % Operator
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
print("Number: %5d" % number)      # Output: Number: 123 (padded with spaces)
print("Number: %-5d" % number)     # Output: Number: 123  (left-justified)

pi = 3.141592653589793
print("Pi: %.4f" % pi)             # Output: Pi: 3.1416 (4 digits after the decimal)
print("Pi: %8.4f" % pi)            # Output: Pi: 3.1416 (minimum width 8, padded with spaces)

text = "Hello, world!"
print("%.5s" % text)               # Output: Hello (first 5 characters)
print("%10.5s" % text)             # Output: Hello (first 5 characters, minimum width 10)

# String format method
txt1 = "My name is {name}, I'm {age}\n".format(name = "John", age = 32)
txt2 = "My name is {0}, I'm {1}\n".format("John", 32)
txt3 = "My name is {}, I'm {}\n".format("John", 32)
txt4 = "I'm {1}, and my name is {0}\n".format("John", 32)
print("Print multiple lines:\n", txt1, txt2, txt3, txt4) # Print multiple variables on one line

#  f-strings (formatted string literals)
name = "Alice"
age = 30
print(f"Name: {name}, Age: {age}")  # Output: Name: Alice, Age: 30


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


# String methods
text = "Hello, World!"
print(text.capitalize())  # capitalize() - Capitalizes the first character of the string.
print(text.casefold())  # casefold() - Converts the string to lowercase for caseless matching.
print(text.center(20, '*'))  # center(width, fillchar) - Centers the string with the specified width, padded with fillchar.
print(text.count('o'))  # count(substring) - Returns the number of non-overlapping occurrences of the substring.
print(text.encode('utf-8'))  # encode(encoding, errors) - Encodes the string using the specified encoding.
print(text.endswith('!'))  # endswith(suffix) - Returns True if the string ends with the specified suffix.
print(text.find('World'))  # find(substring) - Returns the lowest index of the substring, or -1 if not found.
print(text.index('World'))  # index(substring) - Returns the lowest index of the substring, raises ValueError if not found.
print(text.isalpha())  # isalpha() - Returns True if all characters in the string are alphabetic.
print(text.isascii())  # isascii() - Returns True if all characters in the string are ASCII.
print(text.islower())  # islower() - Returns True if all characters in the string are lowercase.
print(text.isprintable())  # isprintable() - Returns True if all characters in the string are printable.
print(text.istitle())  # istitle() - Returns True if the string is titlecased.

numeric_text = "12345"
print(numeric_text.isdecimal())  # isdecimal() - Returns True if all characters in the string are decimal characters.
print(numeric_text.isdigit())  # isdigit() - Returns True if all characters in the string are digits.
print(numeric_text.isnumeric())  # isnumeric() - Returns True if all characters in the string are numeric.

tabbed_text = "Hello\tWorld"
print(tabbed_text.expandtabs(4))  # expandtabs(tabsize) - Expands tabs in the string to multiple spaces, default tabsize is 8.

alphanumeric_text = "HelloWorld123"
print(alphanumeric_text.isalnum())  # isalnum() - Returns True if all characters in the string are alphanumeric.

identifier_text = "hello_world" # An identifier starts with a letter or underscore, followed by letters, digits, or underscores, and cannot be a reserved word.
print(identifier_text.isidentifier())  # isidentifier() - Returns True if the string is a valid identifier.

space_text = "   "
print(space_text.isspace())  # isspace() - Returns True if all characters in the string are whitespace.


# String slicing and indexing
s = "Hello, World!"
print(s[0])     # 'H'
print(s[7:12])  # 'World'
print(s[-1])    # '!'
