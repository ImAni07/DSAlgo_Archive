# Search in Rotated Sorted Array - 1

"""
Problem Statement:-

    Given an integer array arr, sorted in ascending order (with distinct values) and a target value k. 
    The array is rotated at some pivot point that is unknown. 
    Find the index at which k is present and if k is not present return -1.

Examples:-

    Example 1:
    
        Input: 
            arr = [4, 5, 6, 7, 0, 1, 2], 
            k = 0
        Output: 
            4
        Explanation: 
            Here, the target is 0. 
            We can see that 0 is present in the given rotated sorted array, arr. 
            Thus, we get output as 4, which is the index at which 0 is present in the array.
    
    Example 2:
    
        Input: 
            arr = [4, 5, 6, 7, 0, 1, 2], 
            k = 3
        Output: 
            -1
        Explanation: 
            Here, the target is 3. 
            Since 3 is not present in the given rotated sorted array. 
            Thus, we get the output as -1.
"""

# Function to search for the given element in a rotated and sorted array
def search (arr, n, k):
    
    # Declare and initialize the required variables
    lo = 0
    hi = n - 1
    
    # Search
    while (lo <= hi):
        mid = (lo + hi) // 2
        
        # If the mid point is equal to the target element
        if arr[mid] == k:
            return mid
        
        # If the left half of the array is sorted
        if arr[lo] <= arr[mid]:
            
            # Check whether the element exists or not
            if arr[lo] <= k and k <= arr[mid]:
                
                # If the element exists
                hi = mid - 1
            
            else:
                # If the element doesn't exist
                lo = mid + 1
        
        # If the right half of the array is sorted
        else:
            if arr[mid] <= k and k <= arr[hi]:
                
                # If the element exists
                lo = mid + 1
            
            else:
                # If the element doesn't exist
                hi = mid - 1
    
    # If the element doesn't exist
    return -1

# Main Function
def main():
    
    # Take User Input for the Size of the Array
    n = int (input ("Enter the Size of the Array:\n"))
    
    # Take User Input for the Elements of the Array
    arr = list (map (int, input ("Enter the Elements of the Array:\n").split ()))
    
    # Take User Input for the Target Value
    k = int (input ("Enter the Target Value:\n"))
    
    # Store the Result
    index = search (arr, n, k)
    
    # Output
    if index == -1:
        print (f"The Target Value {k} is not present in the given Array.")
        print (f"The Index is: {index}")
    else:
        print (f"The Target Value {k} is present in the given Array.")
        print (f"The Index is: {index}")

if __name__ == "__main__":
    main()

# Sample Input / Output

"""
Test Case 1 --> When the Target Value is present

Input:

Enter the Size of the Array:
n = 10

Enter the Elements of the Array:
arr = 5 6 7 8 9 0 1 2 3 4

Enter the Target Value:
k = 3

Output:

The Target Value 3 is present in the given Array.
The Index is: 8

Test Case 2 --> When the Target Value is absent

Input:

Enter the Size of the Array:
n = 4

Enter the Elements of the Array:
arr = 3 4 5 1 2

Enter the Target Value:
k = 6

Output:

The Target Value 6 is not present in the given Array.
The Index is: -1
"""

# Link

"""
Access the Problem:-
    Take U Forward (TUF): https://takeuforward.org/plus/dsa/problems/search-in-rotated-sorted-array-i
    Leetcode (Question No. 33): https://leetcode.com/problems/search-in-rotated-sorted-array/description/
    Geeks For Geeks (GFG): https://www.geeksforgeeks.org/problems/search-in-a-rotated-array4618/1
    Naukri Code 360 (Coding Ninjas): https://www.naukri.com/code360/problems/search-in-rotated-sorted-array_1082554

Article: https://takeuforward.org/data-structure/search-element-in-a-rotated-sorted-array/
"""