# Check if the array is sorted

"""
This question has 2 variants -
    1. Check whether the array is sorted in increasing order
    2. Check whether the array is both sorted and rotated

Variant 1 is available on -
    Take U Forward (TUF)
    Geeks For Geeks (GFG)
    Naukri Code 360 (Coding Ninjas)

Variant 2 is available on - Leetcode (Question No. 1752)
"""

# Variant 1 --> Check whether the array is sorted in increasing order

"""
Problem Statement:-

    Given an array of n integers, return true if the array nums is sorted in non-decreasing order or else false.

Example:-

    Example 1:
    
        Input: 
            nums = [1, 2, 3, 4, 5]
        Output: 
            true
        Explanation: 
            For all i (1 <= i <= 4) it holds nums[i] <= nums[i+1], 
            hence it is sorted and we return true.
    
    Example 2:
    
        Input: 
            nums = [1, 2, 1, 4, 5]
        Output:
            false
        Explanation: 
            For i == 2 it does not hold nums[i] <= nums[i+1], 
            hence it is not sorted and we return false.
"""

# Variant 2 --> Check whether the array is sorted and rotated

"""
Problem Statement:-

    Check if Array is Sorted and Rotated
    
    Given an array, 
    return true if the array was originally sorted in non-decreasing order, then rotated some number of positions (including zero). 
    Otherwise, return false.
    
    There may be duplicates in the original array.
    
    Note: 
        An array A rotated by x positions results in an array B of the same length 
        such that B[i] == A[(i+x) % A.length] for every valid index i.

Examples:-

    Example 1:
    
        Input: 
            nums = [3,4,5,1,2]
        Output: 
            true
        Explanation: 
            [1,2,3,4,5] is the original sorted array.
            You can rotate the array by x = 2 positions to begin on the element of value 3: [3,4,5,1,2].
    
    Example 2:
    
        Input: 
            nums = [2,1,3,4]
        Output: 
            false
        Explanation: 
            There is no sorted array once rotated that can make nums.
    
    Example 3:
    
        Input: 
            nums = [1,2,3]
        Output: 
            true
        Explanation: 
            [1,2,3] is the original sorted array.
        You can rotate the array by x = 0 positions (i.e. no rotation) to make nums.
"""

# Variant 1 --> Check if the Array is sorted

# Function to check whether the given array is sorted or not
def isSorted (a, n):
    
    # Declare and initialize a flag variable to 0
    flag = 0
    
    # Traverse through the array
    for i in range (n-1):
        
        # Check the consecutive elements
        if (a[i] > a[i+1]):
            flag += 1
        
        # Check the value of the flag variable, in order to decide whether further traversal is required or not
        if (flag > 0):
            break
    
    # Check the value of flag and decide whether the given array is sorted or not
    if flag != 0:
        return 0
    else:
        return 1

# Variant 2 --> Check if the Array is Sorted and Rotated

# Function to check if array is sorted and rotated
def isSortedAndRotated(a, n):
    
    # Flag variable
    count = 0
    
    # Check the edge condition
    if a[0] < a[-1]:
        count += 1
    
    # Iterate
    for i in range(n - 1):
        
        # If an element is greater than its next element
        if a[i] > a[i + 1]:
            count += 1
        
        if count > 1:
            return False
    
    return True

# Main Function
def main():
    
    # Take user input for array size
    n = int(input("Enter the size of the array: "))
    
    # Take user input for elements of array
    a = list(map(int, input("Enter the elements: ").split()))
    
    # Check conditions
    if isSorted(a, n):
        
        if isSortedAndRotated(a, n):
            print("The array is sorted as well as rotated.")
        
        else:
            print("The array is sorted but not rotated.")
    
    else:
        print("The array is not sorted, hence not rotated.")

if __name__ == "__main__":
    main()

# Sample Input / Output

"""
Test Case 1:

Input:

Enter the size of the array: 
n = 5 
Enter the elements: 
a = 1 2 3 4 5

Output:

The array is sorted as well as rotated.

Test Case 2:

Input:

Enter the size of the array: 
n = 6
Enter the elements: 
a = 90 80 70 100 20 50

Output:

The array is not sorted, hence not rotated.
"""

# Links

"""
Access the Problem:-

Variant 1 --> Check the Array is Sorted or not in Increasing Order
    Take U Forward (TUF): https://takeuforward.org/plus/dsa/problems/check-if-the-array-is-sorted-ii
    Geeks For Geeks (GFG): https://www.geeksforgeeks.org/problems/check-if-an-array-is-sorted0701/1
    Naukri Code 360 (Coding Ninjas): https://www.naukri.com/code360/problems/ninja-and-the-sorted-check_6581957

Variant 2 --> Check the Array is Sorted and Rotated
    Leetcode (Question No. - 1725): https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/description/

Article: https://takeuforward.org/data-structure/check-if-an-array-is-sorted/
"""