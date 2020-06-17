"""
Write a simple program that parse a Wiki page
mentioned below and follow the instructions:
https://en.wikipedia.org/wiki/Deep_learning
•	Print out the title of the page
•	Find all the links in the page (‘a’ tag)
•	Iterate over each tag(above) then return the link using attribute "href" using get
•	Save all the links in the file
"""

from bs4 import BeautifulSoup
import requests

html = requests.get("https://en.wikipedia.org/wiki/Deep_learning")
bsObj = BeautifulSoup(html.content, "html.parser")

# print(bsObj.title)
print(bsObj.title.string)  # Printing the title of the page

print(bsObj.find_all('a'))  # Finding all the links in the page (‘a’ tag)

file_write = open("output.txt", "w")

for links in bsObj.find_all('a'):  # Iterating over each tag
    ws = links.get('href')  # returning the links using attribute "href"
    # print(ws)
    if ws is not None:
        file_write.write(ws)  # writing into file
        file_write.write("\n")
