# Kth Missing Positive Number

# Leetcode 1539

"""
Problem Statement:-

    Given a sorted array of unique positive integers arr, 
        your task is to return the kᵗʰ missing positive number that is not present in arr.
    The array is guaranteed to be strictly increasing, and 
        the missing numbers are those positive integers that do not appear in arr but 
        would appear in a full sequence starting from 1.

Examples:-

    Example 1:
    
        Input: 
            arr = [3, 5, 7, 10], 
            k = 6
        Output: 
            9
        Explanation:
            The missing numbers are [1, 2, 4, 6, 8, 9, 11, ...]. 
            The 6ᵗʰ missing number is 9.
    
    Example 2:
    
        Input: 
            arr = [1, 4, 6, 8, 9], 
            k = 3
        Output: 
            5
        Explanation:
            The missing numbers are [2, 3, 5, 7, 10, ...]. 
            The 3ʳᵈ missing number is 5.
"""

# Function to find the kth missing positive number
def findKthPositive (arr, k):
    
    # Declare low and high pointers
    lo = 0
    hi = len (arr) - 1
    
    # Apply Binary Search on the index
    while lo <= hi:
        
        # Update the mid value
        mid = (lo + hi) // 2
        
        # Find the missing value
        missing = arr[mid] - (mid + 1)
        
        # Compare the value of the missing positive number with k
        if missing < k:
            
            # Eliminate the left half
            lo = mid + 1
        
        else:
            # Eliminate the right half
            hi = mid - 1
    
    # Return the kth missing number
    return k + hi + 1

# Main Function
def main ():
    
    # Take User Input for the Size of the Array
    n = int (input ("Enter the Size of the Array:\n"))
    
    # Take User Input for the Elements of the Array
    arr = list (map (int, input ("Enter the Elements of the Array:\n").split ()))
    
    # Take User Input for the value of the k
    k = int (input ("Enter the Value of k:\n"))
    
    # Print the output
    print (f"{findKthPositive (arr, k)} is the missing number, which falls at value of k equals to {k}")

if __name__ == "__main__":
    main ()

# Sample Input / Output

"""
Input:

Enter the Size of the Array:
n = 4

Enter the Elements of the Array:
arr = 3 5 7 10

Enter the Value of k:
k = 6

Output:

9 is the missing number, which falls at value of k equals to 6
"""

# Link

"""
Access the Problem:-
    Take U Forward (TUF): https://takeuforward.org/plus/dsa/problems/kth-missing-positive-number
    Leetcode (Question No. 1539): https://leetcode.com/problems/kth-missing-positive-number/description/
    Geeks For Geeks (GFG): https://www.geeksforgeeks.org/problems/kth-missing-positive-number-in-a-sorted-array/1
    Naukri Code 360 (Coding Ninjas): https://www.naukri.com/code360/problems/kth-missing-element_893215

Article: https://takeuforward.org/arrays/kth-missing-positive-number/
"""