# Square Root of a Number
# Find square root of a number using binary search

"""
Problem Statement:-

    Given a positive integer n. 
    Find and return its square root. 
    If n is not a perfect square, then return the floor value of sqrt(n).

Examples:-

    Example 1:
    
        Input: 
            n = 36
        Output: 
            6
        Explanation: 
            6 is the square root of 36.
    
    Example 2:
    
        Input: 
            n = 28
        Output: 
            5
        Explanation: 
            The square root of 28 is approximately 5.292. 
            So, the floor value will be 5.
"""

# Function to find out the square root of the given number
def mySqrt (n):
    
    # Declare low and high pointers to 1 and n, respectively
    lo = 1
    hi = n
    
    # Apply Binary Search
    while lo <= hi:
        
        # Calculate the mid
        mid = (lo + hi) // 2
        
        # Check the square value of mid
        if mid * mid <= n:
            
            # Eliminate the left half
            lo = mid + 1
        
        else:
            
            # Eliminate the right half
            hi = mid - 1
    
    return hi

# Main Function
def main():
    
    # Take User Input for the number
    n = int (input ("Enter the Number:\n"))
    
    # Print the result
    print (f"The Square Root of {n} is\n{mySqrt(n)}")

if __name__ == "__main__":
    main()

# Sample Input / Output

"""
Input:

Enter the Number:
n = 36

Output:

The Square Root of 36 is:
6
"""

# Link

"""
Access the Problem:-
    Take U Forward (TUF): https://takeuforward.org/plus/dsa/problems/find-square-root-of-a-number
    Leetcode (Question No. 69): https://leetcode.com/problems/sqrtx/description/

Article: https://takeuforward.org/binary-search/finding-sqrt-of-a-number-using-binary-search/
"""