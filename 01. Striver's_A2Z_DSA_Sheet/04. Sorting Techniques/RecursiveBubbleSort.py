# Recursive Bubble Sort

"""
Problem Statement:-

    Bubble Sort Algorithm using Recursion
    
    Given an array of integers, 
    sort the array in non-decreasing order using the recursive Bubble Sort algorithm, and 
    return the sorted array.
    
    You must implement Bubble Sort using recursion only.
    Do not use built-in sorting functions (sort, sorted, Arrays.sort, etc.).
    A sorted array in non-decreasing order is an array where each element is greater than or equal to the previous one.

Examples:-

    Example 1:
    
        Input: 
            nums = [7, 4, 1, 5, 3]
        Output: 
            [1, 3, 4, 5, 7]
        Explanation: 
            1 <= 3 <= 4 <= 5 <= 7.
            Thus the array is sorted in non-decreasing order.
    
    Example 2:
    
        Input: 
            nums = [5, 4, 4, 1, 1]
        Output: 
            [1, 1, 4, 4, 5]
        Explanation: 
            1 <= 1 <= 4 <= 4 <= 5.
            Thus the array is sorted in non-decreasing order.
"""

# Function to implement the bubble sort algorithm recursively
def bubble_sort_recursive(nums, n=None, i=0):
    
    # Initialize n on the first call
    if n is None:
        n = len(nums)
    
    # Base case: when only one element is left
    if n == 1:
        return nums
    
    # Inner recursion: traverse the array and bubble up the largest element
    if i < n - 1:
        
        # Check for the greater element, when it is out of order
        if nums[i] > nums[i + 1]:
            
            # Swap
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
        
        # Recur for the next index
        return bubble_sort_recursive(nums, n, i + 1)
    
    # Outer recursion: restart inner recursion for the next pass
    return bubble_sort_recursive(nums, n - 1, 0)

# Main Function
def main ():
    
    # Take User Input for the Elements of the Array
    nums = list (map (int, input ().split ()))
    
    # Output
    print(bubble_sort_recursive(nums))

if __name__ == "__main__":
    main ()

# Sample Input / Output

"""
Input:
5 4 4 1 1

Output:
[1, 1, 4, 4, 5]
"""

# Links

"""
Access the Problem:-
    Take U Forward (TUF): https://takeuforward.org/plus/dsa/problems/recursive-bubble-sort

Article: https://takeuforward.org/arrays/recursive-bubble-sort-algorithm/
"""