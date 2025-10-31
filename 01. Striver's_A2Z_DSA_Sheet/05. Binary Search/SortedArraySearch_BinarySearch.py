# Binary Search
# Search in a Sorted Array
# Sorted Array Search

"""
Problem Statement:-

    Given a sorted array of integers arr with 0-based indexing. 
    Find the index of a specified target integer. 
    If the target is found in the array, return its index. 
    If the target is not found, return -1.

Examples:-

    Example 1:
    
        Input: 
            arr = [-1,0,3,5,9,12], 
            target = 9
        Output: 
            4
        Explanation: 
            The target integer 9 exists in arr and its index is 4
    
    Example 2:
    
        Input: 
            arr = [-1,0,3,5,9,12], 
            target = 2
        Output: 
            -1
        Explanation: 
            The target integer 2 does not exist in arr so return -1
"""

# Function to perform binary search to search the target element from a given array
def search (arr, target):
    
    # Initialize the low and the high pointers
    lo = 0
    hi = len(arr) - 1
    
    # Iterate in the array, as long as the value of low pointer is less than or equal to the value of the high pointer
    while lo <= hi:
        
        # Update the value of the mid pointer
        mid = (lo + hi) // 2
        
        # Check if the value of the mid pointer is equal to the target value or not, if yes then return it
        if arr[mid] == target:
            return mid
        
        # If the value of the mid pointer is greater than the target, then update the value of the high pointer
        elif arr[mid] > target:
            hi = mid - 1
        
        # If the value of the mid pointer is less than the target, then update the value of the low pointer
        else:
            lo = mid + 1
    
    # If the target value is not present
    return -1

# Main Function
def main():
    
    # Take User Input for the Size of the Array
    n = int (input ("Enter the Size of the Array:\n"))
    
    # Take User Input for the Elements of the Array
    arr = list (map (int, input ("Enter the Elements of the Array:\n").split ()))
    
    # Take User Input for the Target Element
    target = int (input ("Enter the Target Value:\n"))
    
    # Store the Result
    result = search (arr, target)
    
    # Output
    if result == -1:
        print (f"The Target Value of {target} is not present in the given Array.")
    else:
        print (f"The Target Value of {target} is present in the given Array at index:\n {result}")

if __name__ == "__main__":
    main()

# Sample Input / Output

"""
Input:

Enter the Size of the Array:
n = 10

Enter the Elements of the Array:
arr = 0 1 2 3 4 5 6 7 8 9

Enter the Target Value:
target = 7

Output:

The Target Value of 7 is present in the given Array at index:
7
"""

# Link

"""
Access the Problem:-
    Take U Forward (TUF): https://takeuforward.org/plus/dsa/problems/search-x-in-sorted-array
    Leetcode (Question No. 704): https://leetcode.com/problems/binary-search/description/
    Geeks For Geeks (GFG): https://www.geeksforgeeks.org/problems/who-will-win-1587115621/1
    Naukri Code 360 (Coding Ninjas): https://www.naukri.com/code360/problems/binary-search_972

Article: https://takeuforward.org/data-structure/binary-search-explained/
"""