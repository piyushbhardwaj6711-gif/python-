# -----------------------------------
# Python Basics: Strings and Conditions
# Author: Piyush Bhardwaj
# -----------------------------------

# Strings
# We can create strings using single quotes, double quotes, or triple quotes.

message = "My name is Piyush.\nI am a good boy."
print(message)

# Escape Sequence Characters
# \n is used for a new line
# \t is used for tab space

tab_example = "Piyush\tBhardwaj"
print(tab_example)

# String Concatenation
# Joining two strings is called concatenation.

first_part = "My name is Piyush. "
second_part = "I am a good boy."

full_sentence = first_part + second_part
print(full_sentence)

# Length of a String

name = "Piyush"
print("Length of name:", len(name))

# Indexing
# Indexing is used to access a single character from a string.

word = "Apna"
print("Character at index 2:", word[2])

# Slicing
# Slicing is used to get a part of a string.

sentence = "My name is Piyush"
print("Sliced text:", sentence[1:7])

# Negative Slicing

name = "Piyush"
print("Negative sliced text:", name[-5:-3])

# -----------------------------------
# Conditional Statements
# if, elif, else
# -----------------------------------

num = 5

if num > 8:
    print("Your number is greater than 8")
elif num > 2:
    print("Perfect")
else:
    print("Your number is 2 or less")

# Driving Eligibility Example

age = int(input("Enter your age: "))

if age >= 18:
    print("You can drive")
else:
    print("You cannot drive")

# Nested If Statement
# Nested if means using one if statement inside another if statement.

age = int(input("Enter your age again: "))

if age >= 18:
    if age >= 90:
        print("You cannot drive")
    else:
        print("You can drive")
else:
    print("You cannot drive")

# Simple If-Else Example

a = 22

if a > 9:
    print("Greater")
else:
    print("Lesser")