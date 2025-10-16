# Prime Number
# Check if a number is a prime number or not

"""
    Check Prime
    
    Problem Statement:-
        A prime number is a positive integer that is divisible by exactly 2 integers, 1 and the number itself.
        You are given a number 'n'.
        Find out whether 'n' is prime or not.
    
    Examples:-
        
        Example 1:
            Input:
                n = 5
            Output:
                YES
            Explanation:
                5 is only divisible by 1 and 5.
                2, 3 and 4 do not divide 5.
        
        Example 2:
            Input:
                n = 6
            Output:
                NO
            Explanation:
                6 is divisible by 1, 2, 3 and 6.
                Therefore, it is not a Prime Number.
                Numbers having more than 2 factors are known as Composite Numbers.
        
        Example 3:
            Input:
                n = 1
            Output:
                NO
            Explanation:
                1 is divisible by only 1, itself and has only 1 factor.
                Therefore, it is not a Prime Number.
                1 is neither a Prime Number, nor a Composite Number.
                It is also called Unique Number.
"""

# Import all the Required Libraries
import math

# Function to check whether the given number is a Prime Number or not
def check_prime (n):
    
    """
        Function Description:- This function checks whether the given number 'n' is a Prime Number or not.
        Parameters:- Accepts an integer value 'n' which is to be checked whether the value stored in 'n' is prime or not
        Return:- It returns 'YES' if 'n' is a Prime Number and 'NO' otherwise.
    """
    
    # Handle the edge cases
    
    # Edge Case 1: When the input is either 0 or 1
    if n < 2:
        return "NO"
    
    # Edge Case 2: When the input is exactly equal to 2
    elif n == 2:
        return "YES"
    
    # When the input is greater than 2
    else:
        
        # Iterate from 2 to the square root of the given number 'n'
        for i in range (2, (int (math.sqrt (n))) + 1):
            
            # Check whether the given number 'n' is divisible by any number situated in the range
            if n % i == 0:
                return "NO"
        
        # If the given number 'n' is not divisible by any number within the range of 2 to the square root of 'n', 
        # then the number is a Prime Number
        return "YES"

# Main Function
def main():
    
    # Read Input from the User
    n = int (input ())
        
    # Print the Output
    print (check_prime (n))

if __name__ == "__main__":
    main()

# Sample Input / Output

"""
Example 1:

Input:
n = 12

Output:
NO

Example 2:

Input:
n = 7

Output:
YES
"""

# Links

"""
Access the problem:-
    Take U Forward (TUF): https://takeuforward.org/plus/dsa/problems/check-for-prime-number
    Geeks For Geeks (GFG): https://www.geeksforgeeks.org/problems/prime-number2314/1
    Code Studio (Coding Ninjas): https://www.naukri.com/code360/problems/check-prime_624934

Article: https://takeuforward.org/data-structure/check-if-a-number-is-prime-or-not/
"""
