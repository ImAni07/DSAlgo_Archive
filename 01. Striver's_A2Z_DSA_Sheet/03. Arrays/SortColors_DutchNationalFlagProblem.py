# Sort Colors 
# Dutch National Flag Problem
# Sort an Array of 0s, 1s and 2s

"""
Problem Statement:-

    Sort an array of 0's 1's and 2's
    Sort Colors
    Dutch National Flag Problem
    
    Given an array consisting of only 0, 1, or 2. 
    Sort the array in non-decreasing order.
    
    The sorting must be done in-place, without making a copy of the original array.

Examples:-

    Example 1:
    
        Input: 
            arr = [1, 0, 2, 1, 0]
        Output: 
            [0, 0, 1, 1, 2]
        Explanation:
            The array in sorted order has 2 zeroes, 2 ones and 1 two
    
    Example 2:
    
        Input: 
            arr = [0, 0, 1, 1, 1]
        Output: 
            [0, 0, 1, 1, 1]
        Explanation:
            The array in sorted order has 2 zeroes, 3 ones and zero twos
"""

# Function to Sort the Colors (Dutch Flag Pattern) or (Sorting 0 1 2) within the given array
def sort012 (arr, n):
    
    # Using the 3-pointer approach, 
    # declare and initialize 3 pointers - lo, mid and hi, 
    # where lo and mid both equals to 0 and hi equals to the size
    
    lo = 0
    mid = 0
    hi = n - 1
    
    # Traverse the array, 
    # as long as the index value of the mid pointer is less than equal to the high pointer
    while mid <= hi:
        
        # Check the value of the mid pointer, 
        if arr[mid] == 0:
            
            # Swap
            arr[lo], arr[mid] = arr[mid], arr[lo]
            
            # increment both of them by 1
            lo += 1
            mid += 1
        
        # Check the value of the mid pointer, 
        # if it is equal to 1, 
        # then just increment the value of the mid pointer by 1
        
        elif arr[mid] == 1:
            mid += 1
        
        # Check the value of the mid pointer, 
        # if it is equal to 2, 
        # then swap the values of mid and high
        # decrease the value of high pointer by 1
        
        else:
            arr[mid], arr[hi] = arr[hi], arr[mid]
            hi -= 1

# Function to print the Answer
def printArray(arr, n):
    
    # Traverse through the sorted array
    for i in range (n):
        
        # Print the elements of the array
        print (arr[i], end=" ")
    
    # For new line
    print ()

# Main Function
def main():
    
    # Take User Input for the Size of the Array
    n = int (input("Enter the Size:\n").strip())
    
    # Take User Input for the Elements of the Array
    arr = list(map(int, input("Enter the 0s, 1s and 2s:\n").strip().split()))
    
    # Output
    print("\nResult:")
    sort012 (arr, n)
    printArray (arr, n)

if __name__ == "__main__":
    main ()

# Sample Input / Output

"""
Input:

Enter the Size:
n = 6

Enter the 0s, 1s and 2s:
arr = 2 0 2 1 1 0

Result:
0 0 1 1 2 2
"""

# Link

"""
Access the Problem:-
    Take U Forward (TUF): https://takeuforward.org/plus/dsa/problems/sort-an-array-of-0's-1's-and-2's
    Leetcode (Question No. 75): https://leetcode.com/problems/sort-colors/description/
    Geeks For Geeks (GFG): https://www.geeksforgeeks.org/problems/sort-an-array-of-0s-1s-and-2s4231/1
    Naukri Code 360 (Coding Ninjas): https://www.naukri.com/code360/problems/sort-an-array-of-0s-1s-and-2s_892977

Article: https://takeuforward.org/data-structure/sort-an-array-of-0s-1s-and-2s/
"""