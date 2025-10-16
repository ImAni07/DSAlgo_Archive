# Leetcode 9
# Palindrome Number

"""
Palindrome Number:
    Given an integer x, return true if x is a palindrome, and false otherwise.
    
    Example 1:
        Input: 
            x = 121
        Output: 
            true
        Explanation: 
            121 reads as 121 from left to right and from right to left.

    Example 2:
        Input: 
            x = -121
        Output: 
            false
        Explanation: 
            From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

    Example 3:
        Input: 
            x = 10
        Output: 
            false
        Explanation: 
            Reads 01 from right to left. Therefore it is not a palindrome.
    
    Solve it in 2 ways:-
    1. Convert the number to string and compare it with its reverse string.
    2. Without converting the number to a string.
"""
class Solution:

    # Function to check palindrome
    def isPalindrome(self, x: int) -> bool:
    
        """
            Function Description:
                This function checks whether the given number is a Palindrome number or not
                It returns True if the number is a palindrome else it returns False.
                Function Name: isPalindrome
                Parameter: Accepts an integer value 'x', which is to be checked, whether it is a Palindrome number or not
                Returns a Boolean value, either 'True' or 'False', depending whether the given is a Palindrome number or not, respectively.
        """
        
        # Way 1:
        
        """
                Workflow:
                    1. Check whether the given number is positive or negative, since negative numbers can't be palindrome
                    2. Convert the given number 'x' to a string
                    3. Reverse the string using slicing
                    4. Convert the reversed string to an integer
                    5. Compare the original number with the reversed number
            """
        
        # Check whether the given number is positive or not
        if x < 0:
            return False
        else:
            answer = int (str (x) [::-1])
            
            # Check whether the value stored in the variable 'answer' is equal to the value stored in the variable 'x'
            if answer == x:
                return True
        
            else:
                return False
    
    # Function to check palindrome
    def palindrome(self, x: int) -> bool:
        
        """
            Function Description:
                This function checks whether the given number is a Palindrome number or not
                It returns True if the number is a palindrome else it returns False.
                Function Name: isPalindrome
                Parameter: Accepts an integer value 'x', which is to be checked, whether it is a Palindrome number or not
                Returns a Boolean value, either 'True' or 'False', depending whether the given is a Palindrome number or not, respectively.
        """
        
        # Way 2
        
        """
            Workflow:
                Initialize an integer revNum to 0.
                Make a duplicate of the original number and store it in an integer dup for later comparison.
                Run a while loop with the condition n>0 to reverse the number and at each iteration:
                    Get the last digit of n by using the modulus operator % with 10 and store it in a temporary variable ld.
                    Update the revNum by multiplying it by 10 and adding the last digit ld.
                    Update n by integer division with 10 effectively removing the last digit.
                After the loop, check if the original number dup is equal to the reversed number revNum.
                    If they are equal, return true indicating the number is a palindrome.
                    If they are not equal, return false indicating that the number is not a palindrome.
            
            Function Description:
                This function checks whether the given number is a Palindrome number or not
                It returns True if the number is a palindrome else it returns False.
                Function Name: palindrome
                Parameter: Accepts an integer value 'x', which is to be checked, whether it is a Palindrome number or not
                Returns a Boolean value, either 'True' or 'False', depending whether the given is a Palindrome number or not, respectively.
        """
        
        # Initialize a variable to store the reverse of a number
        revNum = 0
        
        # Create a duplicate variable to store the original number
        n = x
        
        # Iterate through each digit until the number becomes 0
        while n > 0:
            
            # Extract the last digit of the given number
            last_digit = n % 10
            
            # Add the last digit
            revNum = (revNum * 10) + last_digit
            
            # Remove the last digit
            n = n // 10
        
        # Check if the reversed number is equal to the original number
        if revNum == x:
            
            # Return true, if it is equal
            return True
        
        else:
            
            # Return false, if it is not equal
            return False

# Main Function
def main ():
    
    # Take User Input for the number
    x = int (input ("Enter a Number:\n"))
    
    # Create an object of the Solution class
    obj = Solution()

    # Call both the functions
    result = obj.isPalindrome(x)
    answer = obj.palindrome(x)

    # Print Results
    print("\nResults:")
    print(f"Using String Conversion: {result}")
    print(f"Without String Conversion: {answer}")

if __name__ == "__main__":
    main()

# Sample Input / Output

"""
Example 1:

Input:
x = 121

Output:
Using String Conversion: True
Without String Conversion: True

Example 2:

Input:
x = -121

Output:
Using String Conversion: False
Without String Conversion: False
"""

# Links

"""
Access the problem:-
    Take U Forward (TUF): https://takeuforward.org/plus/dsa/problems/palindrome-number
    Leetcode (Question No. 9): https://leetcode.com/problems/palindrome-number/
    Geeks For Geeks (GFG): https://www.geeksforgeeks.org/problems/palindrome0746/1
    Code Studio (Coding Ninjas): https://www.naukri.com/code360/problems/palindrome-number_624662

Article: https://takeuforward.org/data-structure/check-if-a-number-is-palindrome-or-not/
"""