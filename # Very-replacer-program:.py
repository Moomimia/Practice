# Very-replacer-program: 
# 1. Reading the English essayÖ To read the English essay from a .txt file, you can use the open() function to open the file and the read() method to read its contents.
# Keysplit_text: Python open file, Python read file.

file = open('words.txt', 'r')
text = file.read()
#print(text)

# 2. Defining the replacements
# To define the replacements for the word "very", you can use a dictionary that maps the word to its replacement. 
# Keysplit_text: Python dictionary, Python mapping

# Using curly braces
my_dict = {'very calm': 'patient', 'very big': 'huge', 'very little': 'tiny'}
#print(my_dict)

#3. Replacing the word "very" with its corresponding replacement
# To replace the word "very" with its corresponding replacement, you can split the text into split_text, iterate over each word, and replace it with its replacement if it is in the dictionary.
# Keysplit_text: Python string split, Python for loop, Python if-else statement, .split(),  .lower(), .rstrip()
# NOTE: there is many many ways to do this. No one correct answer.

split_text = text.split(" ")
# print(split_text)

# Replace the word "very ..." with "..."
for i in range(len(split_text)):
    if split_text[i] == "calm":
        split_text[i] = "patient"

    if split_text[i] == "big":
        split_text[i] = "huge"

    if split_text[i] == "little":
        split_text[i] = "tiny"
    
    if split_text[i] == "very":
        split_text[i] = ""

new_text = " ".join(split_text)
print(new_text)



