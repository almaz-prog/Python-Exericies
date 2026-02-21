# 1.10 Future Value Calculator
# Write a program futval.py that calculates and displays the future value of an investment over a specified
# number of years.
# The program should prompt the user to enter:
# 1. The initial amount of investment (principal)
# 2. The annualized interest rate (as a decimal, e.g., 0.10 for 10%)
# 3. The number of years the money will be invested
# The program should then display a formatted table showing the value of the investment at the end of each
# year, including year 0 (the initial amount).
# Input Format
# The first line contains a float — the initial amount of the investment.
# The second line contains a float — the annualized interest rate (e.g., 0.05 for 5%).
# The third line contains an integer — the number of years of the investment.
# Output Format
# The output should be a table with two columns:
# Year — The year number starting from 0.
# Value — The investment value at the end of that year (formatted with two decimal places and a dollar sign
# $).
# Sample Test Case 1
# Input
# 1000
# 0.05
# 5
# Output
# Year Value
# ----------------
# 0 $1000.00
# 1 $1050.00
# 2 $1102.50
# 3 $1157.63
# 4 $1215.51
# 5 $1276.28

# <....Program....>
def futval():
    # Prompt user for inputs
    principal = float(input().strip())   # Initial investment
    rate = float(input().strip())        # Annual interest rate (decimal)
    years = int(input().strip())         # Number of years

    # Print table header
    print("Year Value")
    print("----------------")

    # Display value for each year
    value = principal
    for year in range(years + 1):
        print(f"{year} ${value:.2f}")
        value = value * (1 + rate)

# Run the program
if __name__ == "__main__":
    futval()
