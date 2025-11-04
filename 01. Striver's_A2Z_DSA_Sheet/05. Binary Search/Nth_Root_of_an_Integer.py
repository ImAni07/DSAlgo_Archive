# Nth Root of an Integer
# Find the Nth Root of a Number

"""
Problem Statement:-

    Given two numbers N and M, find the Nth root of M. 
    The Nth root of a number M is defined as a number X such that when X is raised to the power of N, it equals M. 
    If the Nth root is not an integer, return -1.

Examples:-

    Example 1:
    
        Input: 
            N = 3, 
            M = 27
        Output: 
            3
        Explanation: 
            The cube root of 27 is equal to 3.
    
    Example 2:
    
        Input: 
            N = 4, 
            M = 69
        Output:
            -1
        Explanation: 
            The 4th root of 69 does not exist. 
            So, the answer is -1.
"""

# Function to get the power
def power (mid, n, m):
    
    # Store the answer
    result = 1
    
    # Iterate
    for i in range (1, (n + 1)):
        result = result * mid

        # Return early to avoid overflow
        if result > m:
            return -1
    
    # Return 1 upon matching
    if result == m:
        return 1
    
    # Return 0, if it is less than mid
    return 0

# Function to find the nth root of m by binary search
def nthRoot (n, m):
    
    # Handle edge cases
    
    # When the given number is 0
    # nth root of 0 is 0
    if m == 0:
        return 0
    
    # If n is 1, return m
    if n == 1:
        return m
    
    # Initialize low and high pointers
    lo = 1
    hi = m
    
    # Apply Binary Search
    while lo <= hi:
        
        # Update mid value
        mid = (lo + hi) // 2
        
        # Compute the value of mid ^ n
        value = power (mid, n, m)
        
        # If mid ^ n is equal to m
        if value == 1:
            return mid
        
        # If mid ^ n is less than m
        elif value == 0:
            lo = mid + 1
        
        # If mid ^ n is greater than m
        else:
            hi = mid - 1
    
    # If not found
    return -1

# Main Function
def main ():
    
    # Take User Input for the Base
    m = int (input ("Enter the Base Number:\n"))
    
    # Take User Input for the Exponent
    n = int (input ("Enter the Exponent Number:\n"))
    
    # Output
    print(f"The Root of {n} on the Base of {m} is:\n{nthRoot (n, m)}")

if __name__ == "__main__":
    main ()

# Sample Input / Output

"""
Input:

Enter the Base Number:
27

Enter the Exponent Number:
3

Output:

The Root of 3 on the Base of 27 is:
3
"""

# Link

"""
Access the Problem:-
    Take U Forward (TUF): https://takeuforward.org/plus/dsa/problems/find-nth-root-of-a-number
    Geeks For Geeks (GFG): https://www.geeksforgeeks.org/problems/find-nth-root-of-m5843/1
    Naukri Code 360 (Coding Ninjas): https://www.naukri.com/code360/problems/nth-root-of-m_1062679?leftPanelTabValue=PROBLEM

Article: https://takeuforward.org/data-structure/nth-root-of-a-number-using-binary-search/
"""