# Search single element from a given sorted array

"""
Problem Statement:-

    Given an array nums sorted in non-decreasing order. 
    Every number in the array except one appears twice. 
    Find the single number in the array.

Examples:-

    Example 1:
    
        Input:
            nums = [1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6]
        Output:
            4
        Explanation: 
            Only the number 4 appears once in the array.
    
    Example 2:
    
        Input: 
            nums = [1, 1, 3, 5, 5]
        Output:
            3
        Explanation: 
            Only the number 3 appears once in the array.
"""

# Function to find the single element in a sorted array
def singleNonDuplicate (nums):
    
    # Size of the given sorted array
    n = len (nums)
    
    # Handle the edge cases
    
    # If the array contains only one element
    # return that element
    if n == 1:
        return nums[0]
    
    # If the array contains only two elements and both of them are distinct
    # return the the element at the 0th index
    if nums[0] != nums[1]:
        return nums[0]
    
    # If the last element differs from the 2nd last element,
    # return the last element
    if nums[n - 1] != nums [n - 2]:
        return nums[n - 1]
    
    # Declare and initialize the low and high pointers to the 2nd element and the 2nd last element, respectively
    lo = 1
    hi = n - 2
    
    # Apply Binary Search
    while (lo <= hi):
        
        # Update the mid value
        mid = (lo + hi) // 2
        
        # If the unique element is the mid element
        if nums[mid] != nums[mid + 1] and nums[mid] != nums[mid - 1]:
            return nums[mid]
        
        # In the left half
        if (mid % 2 == 1 and nums[mid] == nums[mid - 1]) or (mid % 2 == 0 and nums[mid] == nums[mid + 1]):
            
            # Eliminate the left half
            lo = mid + 1
        
        # In the right half
        else:
            
            # Eliminate the right half
            hi = mid - 1
    
    # Return, if the required element is not found
    return -1

# Main Function
def main():
    
    # Take the User Input for the Size of the Array
    n = int (input ("Enter the Size of the Array:\n"))
    
    # Take User Input for the Elements of the Array
    nums = list (map (int, input ("Enter the Elements of the Array:\n").split ()))
    
    # Output
    print (f"{singleNonDuplicate (nums)} is the Single Element in the given Sorted Array.")

if __name__ == "__main__":
    main()

# Sample Input / Output

"""
Input:

Enter the Size of the Array:
n = 7

Enter the Elements of the Array:
nums = 1 2 2 4 4 8 8

Output:

1 is the Single Element in the given Sorted Array.
"""

# Link

"""
Access the Problem:-
    Take U Forward (TUF): https://takeuforward.org/plus/dsa/problems/single-element-in-sorted-array
    Leetcode (Question No. 540): https://leetcode.com/problems/single-element-in-a-sorted-array/description/
    Geeks For Geeks (GFG): https://www.geeksforgeeks.org/problems/find-the-element-that-appears-once-in-sorted-array0624/1
    Naukri Code 360 (Coding Ninjas): https://www.naukri.com/code360/problems/unique-element-in-sorted-array_1112654

Article: https://takeuforward.org/data-structure/search-single-element-in-a-sorted-array/
"""