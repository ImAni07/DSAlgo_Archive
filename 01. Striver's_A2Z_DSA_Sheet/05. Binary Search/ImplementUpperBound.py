# Implement Upper Bound

"""
Problem Statement:-

    Upper Bound
    
    Given a sorted array arr and an integer x, write a program to find the upper bound of x.
    The upper bound of x is defined as the smallest index i such that arr[i] > x.
    If no such index is found, return the size of the array.

Examples:-

    Example 1:
    
        Input: 
            n= 4, 
            arr = [1,2,2,3], 
            x = 2
        Output:
            3
        Explanation:
            Index 3 is the smallest index such that arr[3] > x.
    
    Example 2:
    
        Input: 
            n = 5, 
            arr = [3,5,8,15,19], 
            x = 9
        Output: 
            3
        Explanation:
            Index 3 is the smallest index such that arr[3] > x.
"""

# Function to find out the Upper Bound from the given array
def upperBound (arr, n, x):
    
    # Initialize the low and the high pointers
    lo = 0
    hi = n - 1
    
    # Initialize a variable to store the answer
    answer_ub = -1
    
    # Iterate through the array
    while lo <= hi:
        
        # Update the value of the mid pointer
        mid = (lo + hi) // 2
        
        # Maybe an answer
        if arr[mid] > x:
            answer_ub = mid
            
            # Check for other smaller indices
            hi = mid - 1
        
        else:
            # Check for the indices greater than mid value
            lo = mid + 1
    
    # Return the answer
    return answer_ub

# Main Function
def main():
    
    # Take User Input for the Size of the Array
    n = int (input ("Enter the Size of the Array:\n"))
    
    # Take User Input for the Elements of the Array
    arr = list (map (int, input ("Enter the Elements of the Array:\n").split ()))
    
    # Take User Input for Checking the Upper Bound of a Number in the given Array
    x = int (input ("Enter the Element for Upper Bound:\n"))
    
    # Output
    print (f"The Upper Bound of {x} in the given Array is:\n{upperBound (arr, n, x)}")

if __name__ == "__main__":
    main()

# Sample Input / Output

"""
Input:

Enter the Size of the Array:
n = 6

Enter the Elements of the Array:
arr = 3 5 7 9 15 20

Enter the Element for Upper Bound:
x = 9

Output:

The Upper Bound of 9 in the given Array:
4
"""

# Link

"""
Access the Problem:-
    Take U Forward (TUF): https://takeuforward.org/plus/dsa/problems/upper-bound
    Geeks For Geeks (GFG): https://www.geeksforgeeks.org/problems/implement-upper-bound/1
    Naukri Code 360 (Coding Ninjas): https://www.naukri.com/code360/problems/implement-upper-bound_8165383

Article: https://takeuforward.org/arrays/implement-upper-bound/
"""