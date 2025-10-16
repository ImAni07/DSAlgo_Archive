# Count the Number of Digits

# Variation 1

"""
Problem Statement: 
    Given an integer N, return the number of digits in N.
"""

# Code

# Function to count the number of digits in a given number
def nDigits (n):
    
    # Store the Required Number in a temporary variable
    temp = n
    
    # Variable to count the number of digits 
    count = 0
    
    # Variable to store the unit place digit of the given number
    remainder = 0
    
    # Iterate
    while (temp > 0):
        remainder = temp % 10
        count += 1
        temp = temp // 10
    
    # Return the count
    return count

# Variation 2

# Count the Number of Digits that evenly divides the given number

"""
    Evenly dividing means, the result of the division will yield no remainder.
    For example,
        If the given number is 123
        The result will be 2
            Since, both 1 and 3 divides 123 without any remainder and while dividing by 2, it yields a remainder of 1.
"""

# Function to count the number of digits that divide the given number
def countDigits (n):
    
    # Check if the number is positive or negative
    if n < 0:
        n = abs (n)
    
    # Store the given number in a temporary variable upon which the required operations will be performed
    temp = n
    
    # Variable to store the count of digits that divide the given number evenly
    count = 0
    
    # Iterate
    while (temp > 0):
        remainder = temp % 10
        if remainder != 0 and n % remainder == 0:
            count += 1
        temp //= 10
    
    # Return the answer
    return count

# Main Function
def main():
    
    # Take User Input
    n = int(input("Enter a Number:\n"))
    
    # Print the Output
    print()
    print("Count Digits:")
    print(f"The number of digits in {n} is: {nDigits(n)}")
    print()
    print("Count Dividing Digits:")
    print(f"The number of digits in {n} that divides {n} is: {countDigits(n)}")
    print()

if __name__ == "__main__":
    main()

# Sample Input / Output

"""
Example:

Input:

Enter a Number:
n = 124

Output:

Count Digits:
The number of digits in 124 is: 3

Count Dividing Digits:
The number of digits in 124 that divides 124 is: 3
"""

# Links

"""
Access the problem (Variation 1):-
    Take U Forward (TUF): https://takeuforward.org/plus/dsa/problems/count-all-digits-of-a-number
    Geeks For Geeks (GFG): https://www.geeksforgeeks.org/problems/count-digits-1606889545/1

Access the problem (Variation 2):-
    Leetcode (Question No. 2520): https://leetcode.com/problems/count-the-digits-that-divide-a-number/description/
    Code Studio (Coding Ninjas): https://www.naukri.com/code360/problems/count-digits_8416387

Article: https://takeuforward.org/data-structure/count-digits-in-a-number/
"""