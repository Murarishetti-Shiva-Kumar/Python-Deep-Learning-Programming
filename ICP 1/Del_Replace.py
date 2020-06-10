"""
Input the string “Python” as a list of characters from console,
delete at least 2 characters,
reverse the resultant string and print it
"""

# importing randint class from random package
from random import randint


# Defining function to perform deleting the characters and then reverse the remaining string
def proc_word(word):
    new_word = ""
    for x in range(0, int(no_delete)):  # iterates for the number of characters to be deleted
        pos = randint(0, len(word) - 1)
        new_word += word[pos]  # storing the deleted characters
        word = word[:pos] + word[pos + 1:]  # removing the deleted characters using the range from the string
    print(f'The {no_delete} characters deleted are:', new_word)
    print(f'After deleting the {no_delete} characters, newly formed word is:', word)
    print('After Reversing the remaining characters newly formed string is:', word[::-1])  # Reversing the remaining characters in the string


word = input("Enter the word to be processed:")  # user enters the word
no_delete = input("Number of Characters to be deleted from the string randomly: ")  # user enters the number of characters to be deleted
print('The word you have entered is:', word)
proc_word(word)
