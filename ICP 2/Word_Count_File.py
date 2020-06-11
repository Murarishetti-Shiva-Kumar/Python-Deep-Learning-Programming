"""
Write a python program to find the wordcount in a file for each line and then print the output. Finally store the output back to the file.
Input: a file includes two line
    Python Course
    Deep Learning Course
Output:
    Python: 1
    Course: 2
    Deep: 1
    Learning: 1
Note: Your program should work for any number of lines
"""

# import json
d = dict()  # creating empty dictionary to store the words and there count values

file1 = open("Input.txt", 'r')  # Reading the input file
lines = file1.readlines()  # read all lines in the list

# print(lines)
for line in lines:
    line = line.strip()  # Remove each line with \n as new line with strip()
    # print("line:", line)
    words = line.split(" ")  # Divide line into words based on " "
    # print("words:", words)
    for word in words:  # for each word in the line
        if word in d:  # if already in the dictionary
            d[word] = d[word] + 1   # Increment count of word by 1
        else:
            d[word] = 1  # Add the word to dictionary with count 1

# Write the contents of dictionary
# print(d)
with open('Output.txt', 'w') as file:
    # file.write(json.dumps(d))
    file.write(str(d))
