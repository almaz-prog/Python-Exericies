# 1.7 Name Numerology Value Calculator
# Numerologists claim to determine a person's character traits based on the numeric value of their name.
# The value of a name is determined by summing up the values of each letter, where:
# 'a' = 1, 'b' = 2, 'c' = 3, … up to 'z' = 26.
# Example: The name “Rohith” has the value
# 18 + 15 + 8 + 9 + 20 + 8 = 78.
# Write a program that accepts a single name as input and calculates its numeric value according to this rule.
# Input Format
# A single word (string) representing a person's name. The name may contain uppercase or lowercase letters.
# Output Format
# Print the numeric value of the given name as an integer.
# Sample Test Case 1
# Input
# Rohith
# Output
# 78

# <....program....>

name = input()

name = name.Lower()

total = 0

for char in name:
    if char.isalpha():
        value = ord(char) - ord('a') + 1
        total += value

print(total)