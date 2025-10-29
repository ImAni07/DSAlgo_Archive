# Reverse Pairs

"""
Problem Statement:-

    Given an integer array a. 
    Return the number of reverse pairs in the array.
    
    An index pair (i, j) is called a reverse pair if:
        0 <= i < j < a.length
        a[i] > 2 * a[j]

Examples:-

    Example 1:

        Input: 
            a = [6, 4, 1, 2, 7]
        Output: 
            3
        Explanation:
            The reverse pairs are:
                (0, 2): a[0] = 6, a[2] = 1, 6 > 2 * 1
                (0, 3): a[0] = 6, a[3] = 2, 6 > 2 * 2
                (1, 2): a[1] = 4, a[2] = 1, 4 > 2 * 1
    
    Example 2:
    
        Input: 
            a = [5, 4, 4, 3, 3]
        Output: 
            0
        Explanation:
            No pairs satisfy both the conditions.
"""

# Function to perform the Merge
def mergeAndCount (a, temp, start, mid, end):
    
    # Declare and initialize the required pointers
    i = start
    j = mid + 1
    k = start
    inversion_count = 0
    
    # Count the valid number of pairs
    while i <= mid and j <= end:
        
        # Check whether the ith element is greater than twice the jth element
        if a[i] > 2 * a[j]:
            inversion_count += (mid - i + 1)
            j += 1
        
        else:
            i += 1
    
    # Reset the pointers
    i = start
    j = mid + 1
    
    # Merge both the halves into the temporary array
    while i <= mid and j <= end:
        
        if a[i] <= a[j]:
            temp[k] = a[i]
            i += 1
        
        else:
            temp[k] = a[j]
            j += 1
        
        k += 1
    
    # If elements are left in the left subarray
    while i <= mid:
        temp[k] = a[i]
        i += 1
        k += 1
    
    # If elements are left in the right subarray
    while j <= end:
        temp[k] = a[j]
        j += 1
        k += 1
    
    # Store the sorted temporary array into the original array
    for i in range(start, end + 1):
        a[i] = temp[i]
    
    # Return the number of reverse pairs
    return inversion_count

def mergeSortAndCount (a, temp, start, end):
    
    # Initialize the inversion count to 0
    inversion_count = 0
    
    # Check if the value of the left pointer is less than the value of the right pointer
    if start < end:
        
        # Determine the mid point
        mid = (start + end) // 2
        
        # For Left Subarray
        inversion_count += mergeSortAndCount (a, temp, start, mid)
        
        # For Right Subarray
        inversion_count += mergeSortAndCount (a, temp, mid + 1, end)
        
        # For Merging and Counting
        inversion_count += mergeAndCount (a, temp, start, mid, end)
    
    # Return the result
    return inversion_count

# Function to perform the operation
def reversePairs (skill, n):
    
    # Create a list of skills
    temp = [0] * n
    
    # Return the Sorted Array and the required count
    return mergeSortAndCount (skill, temp, 0, n-1)

# Main Function
def main():
    # Take User Input for the Size of the Array
    n = int(input("Enter the Size of the Array:\n"))
    
    # Take User Input for the Elements of the Array
    a = list(map(int, input("Enter the Elements of the Array:\n").split()))
    
    # Output
    print(f"The Number of Reverse Pairs:\n{reversePairs (a, n)}")

if __name__ == "__main__":
    main()

# Sample Input / Output:

"""
Input:

Enter the Size of the Array:
n = 5

Enter the Elements of the Array:
a = 1 3 2 3 1

Output:

The Number of Reverse Pairs:
2
"""

# Link

"""
Access the Problem:-
    Take U Forward (TUF): https://takeuforward.org/plus/dsa/problems/reverse-pairs
    Leetcode (Question No. 493): https://leetcode.com/problems/reverse-pairs/description/
    Geeks For Geeks (GFG): https://www.geeksforgeeks.org/problems/count-reverse-pairs/1
    Naukri Code 360 (Coding Ninjas): https://www.naukri.com/code360/problems/reverse-pairs_1112652

Article: https://takeuforward.org/data-structure/count-reverse-pairs/
"""