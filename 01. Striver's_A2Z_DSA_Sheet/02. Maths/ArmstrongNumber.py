# Armstrong Number
# Check whether a given number is an Armstrong Number or not

"""
    Problem Statement:-
        You are given an integer 'n'.
        Return 'true' if 'n' is an Armstrong number, and 'false' otherwise.
        An Armstrong number is a number (with 'k' digits) such that the sum of its digits raised to 'kth' power is equal to the number itself.
        For example, 371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371.
    
    Detailed Explanation:-
        Sample Input 1 :
            1
        Sample Output 1 :
            true
        Explanation of Sample Input 1 :
            1 is an Armstrong number as, 1^1 = 1.

        Sample Input 2 :
            103
        Sample Output 2 :
            false
            
        Sample Input 3 :
            1634
        Sample Output 3 :
            true
        Explanation of Sample Input 3 :
            1634 is an Armstrong number, as 1^4 + 6^4 + 3^4 + 4^4 = 1634
"""

# Function to check whether a number is an Armstrong number or not
def checkArmstrong (n):
    
    """
        Function Description: This function checks whether a given number ('n', in this case), is an Armstrong number or not
        Parameters: n (int) - The number to be checked
        Returns: bool - True if the number is an Armstrong number, False otherwise
    """
    
    # Calculate the number of digits in the given number
    num_digits = len (str (n))
    
    # Create a Variable to store the Sum of the Digits of the given number, to the power of the Number of Digits of the given number
    sum = 0
    
    # Create a Temporary variable, to store the given number
    temp = n
    
    # Check whether the given number is an Armstrong number or not
    while (temp > 0):
        
        # Extract the last digit of the temporary number
        last_digit = temp % 10
        
        # Add the digit at the unit place of the number, to the power of the number of digits
        sum += last_digit ** num_digits
        
        # Divide the value stored 'temp' by 10
        temp //= 10
    
    # Return whether the given number is an Armstrong number or not
    if n == sum:
        return True
    else:
        return False
    
# Main Function
def main():

    n = int(input ("Enter a Number:\n"))
    print (str (checkArmstrong (n)). lower())
    
if __name__ == "__main__":
    main()

# Sample Input / Output

"""
Example:

Input:
n = 371

Output:
true
"""

# Link

"""
Access the problem:-
    Take U Forward (TUF): https://takeuforward.org/plus/dsa/problems/check-if-the-number-if-armstrong
    Leetcode (Premium Problem): https://leetcode.com/problems/armstrong-number/description/
    Geeks For Geeks (GFG): https://www.geeksforgeeks.org/problems/armstrong-numbers2727/1
    Code Studio (Coding Ninjas): https://www.naukri.com/code360/problems/check-armstrong_589

Article: https://takeuforward.org/maths/check-if-a-number-is-armstrong-number-or-not/
"""