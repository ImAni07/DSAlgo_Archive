# Count Inversions in an Array

"""
Problem Statement:-

    Count Inversions
    
    Given an integer array a. 
    Return the number of inversions in the array.
    
    Two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j.
        It indicates how close an array is to being sorted.
        A sorted array has an inversion count of 0.
        An array sorted in descending order has maximum inversion.

Examples:-

    Example 1:
    
        Input: 
            a = [2, 3, 7, 1, 3, 5]
        Output: 
            5
        Explanation:
            The responsible indexes are:
                a[0], a[3], values: 2 > 1 & indexes: 0 < 3
                a[1], a[3], values: 3 > 1 & indexes: 1 < 3
                a[2], a[3], values: 7 > 1 & indexes: 2 < 3
                a[2], a[4], values: 7 > 3 & indexes: 2 < 4
                a[2], a[5], values: 7 > 5 & indexes: 2 < 5
    
    Example 2:
    
        Input: 
            a = [-10, -5, 6, 11, 15, 17]
        Output: 
            0
        Explanation:
            a is sorted, hence no inversions present.
"""

# Function to perform the Merge
def merge(a, start, mid, end):
    
    # Temporary lists for left and right subarrays
    left_subarray = a[start:mid + 1]
    right_subarray = a[mid + 1:end + 1]
    
    # Pointers for left_sub, right_sub and main array
    i = 0
    j = 0
    k = start
    inversions = 0
    
    # Merge the subarrays back into a
    while i < len(left_subarray) and j < len(right_subarray):
        
        # If the ith element of the left subarray is less than equal to the jth element of the right subarray
        if left_subarray[i] <= right_subarray[j]:
            a[k] = left_subarray[i]
            i += 1
        
        # If the ith element of the left subarray is greater than the jth element of the right subarray
        else:
            a[k] = right_subarray[j]
            j += 1
            
            # Count Inversions
            inversions += (mid - start + 1 - i)
        
        # Increment the k pointer, traversing in the main array
        k += 1
    
    # Copy any remaining elements of left_sub
    while i < len(left_subarray):
        a[k] = left_subarray[i]
        i += 1
        k += 1
    
    # Copy any remaining elements of right_sub
    while j < len(right_subarray):
        a[k] = right_subarray[j]
        j += 1
        k += 1
    
    return inversions

# Function to perform Merge Sort and count inversions
def mergeSort(a, start, end):
    
    # Declare a variable to count the number of inversions and initialize it to 0
    inversions = 0
    
    # If the value of the start pointer is less than the value of the end pointer
    if start < end:
        
        # Determine the mid
        mid = (start + end) // 2
        inversions += mergeSort(a, start, mid)
        inversions += mergeSort(a, mid + 1, end)
        inversions += merge(a, start, mid, end)
    
    # Return the inversions
    return inversions

# Function to count the Number of Inversions
def numberOfInversions(a, n):
    
    # Count the Number of Pairs
    return mergeSort(a, 0, n - 1)

# Main Function
def main():
    # Take User Input for the Size of the Array
    n = int(input("Enter the Size of the Array:\n"))
    
    # Take User Input for the Elements of the Array
    a = list(map(int, input("Enter the Elements of the Array:\n").split()))
    
    # Output
    print(f"The Number of Inversions:\n{numberOfInversions(a, n)}")

if __name__ == "__main__":
    main()

# Sample Input / Output

"""
Input:

Enter the Size of the Array:
n = 5

Enter the Elements of the Array:
a = 2 4 1 3 5

Output:

The Number of Inversions:
3
"""

# Link

"""
Access the Problem:-
    Take U Forward (TUF): https://takeuforward.org/plus/dsa/problems/count-inversions
    Geeks For Geeks (GFG): https://www.geeksforgeeks.org/problems/inversion-of-array-1587115620/1
    Naukri Code 360 (Coding Ninjas): https://www.naukri.com/code360/problems/count-inversions_615?leftPanelTabValue=PROBLEM

Article: https://takeuforward.org/data-structure/count-inversions-in-an-array/
"""