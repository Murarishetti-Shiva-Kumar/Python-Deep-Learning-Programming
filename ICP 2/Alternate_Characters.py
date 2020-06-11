"""
Write a program that returns every other char of a given string starting with first using a function named “string_alternative”
Str = “Good evening”
Output: Go vnn
Note: You need to create a function named “string_alternative” for this program and call it from main function
"""


def string_alternative(str):
    print(str[::2])  # step of 2 to take alternate characters


if __name__ == '__main__':
    str = input("Enter the String to be processed:")
    string_alternative(str)
