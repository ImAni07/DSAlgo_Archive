# Find the number of times the given sorted array has been rotated

"""
Problem Statement:-

    Given an integer array arr of size n, sorted in ascending order with distinct values. 
    The array has been right rotated an unknown number of times, between 0 and n-1 (including). 
    Determine the number of rotations performed on the array.

Examples:-

    Example 1:
    
        Input: 
            arr = [4, 5, 6, 7, 0, 1, 2, 3]
        Output: 
            4
        Explanation: 
            The original array should be [0, 1, 2, 3, 4, 5, 6, 7]. 
            So, we can notice that the array has been rotated 4 times.
    
    Example 2:
    
        Input: 
            arr = [3, 4, 5, 1, 2]
        Output: 
            3
        Explanation: 
            The original array should be [1, 2, 3, 4, 5]. 
            So, we can notice that the array has been rotated 3 times.
"""

# Function to find the number of times the given sorted array has been rotated
def findKRotation (arr):
    
    # Size of the given sorted array
    n = len (arr)
    
    # Declare and initialize the required variables
    lo = 0
    hi = n - 1
    ans = float('inf')
    index = -1
    
    # Apply Binary Search
    while (lo <= hi):
        
        # Update the mid value
        mid = (lo + hi) // 2
        
        # If search space is already sorted
        if arr[lo] <= arr[hi]:
            
            if arr[lo] < ans:
                index = lo
                ans = arr[lo]
                
                break

        # If left part is sorted
        if arr[lo] <= arr[mid]:
            
            # Keep the minimum
            if arr[lo] < ans:
                index = lo
                ans = arr[lo]

            # Eliminate left half
            lo = mid + 1
            
        # If right part is sorted
        else:  
            
            # Keep the minimum
            if arr[mid] < ans:
                index = mid
                ans = arr[mid]

            # Eliminate right half
            high = mid - 1

        # Return the result
        return index

# Main Function
def main():
    
    # Take User Input for the Size of the Array
    n = int (input ("Enter the Size of the Array:\n"))
    
    # Take User Input for the Elements of the Array
    arr = list (map (int, input ("Enter the Elements of the Array:\n").split ()))
    
    # Output
    print (f"The Number of Times the given Sorted Array has been Rotated is:\n{findKRotation (arr)}")

if __name__ == "__main__":
    main()

# Sample Input / Output

"""
Input:

Enter the Size of the Array:
n = 5

Enter the Elements of the Array:
arr = 5 1 2 3 4

Output:

The Number of Times the given Sorted Array has been Rotated is:
1
"""

# Link

"""
Access the Problem:-
    Take U Forward (TUF): https://takeuforward.org/plus/dsa/problems/find-out-how-many-times-the-array-is-rotated
    Geeks For Geeks (GFG): https://www.geeksforgeeks.org/problems/rotation4723/1
    Naukri Code 360 (Coding Ninjas): https://www.naukri.com/code360/problems/rotation_7449070

Article: https://takeuforward.org/arrays/find-out-how-many-times-the-array-has-been-rotated/
"""