# Implement Lower Bound

"""
Problem Statement:-

    Lower Bound
    
    Given a sorted array arr and an integer x, write a program to find the lower bound of x.
    The lower bound algorithm finds the first and smallest index in a sorted array 
        where the value at that index is greater than or equal to a given key i.e. x.
    If no such index is found, return the size of the array.

Examples:-

    Example 1:
    
        Input: 
            arr = [1,2,2,3], 
            x = 2
        Output:
            1
        Explanation:
            Index 1 is the smallest index such that arr[1] >= x.
    
    Example 2:
    
        Input: 
            arr = [3,5,8,15,19], x = 9
        Output: 
            3
        Explanation:
            Index 3 is the smallest index such that arr[3] >= x.
"""

# Function to find out the Lower Bond from the given array
def lowerBound (arr, n, x):
    
    # Initialize the low and the high pointers
    lo = 0
    hi = n - 1
    
    # Initialize a variable to store the answer
    answer_lb = -1
    
    # Iterate through the array
    while lo <= hi:
        
        # Update the value of the mid pointer
        mid = (lo + hi) // 2
        
        # Maybe an answer
        if arr[mid] >= x:
            answer_lb = mid
            
            # Check for other smaller indices
            hi = mid - 1
        
        else:
            # Check for the indices greater than mid value
            lo = mid + 1
    
    # Return the answer
    return answer_lb

# Main Function
def main():
    
    # Take User Input for the Size of the Array
    n = int (input ("Enter the Size of the Array:\n"))
    
    # Take User Input for the Elements of the Array
    arr = list (map (int, input ("Enter the Elements of the Array:\n").split ()))
    
    # Take User Input for Checking the Lower Bound of a Number in the given Array
    x = int (input ("Enter the Element for Lower Bound:\n"))
    
    # Output
    print (f"The Lower Bound of {x} in the given Array is:\n{lowerBound (arr, n, x)}")

if __name__ == "__main__":
    main()

# Sample Input / Output

"""
Input:

Enter the Size of the Array:
n = 7

Enter the Elements of the Array:
arr = 2 3 7 10 11 11 25

Enter the Element for Lower Bound:
x = 11

Output:

The Lower Bound of 11 in the given Array is:
4
"""

# Link

"""
Access the Problem:-
    Take U Forward (TUF): https://takeuforward.org/plus/dsa/problems/lower-bound-
    Geeks For Geeks (GFG): https://www.geeksforgeeks.org/problems/implement-lower-bound/0
    Naukri Code 360 (Coding Ninjas): https://www.naukri.com/code360/problems/lower-bound_8165382

Article: https://takeuforward.org/arrays/implement-lower-bound-bs-2/
"""