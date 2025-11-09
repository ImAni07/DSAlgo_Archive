# Largest Odd Number in String

"""
Problem Statement:-

    Largest Odd Number in a String
    
    Given a string s, representing a large integer, 
        the task is to return the largest-valued odd integer (as a string) that is a substring of the given string s.
    
    The number returned should not have leading zero's. 
        But the given input string may have leading zero. 
        (If no odd number is found, then return empty string.)

Examples:-

    Example 1:
    
        Input: 
            s = "5347"
        Output: 
            "5347"
        Explanation:
            The odd numbers formed by given strings are --> 
                5, 3, 53, 347, 5347.
            So the largest among all the possible odd numbers for given string is 5347.
    
    Example 2:
    
        Input: 
            s = "0214638"
        Output: 
            "21463"
        Explanation:
            The different odd numbers that can be formed by the given string are --> 
                1, 3, 21, 63, 463, 1463, 21463.
            We cannot include 021463 as the number contains leading zero.
            So largest odd number in given string is 21463.
"""

# Function to find the largest odd number in a string
def largestOddNumber(num):
    
    # Traverse the string from the end, looking for the first odd digit
    for i in range(len(num) - 1, -1, -1):
        
        # If the digit is odd, return the substring from the start to this digit (inclusive)
        if int(num[i]) % 2 == 1:
            return num[:i + 1]
    
    # If no odd digit is found, return an empty string
    return ""

# Main Function
def main():
    
    # Take User Input for the String
    num = input("Enter a Numerical String:\n")
    
    # Call the function and print the result
    print(f"The Largest Odd Number in the given String is:\n{largestOddNumber(num)}")

if __name__ == "__main__":
    main()

# Sample Input / Output

"""
Test Case 1:

Input:

Enter a Numerical String:
num = "504"

Output:

The Largest Odd Number in the given String is:
"5"

Test Case 2:

Input:

Enter a Numerical String:
num = "123456789"

Output:

The Largest Odd Number in the given String is:
"123456789"

Test Case 3:

Input:

Enter a Numerical String:
num = "2024"

Output:

The Largest Odd Number in the given String is:
""
"""

# Link

"""
Access the Problem:-
    Take U Forward (TUF): https://takeuforward.org/plus/dsa/problems/largest-odd-number-in-a-string
    Leetcode (Question No. 1903): https://leetcode.com/problems/largest-odd-number-in-string/description/
    Geeks For Geeks (GFG): https://www.geeksforgeeks.org/problems/largest-odd-number-in-string/1

Article: https://takeuforward.org/data-structure/largest-odd-number-in-a-string
"""