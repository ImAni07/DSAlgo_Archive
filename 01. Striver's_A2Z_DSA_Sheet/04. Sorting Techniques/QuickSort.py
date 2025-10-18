# Quick Sort

"""
Problem Statement:-

    Quick Sorting Algorithm
    
    Given an array of integers, 
    sort the array in non-decreasing order using the quick sort algorithm and 
    return the sorted array.
    
    A sorted array in non-decreasing order is an array where 
    each element is greater than or equal to all preceding elements in the array.

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

# Function for Pivot Element
def partition(nums, low, high):
    
    # Set the 1st element of the array as the pivot element
    pivot_element = nums[low]
    
    # Set a couple of pointers as low and high, to the 1st and the last elements of the array, respectively
    i = low
    j = high
    
    # As long as the pointer of low is less than the pointer of high
    while i < j:
        
        # Check the element greater than the pivot element, from the left side of the array
        while nums[i] <= pivot_element and i < high:
            i += 1
        
        # Check the element smaller than the pivot element, from the right side of the array
        while nums[j] > pivot_element and j > low:
            j -= 1
        
        if i < j:
            
            # Swap the elements at the pointers i and j
            nums[i], nums[j] = nums[j], nums[i]
    
    nums[low], nums[j] = nums[j], nums[low]
    return j

# Function for QuickSort
def quickSort(nums, low, high):
    
    # As long as the Array contains more than 1 element
    if low < high:
        
        # Determining the Partition Index, so that the Left and the Right Subarrays can be sorted
        partition_index = partition (nums, low, high)
        
        # Sorting the Left Subarray
        quickSort(nums, low, partition_index - 1)
        
        # Sorting the Right Subarray
        quickSort(nums, partition_index + 1, high)

# Main Function
def main():
    
    # Take User Input for the Elements of the Array
    nums = list(map(int, input().split()))
    
    # Length of the Array
    n = len (nums)
    
    # Output
    quickSort(nums, 0, n - 1)
    print(*nums)

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
    Take U Forward (TUF): https://takeuforward.org/plus/dsa/problems/quick-sorting
    Geeks For Geeks (GFG): https://www.geeksforgeeks.org/problems/quick-sort/1
    Naukri Code 360 (Coding Ninjas): https://www.naukri.com/code360/problems/quick-sort_983625

Article: https://takeuforward.org/data-structure/quick-sort-algorithm/
"""