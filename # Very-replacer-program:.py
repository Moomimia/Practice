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
replacements = {
    "noicy": "deafening",
    "cold": "freezing",
    "hot": "scorching",
    "big": "enormous",
    "small": "tiny",
    "good": "excellent",
    "bad": "terrible",
    "happy": "ecstatic",
    "sad": "devastated",
    "tired": "exhausted",
    "hungry": "starving",
    "thirsty": "parched",
    "expensive": "outrageous",
    "cheap": "bargain",
    "fast": "blazing",
    "slow": "glacial",
    "many": "plentiful",
    "strong": "powerful",
    "weak": "feeble",
    "easy": "simple",
    "difficult": "challenging",
    "dangerous": "hazardous",
    "safe": "secure",
    "clean": "spotless",
    "aggressively": "savagely",
    "dirty": "filthy",
    "nice": "lovely",
    "ugly": "hideous",
    "beautiful": "gorgeous",
    "handsome": "handsome",
    "funny": "hilarious",
    "boring": "tedious",
    "interesting": "intriguing",
    "important": "critical",
    "unimportant": "trivial",
    "short": "brief",
    "long": "endless",
    "old": "ancient",
    "young": "juvenile",
    "fat": "obese",
    "thin": "emaciated",
    "rich": "wealthy",
    "poor": "destitute",
    "smart": "clever",
    "kind": "generous",
    "cruel": "cruel",
    "polite": "courteous",
    "rude": "rude",
    "friendly": "affable",
    "unfriendly": "antagonistic",
    "clever": "ingenious",
    "stupid": "dull",
    "brave": "courageous",
    "cowardly": "cowardly",
    "calm": "tranquil",
    "nervous": "nervous",
    "quiet": "silent",
    "noisy": "deafening",
    "dark": "pitch black",
    "light": "bright",
    "little": "barely any",
    "significant": "significant",
    "very": "",
}
#print(my_dict)

#3. Replacing the word "very" with its corresponding replacement
# To replace the word "very" with its corresponding replacement, you can split the text into split_text, iterate over each word, and replace it with its replacement if it is in the dictionary.
# Keysplit_text: Python string split, Python for loop, Python if-else statement, .split(),  .lower(), .rstrip()
# NOTE: there is many many ways to do this. No one correct answer.

split_text = text.split(" ")
print(split_text)

# Replace the word "very ..." with "..."
for i in range(len(split_text)):
    if split_text[i].lower().rstrip() in replacements:
        split_text[i] = replacements[split_text[i].lower().rstrip()]
print(split_text)
new_text = " ".join(split_text)
print(new_text)



