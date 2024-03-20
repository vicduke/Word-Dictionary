import json
import difflib

 #Load JSON data into a Python dictionary
with open('dictionary-data/data.json', 'r') as file:
    dictionary = json.load(file)

def checkword(word):
    if word in dictionary:
        return dictionary[word]
    else:
        # If the word is not found, suggest similar words
        suggestions = difflib.get_close_matches(word, dictionary.keys(), n=3, cutoff=0.6)
        if suggestions:
            return f"Word not found. Did you mean: {', '.join(suggestions)}?"
        else:
            return "Word not found."

word = input("Enter a word:")
word = word.lower()
definition = checkword(word)
print(definition)