# <!-- 1.9 Average Word Length Calculator
# A word is defined as any sequence of characters separated by spaces.
# The average word length is calculated by dividing the total number of characters in all words by the number
# of words in the sentence.
# Write a program that calculates the average word length in a sentence entered by the user.
# Note: Ignore spaces when counting characters.
# Input Format
# A single line of input containing a sentence (string).
# Output Format
# Print the average word length as a floating-point number (you may round it to 2 decimal places).
# Sample Test Case 1
# Input
# I love programming
# Output
# 5.33
# Explanation: Word lengths = [1, 4, 11]; Total = 16; Average = 16 / 3 = 5.33

# <....Program....> -->

def average_word_length(sentence: str) -> float:
    # Split sentence into words
    words = sentence.split()
    
    # Calculate total characters (ignoring spaces)
    total_chars = sum(len(word) for word in words)
    
    # Calculate average
    average = total_chars / len(words)
    
    # Round to 2 decimal places
    return round(average, 2)

# Input from user
sentence = input().strip()
print(average_word_length(sentence))