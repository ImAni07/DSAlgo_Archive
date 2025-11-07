# Median of 2 Sorted Arrays

"""
Problem Statement:-

    Median of 2 sorted arrays
    
    Given two sorted arrays nums1 and nums2 of size n1 and n2 respectively, return the median of the two sorted arrays.
    The median is defined as the middle value of a sorted list of numbers. 
    In case the length of the list is even, the median is the average of the two middle elements.

Examples:-

    Example 1:
    
        Input: 
            nums1 = [2, 4, 6], 
            nums2 = [1, 3, 5]
        Output: 
            3.5
        Explanation: 
            The array after merging nums1 and nums2 will be --
                [ 1, 2, 3, 4, 5, 6 ]. 
            As the length of the merged list is even, the median is the average of the two middle elements. 
            Here two medians are 3 and 4. 
            So the median will be the average of 3 and 4, which is 3.5.
    
    Example 2:
    
        Input: 
            nums1 = [2, 4, 6], 
            nums2 = [1, 3]
        Output: 
            3.0
        Explanation: 
            The array after merging nums1 and nums2 will be --
                [ 1, 2, 3, 4, 6 ]. 
            The median is simply 3.
"""

# Function to find the median of two sorted arrays
def findMedianSortedArrays (nums1, nums2):
    
    # Store the size of the two arrayS
    n1 = len (nums1)
    n2 = len (nums2)
    
    # Ensure that the first array is smaller than the second one
    if n1 > n2:
        return findMedianSortedArrays (nums2, nums1)
    
    # Declare and initialize the low and high pointers
    lo = 0
    hi = n1
    
    # Calculate the total length of the two arrays
    n = n1 + n2
    
    # Elements on the left side of the partition
    left_half = (n1 + n2 + 1) // 2
    
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
        
        if mid1 < n1:
            right1 = nums1[mid1]
        
        if mid2 < n2:
            right2 = nums2[mid2]
        
        if mid1 - 1 >= 0:
            left1 = nums1[mid1 - 1]
        
        if mid2 - 1 >= 0:
            left2 = nums2[mid2 - 1]
        
        # Check if the partition is correct
        if left1 <= right2 and left2 <= right1:
            
            # If the total length is odd, 
            # return the median
            if n % 2 == 1:
                return max (left1, left2)
            
            # If the total length is even, 
            # return the average of the two medians
            else:
                return (float (max (left1, left2) + min (right1, right2))) / 2
        
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
    n1 = int (input ("Enter the Size of the 1st Array:\n"))
    
    # Take User Input for the Elements of the First Array
    nums1 = list (map (int, input ("Enter the Elements of the 1st Array:\n").split ()))
    
    # Take User Input for the Size of the Second Array
    n2 = int (input ("Enter the Size of the 2nd Array:\n"))
    
    # Take User Input for the Elements of the Second Array
    nums2 = list (map (int, input ("Enter the Elements of the 2nd Array:\n").split ()))
    
    # Print the output
    print (f"The Median of 2 Sorted Arrays is {findMedianSortedArrays (nums1, nums2)}")

if __name__ == "__main__":
    main ()

# Sample Input / Output

"""
Input:

Enter the Size of the 1st Array:
n1 = 2

Enter the Elements of the 1st Array:
nums1 = 1 2

Enter the Size of the 2nd Array:
n2 = 2

Enter the Elements of the 2nd Array:
nums2 = 3 4

Output:

The Median of 2 Sorted Arrays is 2.5
"""

# Link

"""
Access the Problem:-
    Take U Forward (TUF): https://takeuforward.org/plus/dsa/problems/median-of-2-sorted-arrays
    Leetcode (Question No. 4): https://leetcode.com/problems/median-of-two-sorted-arrays/description/
    Naukri Code 360 (Coding Ninjas): https://www.naukri.com/code360/problems/median-of-two-sorted-arrays_985294

Article: https://takeuforward.org/data-structure/median-of-two-sorted-arrays-of-different-sizes/
"""