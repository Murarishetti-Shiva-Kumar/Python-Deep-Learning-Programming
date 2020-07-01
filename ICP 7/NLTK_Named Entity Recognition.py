#importing nltk(Natural Language Toolkit)
import nltk

#Downloading Package punkt
nltk.download('punkt')

#opening file in read mode
file = open('input.txt', 'r')

#Reading the data in the file
input = file.read()


"""
Named entity recognition is the subtask of information extraction that seeks to locate and classify elements in text into pre-defined categories such as the names of the person, organizations, locations, expressions of times, quantities, etc.
"""

#Importing required packages
from nltk.tokenize import wordpunct_tokenize
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk import ne_chunk

#Downloading required packages
nltk.download('maxent_ne_chunker')
nltk.download('words')

print("Named Entity Recognition:")
ne_tree=ne_chunk(pos_tag(wordpunct_tokenize(input)))
print(ne_tree)