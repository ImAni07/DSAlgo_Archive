# Print all Divisors of a given Number

"""
Problem Statement:
    Given an integer N, return all divisors of N.
    
    A divisor of an integer N is a positive integer that divides N without leaving a remainder. 
    In other words, if N is divisible by another integer without any remainder, then that integer is considered a divisor of N.

Examples:

    Example 1:
    
    Input:
        N = 36
    Output:
        [1, 2, 3, 4, 6, 9, 12, 18, 36]
    Explanation: 
        The divisors of 36 are 1, 2, 3, 4, 6, 9, 12, 18, 36.
    
    Example 2:
    
    Input:
        N = 12                
    Output: 
        [1, 2, 3, 4, 6, 12]
    Explanation: 
        The divisors of 12 are 1, 2, 3, 4, 6, 12.     
"""

# Import module
import math

# Function to find the divisors of a number
def findDivisors(n):
    
    # Initialize an empty list to store the divisors
    divisors = [] 

    # Calculate the square root of n
    sqrtN = int(math.sqrt(n)) 
    
    # Iterate from 1 up to the square root of n to find divisors
    for i in range(1, sqrtN + 1):
        
        # Check if i divides n without leaving a remainder
        if n % i == 0:
            
            # Add divisor i to the list
            divisors.append(i) 

            # Add the counterpart divisor if it's different from i
            if i != n // i:
                divisors.append(n // i) 
    
    # Return the list of divisors
    return divisors 

# Main Function
def main ():
    
    # Take User Input
    number = int (input ("Enter a Number:\n"))
    
    # Store the Result
    divisors = findDivisors(number)

    # Print the Result
    print("Divisors of", number, "are:", end=" ")
    for divisor in divisors:
        print(divisor, end=" ")
    print()

if __name__ == "__main__":
    main ()

# Sample Input / Output

"""
Input:

Enter a Number:
number = 12

Output:

Divisors of 12 are: 1 12 2 6 3 4
"""

# Link

"""
Access the problem:-
    Take U Forward (TUF): https://takeuforward.org/plus/dsa/problems/divisors-of-a-number
    Geeks For Geeks (GFG): https://www.geeksforgeeks.org/problems/all-divisors-of-a-number/1
    Code Studio (COding Ninjas): https://www.naukri.com/code360/problems/print-all-divisors-of-a-number_1164188

Article: https://takeuforward.org/data-structure/print-all-divisors-of-a-given-number/
"""