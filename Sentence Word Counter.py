# 1.8 Sentence Word Counter
# A word is defined as any sequence of characters separated by spaces. The program should read the sentence
# from the user and print the total number of words in it. Write a program that counts the number of words
# in a sentence entered by the user.
# Input Format
# A single line of input containing a sentence (string).
# Output Format
# Print a single integer — the total number of words in the given sentence.
# Sample Test Case 1
# Input
# I love programming in Python
# Output
# 5

# <....program....>

sentence = input()

words = sentence.split()

word_count = len(words)

print(word_count)