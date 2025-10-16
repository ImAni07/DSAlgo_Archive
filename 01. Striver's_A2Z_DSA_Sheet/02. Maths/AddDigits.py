# Add Digits

"""
Problem Statement:
    Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

    Examples:
    
    Example 1:
    Input: 
        num = 38
    Output: 
        2
    Explanation: 
        The process is
            38 --> 3 + 8 --> 11
            11 --> 1 + 1 --> 2 
            Since 2 has only one digit, return it.
    
    Example 2:
    Input: 
        num = 0
    Output: 
        0
"""

# Function to add the digits of a number until a single digit is obtained
def addDigits(num):
    
    # Base case: if the number is less than 10, return the number itself
    if num < 10:
        return num
    
    # Iterate on the digits of the number
    while num >= 10:
        
        # Variable to store the sum of the digits
        sumDigits = 0
        
        # Add the digits of the number
        while num > 0:
            sumDigits += num % 10
            num //= 10
        
        # Update num with the sum of its digits
        num = sumDigits
    
    # Return the final single digit
    return num

# Main Function
def main():
    
    # Take input from the user
    num = int (input ())
    
    # Print the Output
    print (addDigits(num))

if __name__ == "__main__":
    main()

# Sample Input / Output:

"""
Input:
num = 123

Output:
6
"""

# Links

"""
Access the problem:-
    Leetcode (Question No. 258): https://leetcode.com/problems/add-digits/description/
"""