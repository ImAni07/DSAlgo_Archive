# Peak Element

"""
Problem Statement:-

    Find Peak Element
    
    Given an array nums of integers. 
    A peak element is defined as an element greater than both of its neighbors.
    Formally, if arr[i] is the peak element, arr[i - 1] < arr[i] and arr[i + 1] < arr[i].
    Find the index(0-based) of a peak element in the array. 
    If there are multiple peak numbers, return the index of any peak number.

Examples:-

    Example 1:
    
        Input: 
            nums = [1, 2, 3, 4, 5, 6, 7, 8, 5, 1]
        Output: 
            7
        Explanation: 
            In this example, there is only 1 peak that is at index 7.
    
    Example 2:
    
        Input: 
            nums = [1, 2, 1, 3, 5, 6, 4]
        Output: 
            1
        Explanation: 
            In this example, there are 2 peak numbers at indices 1 and 5. We can consider any of them.
"""

# Function to find Peak Element
def findPeakElement (nums):
    
    """
        Peak Element:-
            if the ith element of the given array is greater than its previous as well as the next element
    """
    
    # Size of the given array
    n = len (nums)
    
    # Handle the edge cases
    
    # If the array contains only one element
    if n == 1:
        return nums [0]
    
    # If the the 1st element is the highest
    if nums [0] > nums [1]:
        return nums [0]
    
    # If the last element is greater than the second last element
    if nums [n - 1] > nums [n - 2]:
        return nums [n - 1]
    
    # Declare and initialize the low and high pointer to the 2nd and the 2nd last element
    lo = 1
    hi = n - 2
    
    # Apply Binary Search
    while lo <= hi:
        
        # Update the mid value
        mid = (lo + hi) // 2
        
        # If mid element is greater than next
        if nums[mid] > nums[mid + 1]:
            
            # Move to left half
            hi = mid
        
        else:
            # Move to right half
            lo = mid + 1

        # Return peak index
        return lo

# Main Function
def main():
    
    # Take User Input for the Size of the Array
    n = int (input ("Enter the Size of the Array:\n"))
    
    # Take User Input for the Elements of the Array
    nums = list (map (int, input ("Enter the Elements of the Array:\n").split ()))
    
    # Output
    print (f"The Index of the Peak Element is:\n{findPeakElement (nums)}")

if __name__ == "__main__":
    main()

# Sample Input / Output

"""
Input:

Enter the Size of the Array:
n = 4

Enter the Elements of the Array:
nums = 1 2 3 1

Output:

The Index of the Peak Element is:
2
"""

# Link

"""
Access the Problem:-
    Take U Forward (TUF): https://takeuforward.org/plus/dsa/problems/find-peak-element
    Leetcode (Question No. 162): https://leetcode.com/problems/find-peak-element/description/
    Geeks For Geeks (GFG): https://www.geeksforgeeks.org/problems/peak-element/1
    Naukri Code 360 (Coding Ninjas): https://www.naukri.com/code360/problems/find-peak-element_1081482

Article: https://takeuforward.org/data-structure/peak-element-in-array/
"""