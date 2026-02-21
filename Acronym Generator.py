# 1.6 Acronym Generator
# An acronym is a word formed by taking the first letters of the words in a phrase and making a new word
# from them. For example, RAM is an acronym for “random access memory.”
# Write a program that allows the user to enter a phrase, and then outputs the acronym for that phrase.
# Note: The acronym should be in all uppercase letters, even if the words in the phrase are not capitalized.
# Input Format
# A single line of input containing a phrase (string) made up of one or more words.
# Output Format
# Print a single word — the acronym formed by taking the first letter of each word in the phrase and
# converting it to uppercas

# <....Program....>

phrase = input()

words = phrase.split()

acronym = ""
for word in words:
    acronym += word[0].upper()

print(acronym)