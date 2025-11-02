# Find minimum in a rotated sorted array

"""
Problem Statement:-

    Given an integer array nums of size N, 
        sorted in ascending order with distinct values, and 
        then rotated an unknown number of times (between 1 and N), 
        find the minimum element in the array.

Examples:-

    Example 1:
    
        Input: 
            nums = [4, 5, 6, 7, 0, 1, 2, 3]
        Output: 
            0
        Explanation: 
            Here, the element 0 is the minimum element in the array.
    
    Example 2:
    
        Input: 
            nums = [3, 4, 5, 1, 2]
        Output: 
            1
        Explanation:
            Here, the element 1 is the minimum element in the array.
"""

# Import requirement
import sys

# Function to find the minimum element in a given rotated sorted array
def findMin (nums):
    
    # Size of the given rotated sorted array
    n = len (nums)
    
    # Declare and initialize the required variables
    lo = 0
    hi = n - 1
    ans = sys.maxsize
    
    # Apply Binary Search
    while (lo <= hi):
        
        # Update the mid value
        mid = (lo + hi) // 2
        
        # If the given array is already completely sorted then -
        if nums[lo] <= nums[hi]:
            ans = min (ans, nums[lo])
            
            break
        
        # If the left half is sorted -
        if nums[lo] <= nums[mid]:
            ans = min (ans, nums[lo])
            lo = mid + 1
        
        # If the right part is sorted -
        else:
            
            ans = min (ans, nums[mid])
            hi = mid - 1
    
    # Return the resultant
    return ans

# Main Function
def main():
    
    # Take User Input for the Size of the Array
    n = int (input ("Enter the Size of the Array:\n"))
    
    # Take User Input for the Elements of the Array
    nums = list (map (int, input ("Enter the Elements of the Array:\n").split ()))
    
    # Output
    print (f"The Minimum Number in the given Rotated Sorted Array:\n{findMin (nums)}")

if __name__ == "__main__":
    main()

# Sample Input / Output

"""
Input:

Enter the Size of the Array:
n = 6

Enter the Elements of the Array:
nums = 5 6 1 2 3 4

Output:

The Minimum Number in the given Rotated Sorted Array:
1
"""

# Link

"""
Access the Problem:-
    Take U Forward (TUF): https://takeuforward.org/plus/dsa/problems/find-minimum-in-rotated-sorted-array
    Leetcode (Question No. 153): https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
    Geeks For Geeks (GFG): https://www.geeksforgeeks.org/problems/minimum-element-in-a-sorted-and-rotated-array3611/1
    Naukri Code 360 (Coding Ninjas): https://www.naukri.com/code360/problems/rotated-array_1093219

Article: https://takeuforward.org/data-structure/minimum-in-rotated-sorted-array/
"""