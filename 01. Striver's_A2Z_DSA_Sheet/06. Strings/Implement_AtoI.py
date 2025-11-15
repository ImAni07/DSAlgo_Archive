# Atoi Function
# Implement Atoi
# String to Integer (atoi)

"""
Problem Statement:-

    Implement the function myAtoi(s) which converts the given string s to a 32-bit signed integer.
    
    Steps to implement:
        
        First, ignore any leading whitespace characters ' ' until the first non-whitespace character is found.
        Check the next character to determine the sign. 
            If it’s a '-', the number should be negative. 
            If it’s a '+', the number should be positive. 
            If neither is found, assume the number is positive.
        Read the digits and convert them into a number. 
            Stop reading once a non-digit character is encountered or the end of the string is reached. 
            Leading zeros should be ignored during conversion.
        The result should be clamped within the 32-bit signed integer range: [-2147483648, 2147483647]. 
            If the computed number is outside this range, 
                return -2147483648 if the number is less than -2147483648, or return 2147483647 if the number is greater than 2147483647.
        Finally, return the computed number after applying all the above steps.
    

Examples:-

    Example 1:
    
        Input: 
            s = "-12345"
        Output: 
            -12345
        Explanation:
            Ignore leading whitespaces.
            The sign '-' is encountered, indicating the number is negative.
            Digits 12345 are read and converted to -12345.
    
    Example 2:
    
        Input: 
            s = "4193 with words"
        Output: 
            4193
        Explanation:
            Read the digits 4193 and stop when encountering the first non-digit character (w).
"""

# Function to convert a string to an integer
# My Atoi Function

def myAtoi (s):
    
    # Step 1: 
    # Remove the leading whitespaces
    s = s.strip ()
    
    # Step 2: 
    # Check if the string is empty after removing the whitespaces
    if len (s) == 0:
        return 0
    
    # Step 3: 
    # Check for the sign
    
    # Initialize a variable to 1, to store the sign
    sign = 1
    
    # Track current position in the string
    index = 0
    
    # Check if the first character is a sign or not
    if s[0] in ['-', '+']:
        
        # Check whether the sign is negative or not, 
        # if it is negative, then update the value of sign as -1
        if s[0] == '-':
            sign = -1
        
        # Increment the value of index by 1
        index += 1
    
    # Step 4: 
    # Convert the string to an integer
    
    # Declare a variable to store the result
    answer = 0
    
    # Iterate over the string from the current index to the end of the string
    while index < len (s):
        
        # Check if the current character is a digit or not
        if s[index].isdigit ():
            
            # If it is a digit, 
            # then update the value of the answer by 
            # multiplying the value by 10 and adding the current digit
            answer = answer * 10 + int (s[index])
            
            # Increase the value of index by 1, to check the next character
            index += 1
        
        # If the current character is not a digit, then break the loop
        else:
            break
    
    # Step 5: 
    # Update the result by multiplying it with the sign
    answer *= sign
    
    # Step 6: 
    # Rounding the result
    
    # Declare the upper limit and the lower limit for the answer
    INT_MAX = 2 ** 31 - 1
    INT_MIN = -2 ** 31
    
    # Check if the result is greater than the upper limit or less than the lower limit, 
    # if it is, then return the upper limit or the lower limit respectively
    if answer > INT_MAX:
        return INT_MAX
    
    elif answer < INT_MIN:
        return INT_MIN
    
    # Otherwise, return the result
    return answer

# Main Function
def main ():
    
    # Take User Input for the String
    s = input ("Enter the String:\n")
    
    # Print the Output
    print (f"The Answer is: {myAtoi (s)}")
    
if __name__ == '__main__':
    main ()

# Sample Input / Output

"""
Input:

Enter the String:
s = "45"

Output:

The Answer is: 45
"""

# Link

"""
Access the Problem:-
    Take U Forward (TUF): https://takeuforward.org/plus/dsa/problems/string-to-integer-atoi
    Leetcode (Question No. 8): https://leetcode.com/problems/string-to-integer-atoi/description/
    Geeks For Geeks (GFG): https://www.geeksforgeeks.org/problems/implement-atoi/1
    Naukri Code 360 (Coding Ninjas): https://www.naukri.com/code360/problems/atoi_981270

Article: https://takeuforward.org/data-structure/implement-atoi
"""