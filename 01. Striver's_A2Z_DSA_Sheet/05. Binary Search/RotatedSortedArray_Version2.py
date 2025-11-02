# Search in Rotated Sorted Array - 2

"""
Problem Statement:-

    There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).
    Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) 
        such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). 
        For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].
    Given the array nums after the rotation and an integer target, 
        return true if target is in nums, or false if it is not in nums.
    You must decrease the overall operation steps as much as possible.

Examples:-

    Example 1:
    
        Input: 
            nums = [2,5,6,0,0,1,2], 
            target = 0
        Output: 
            true
    
    Example 2:
    
        Input: 
            nums = [2,5,6,0,0,1,2], 
            target = 3
        Output: 
            false
"""

# Function to find the target element from the given rotated sorted array
def search (nums, target):
    
    # Size of the given rotated sorted array
    n = len (nums)
    
    # Declare and initialize the required variables
    lo = 0
    hi = n - 1
    
    # Apply Binary Search
    while (lo <= hi):
        
        # Update the mid value
        mid = (lo + hi) // 2
        
        # If the mid point is equal to the target element
        if nums[mid] == target:
            return True
        
        # Handling the edge case
        if nums[mid] == nums[lo] and nums[mid] == nums[hi]:
            
            # Shrink the search space by decreasing the value of hi by 1 and increasing the value of lo by 1
            lo += 1
            hi -= 1
            continue
        
        # If the left half of the array is sorted
        if nums[lo] <= nums[mid]:
            
            # Check whether the element exists or not
            if nums[lo] <= target and target <= nums[mid]:
                
                # If the element exists
                hi = mid - 1
            
            else:
                # If the element doesn't exist
                lo = mid + 1
        
        # If the right half of the array is sorted
        else:
            if nums[mid] <= target and target <= nums[hi]:
                
                # If the element exists
                lo = mid + 1
            
            else:
                # If the element doesn't exist
                hi = mid - 1
    
    # If the element doesn't exist
    return False

# Main Function
def main():
    
    # Take User Input for the Size of the Array
    n = int (input ("Enter the Size of the Array:\n"))
    
    # Take User Input for the Elements of the Array
    nums = list (map (int, input ("Enter the Elements of the Array:\n").split ()))
    
    # Take User Input for the Target Value
    target = int (input ("Enter the Target Value:\n"))
    
    # Store the result
    answer = search (nums, target)
    
    # Output
    if not answer:
        print(f"The Target Element {target} is not present.")
        print(f"Therefore, the Output is: {answer}")
    else:
        print(f"The Target Element {target} is present.")
        print(f"Therefore, the Output is: {answer}")

if __name__ == "__main__":
    main()

# Sample Input / Output

"""
Test Case 1 --> When the Target is present

Input:

Enter the Size of the Array:
n = 10

Enter the Elements of the Array:
nums = 7 8 9 0 1 2 3 4 5 6

Enter the Target Value:
target = 3

Output:

The Target Element 3 is present.
Therefore, the Output is: True

Test Case 2 --> When the Target is not present

Input:

Enter the Size of the Array:
n = 10

Enter the Elements of the Array:
nums = 7 8 9 0 1 2 3 4 5 6

Enter the Target Value:
target = 10

Output:

The Target Element 10 is not present.
Therefore, the Output is: False
"""

# Link

"""
Access the Problem:-
    Take U Forward (TUF): https://takeuforward.org/plus/dsa/problems/search-in-rotated-sorted-array-ii
    Leetcode (Question No. 81): https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/

Article: https://takeuforward.org/arrays/search-element-in-rotated-sorted-array-ii/
"""