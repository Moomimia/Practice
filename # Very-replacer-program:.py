# Very-replacer-program: 
# 1. Reading the English essayÖ To read the English essay from a .txt file, you can use the open() function to open the file and the read() method to read its contents.
# Keywords: Python open file, Python read file.

file = open('words.txt', 'r')
text = file.read()
print(text)

# 2. Defining the replacements
# To define the replacements for the word "very", you can use a dictionary that maps the word to its replacement. 
# Keywords: Python dictionary, Python mapping

# Using curly braces
my_dict = {'very calm': 'patient', 'very big': 'huge', 'very little': 'tiny'}
print(my_dict)