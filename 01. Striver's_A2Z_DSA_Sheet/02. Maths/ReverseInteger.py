# LeetCode 7:
# Reverse Integer

"""
Problem Statement:
    Given a signed 32-bit integer x, return x with its digits reversed.
    If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.
    Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
"""

# Code

class Solution:

    # Function to reverse the digits of a number
    def reverse (self, x: int) -> int:

        """
            Function Description:
                Name: reverse
                Parameter: Accepts an integer value in a variable 'x'
                Output: Returns an integer value by reversing the digits of the given integer
        """

        # Creating a Temporary Variable to store the given number
        n = x

        # Check whether the given number is positive or negative
        if x < 0:
            sign = -1
        else:
            sign = 1
        
        n = x * sign

        # Variable to store the reversed number
        rev = 0

        # Reversing the given integer x

        while n > 0:
            rev = (rev * 10) + (n % 10)
            n //= 10

        rev *= sign

        # Return the output based on the condition

        """
        Condition:
            If the value of 'rev' is within the prescribed range, as defined -
                Then return the reversed value, stored in 'rev'
            Else
                Return 0
            The prescribed range is:
                The value should be greater than equal to (-2 ** 31)
                The value should be less than equal to ((-2 ** 31) -1)
        """

        if rev < -2**31 or rev > 2**31 - 1:
            return 0
        else:
            return rev

# Main Function
def main ():
    
    # Take User Input for the number
    n = int (input ("Enter a Number:\n"))
    
    # Create an object of the Solution class
    obj = Solution()

    # Call the reverse function
    result = obj.reverse(n)

    # Print the reversed integer
    print(f"The reversed integer is: {result}")

if __name__ == "__main__":
    main ()

# Sample Input / Output

"""
Example:

Input:
x = 123

Output:
3
"""

# Links

"""
Access the problem:-
    Take U Forward (TUF): https://takeuforward.org/plus/dsa/problems/reverse-a-number
    Leetcode (Question No. 7): https://leetcode.com/problems/reverse-integer/
    Geeks For Geeks (GFG): https://www.geeksforgeeks.org/problems/reverse-digit0316/1
    Code Studio (Coding Ninjas): https://www.naukri.com/code360/problems/reverse-of-a-number_624652

Article: https://takeuforward.org/maths/reverse-digits-of-a-number
"""