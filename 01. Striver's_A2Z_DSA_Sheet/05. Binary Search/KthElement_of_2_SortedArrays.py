# Kth Element of 2 Sorted Arrays

"""
Problem Statement:-

    # Kth Element of 2 Sorted Arrays
    
    Given two sorted arrays arr1 and arr2 of size n and m respectively. 
    Find the kth element of the final sorted array.

Examples:-

    Example 1:
    
        Input: 
            arr1 = [2, 3, 6, 7, 9], 
            arr2 = [1, 4, 8, 10], 
            k = 5
        Output: 
            6
        Explanation: 
            The final sorted array would be --
                [1, 2, 3, 4, 6, 7, 8, 9, 10]. 
            The 5th element of this array is 6.
    
    Example 2:
    
        Input: 
            arr1 = [100, 112, 256, 349, 770], 
            arr2 = [72, 86, 113, 119, 265, 445, 892], 
            k = 7
        Output: 
            256
        Explanation: 
            Final sorted array is - 
                [72, 86, 100, 112, 113, 119, 256, 265, 349, 445, 770, 892], 
                7th element of this array is 256.
"""

# Function to find the Kth Element of two sorted arrays
def kthElement (arr1, arr2, k):
    
    # Store the size of the two arrayS
    n = len (arr1)
    m = len (arr2)
    
    # Ensure that the first array is smaller than the second one
    if n > m:
        return kthElement (arr2, arr1, k)
    
    # Elements on the left side of the partition
    left_half = k
    
    # Declare and initialize the low and high pointers
    lo = max (0, k - n)
    hi = min (k, m)
    
    # Calculate the total length of the two arrays
    total_length = n + m
    
    # Perform Binary Search
    while lo <= hi:
        
        # Calculate the partition index for the first array
        mid1 = (lo + hi) // 2
        
        # Calculate the partition index for the second array
        mid2 = left_half - mid1
        
        # Calculate the left and right elements of the partition for both arrays
        left1 = float('-inf')
        right1 = float('inf')
        left2 = float('-inf')
        right2 = float('inf')
        
        if mid1 < n:
            right1 = arr1[mid1]
        
        if mid2 < m:
            right2 = arr2[mid2]
        
        if mid1 - 1 >= 0:
            left1 = arr1[mid1 - 1]
        
        if mid2 - 1 >= 0:
            left2 = arr2[mid2 - 1]
        
        # Check if the partition is correct
        if left1 <= right2 and left2 <= right1:
            return max (left1, left2)
        
        # Eliminate the halves
        elif left1 > right2:
            hi = mid1 - 1
        
        else:
            lo = mid1 + 1
    
    # Dummy return statement, if the median is not found
    return -1

# Main Function
def main ():
    
    # Take User Input for the Size of the First Array
    n = int (input ("Enter the Size of the 1st Array:\n"))
    
    # Take User Input for the Elements of the First Array
    arr1 = list (map (int, input ("Enter the Elements of the 1st Array:\n").split ()))
    
    # Take User Input for the Size of the Second Array
    m = int (input ("Enter the Size of the 2nd Array:\n"))
    
    # Take User Input for the Elements of the Second Array
    arr2 = list (map (int, input ("Enter the Elements if the 2nd Array:\n").split ()))
    
    # Take User Input for the value of k
    k = int (input ("Enter the Value of k --> Specify a Position:\n"))
    
    # Print the output
    print (f"The k-th element of two sorted arrays is {kthElement (arr1, arr2, k)}")

if __name__ == "__main__":
    main ()

# Sample Input / Output

"""
Input:

Enter the Size of the 1st Array:
n = 5

Enter the Elements of the 1st Array:
arr1 = 2 3 6 7 9

Enter the Size of the 2nd Array:
m = 4

Enter the Elements of the 2nd Array:
arr2 = 1 4 8 10

Enter the Value of k --> Specify a Position:
k = 5

Output:

The k-th element of two sorted arrays is 6
"""

# Link

"""
Access the Problem:-
    Take U Forward (TUF): https://takeuforward.org/plus/dsa/problems/kth-element-of-2-sorted-arrays
    Geeks For Geeks (GFG): http://geeksforgeeks.org/problems/k-th-element-of-two-sorted-array1317/1
    Naukri Code 360 (Coding Ninjas): https://www.naukri.com/code360/problems/k-th-element-of-2-sorted-array_1164159

Article: https://takeuforward.org/data-structure/k-th-element-of-two-sorted-arrays/
"""