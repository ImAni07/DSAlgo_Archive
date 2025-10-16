# GCD of HCF
# Find the Greatest Common Divisor (GCD) or Highest Common Factor (HCF) of 2 numbers

"""
Problem Statement:
    Given two integers N1 and N2, find their greatest common divisor.
    The Greatest Common Divisor of any two integers is the largest number that divides both integers.

Examples:

    Example 1:
        Input:
            N1 = 9, 
            N2 = 12
        Output:
            3
        Explanation:
            Factors of 9: 1, 3 and 9
            Factors of 12: 1, 2, 3, 4, 6, 12
            Common Factors: 1, 3 out of which 3 is the greatest hence it is the GCD.

    Example 2:
        Input:
            N1 = 20, 
            N2 = 15
        Output: 
            5
        Explanation:
            Factors of 20: 1, 2, 4, 5
            Factors of 15: 1, 3, 5
            Common Factors: 1, 5 out of which 5 is the greatest hence it is the GCD.
"""

# Function to calculate the HCF
def find_gcd(a, b):
    
    # Iterate until both the numbers are greater than 0
    while a > 0 and b > 0:
        
        # Check if a is greater than b
        if a > b:
            
            # Update the value of a
            a = a % b
        
        else:
            
            # Update the value of b
            b = b % a
    
    # Check whether a becomes 0, if so then return b
    if a == 0:
        return b
    
    # If a does not become 0, then return a
    return a

# Main Function
def main():
    
    # Take User Input
    a = int (input ("Enter the 1st Number:\n"))
    b = int (input ("Enter the 2nd Number:\n"))
    
    # Store the result
    gcd = find_gcd(a,b)
    
    # Print
    print(f"GCD or HCF of {a} and {b} is: {gcd}")

if __name__ == "__main__":
    main ()

# Sample Input / Output

"""
Example:

Input:
Enter the 1st Number:
a = 20
Enter the 2nd Number:
b = 12

Output:
GCD or HCF of 20 and 12 is: 4
"""

# Links

"""
Access the problem:-
    Take U Forward (TUF): https://takeuforward.org/plus/dsa/problems/gcd-of-two-numbers
    Geeks For Geeks (GFG): https://www.geeksforgeeks.org/problems/gcd-of-two-numbers3459/1
    Code Studio (Coding Ninjas): https://www.naukri.com/code360/problems/hcf-and-lcm_840448?leftPanelTabValue=PROBLEM

Article: https://takeuforward.org/data-structure/find-gcd-of-two-numbers/
"""