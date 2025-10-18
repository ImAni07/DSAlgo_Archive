# Recursive Insertion Sort

"""
Problem Statement:-

    Insertion Sort Algorithm implementation recurisively
    
    Given an array of integers, 
    sort the array in non-decreasing order using the recursive Insertion Sort algorithm, and 
    return the sorted array.
    
    You must implement Insertion Sort using recursion only.
    Do not use loops (like for or while) or built-in sorting functions (sort, Arrays.sort, etc.).
    A sorted array in non-decreasing order is an array where each element is greater than or equal to all elements that come before it.
"""

# Function to perform the insert recursively
def recursive_insert(nums, n, last):
    
    # Base case: when position found or j < 0
    if n < 0 or nums[n] <= last:
        nums[n + 1] = last
        return
    
    # Shift element right
    nums[n + 1] = nums[n]
    
    # Recursive call for previous index
    recursive_insert(nums, n - 1, last)

# Function to perform the insertion sort
def insertionSort(nums, n=None):
    
    # Initialize n during first call
    if n is None:
        n = len(nums)
    
    # Base case: array of size 1 is already sorted
    if n <= 1:
        return nums
    
    # Recursively sort first n-1 elements
    insertionSort(nums, n - 1)
    
    # Insert the nth element into its correct position
    last = nums[n - 1]
    recursive_insert(nums, n - 2, last)
    
    # Return
    return nums

# Main Function
def main ():
    
    # Take User Input for the Elements of the Array
    nums = list (map (int, input ().split ()))
    
    # Output
    print(insertionSort(nums))

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
    Take U Forward (TUF): https://takeuforward.org/plus/dsa/problems/recursive-insertion-sort

Article: https://takeuforward.org/arrays/recursive-insertion-sort-algorithm/
"""