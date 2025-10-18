# Merge Sort

"""
Problem Statement:-

    Merge Sorting Algorithm
    
    Given an array of integers, 
    sort the array in non-decreasing order using the merge sort algorithm. 
    Return the sorted array.
    
    A sorted array in non-decreasing order is one in which 
    each element is either greater than or equal to all the elements to its left in the array.

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

# Function to perform the Merge
def merge (nums, lo, mid, hi):
    
    # A temporary array to store the merged array
    temp = []
    
    # Assign left and right pointers, 
    # to the starting point of the sorted arrays of both left and right halves, respectively
    left = lo
    right = mid + 1
    
    # Compare the elements of both the halves
    while left <= mid and right <= hi:
        if nums[left] <= nums[right]:
            temp.append(nums[left])
            left += 1
        else:
            temp.append(nums[right])
            right += 1
    
    # Fill the left out elements (for left half sorted array)
    while left <= mid:
        temp.append(nums[left])
        left += 1
    
    # Fill the left out elements (for right half sorted array)
    while right <= hi:
        temp.append(nums[right])
        right += 1
    
    # Transferring all elements from the temporary array to the actually array
    for i in range(lo, hi + 1):
        nums[i] = temp[i - lo]

# Function to perform the Merge Sort
def mergeSort (nums, lo, hi):
    
    # Base Case
    if lo >= hi:
        return
    
    mid = int ((lo + hi) / 2)
    
    # Sort the Left Half of the Array, recursively
    mergeSort (nums, lo, mid)
    
    # Sort the Right Half of the Array, recursively
    mergeSort (nums, mid + 1, hi)
    
    # Merge both the sorted halves of the Array
    merge (nums, lo, mid, hi)

# Main Function
def main():
    
    # Take User Input for the Elements of the Array
    nums = list (map (int, input ().split ()))
    
    # Length of the Array
    n = len (nums)
    
    # Output
    mergeSort (nums, 0, n - 1)
    print (*nums)

if __name__ == "__main__":
    main()

# Sample Input / Output

"""
Input:
7 4 1 5 3

Output:
1 3 4 5 7
"""

# Links

"""
Access the Problem:-
    Take U Forward (TUF): https://takeuforward.org/plus/dsa/problems/merge-sorting
    Geeks For Geeks (GFG): https://www.geeksforgeeks.org/problems/merge-sort/1
    Naukri Code 360 (Coding Ninjas): https://www.naukri.com/code360/problems/merge-sort_920442

Article: https://takeuforward.org/data-structure/merge-sort-algorithm/
"""