# First and Last Occurrence
# Find the First and the Last Occurrence of a Target Key in a Sorted Array

"""
Problem Statement:-

    Given an array of integers arr sorted in non-decreasing order, 
        find the starting and ending position of a given target value. 
    If the target is not found in the array, return [-1, -1].

Examples:-

    Example 1:
    
        Input: 
            arr = [5, 7, 7, 8, 8, 10], 
            target = 8
        Output: 
            [3, 4]
        Explanation:
            The target is 8, and it appears in the array at indices 3 and 4.
            Therefore, the output is [3,4]
    
    Example 2:

        Input: 
            arr = [5, 7, 7, 8, 8, 10], 
            target = 6
        Output: 
            [-1, -1]
        Expalantion: 
            The target is 6, which is not present in the array. 
            Therefore, the output is [-1, -1].
"""

# Function to find the First Occurrence of a Target Key in the given Sorted Array
def findFirst (arr, n, x):
    
    # Initialize the low and the high pointers
    lo = 0
    hi = n - 1
    
    # Initialize a variable to store the result of the first occurrence to -1 
    # default assumption: target not present
    first = -1
    
    # Traverse through the given sorted array
    while lo <= hi:
        
        # Find out the value of mid
        mid = (lo + hi) // 2
        
        # Check if the value present at the mid index is equal to the target value
        if arr[mid] == x:
            
            # Update the value of the result
            first = mid
            
            # Search for other index, in the left half of the array
            hi = mid - 1
        
        # If the value present at the mid index is less than the target value
        elif arr[mid] < x:
            lo = mid + 1
        
        # If the value present at the mid index is more than the target value
        else:
            hi = mid - 1
    
    # Return the answer
    return first

# Function to find the Last Occurrence of a Target Key in the given Sorted Array
def findLast (arr, n, x):
    
    # Initialize the low and the high pointers
    lo = 0
    hi = n - 1
    
    # Initialize a variable to store the result of the last occurrence to -1 
    # default assumption: target not present
    last = -1
    
    # Traverse through the given sorted array, until the left pointer crosses over the right
    while lo <= hi:
        
        # Find out the value of mid
        mid = (lo + hi) // 2
        
        # Check if the value present at the mid index is equal to the target value
        if arr[mid] == x:
            
            # Update the value of the result
            last = mid
            
            # Search for other index, in the right half of the array
            lo = mid + 1
        
        # If the value present at the mid index is more than the target value
        elif arr[mid] > x:
            hi = mid - 1
        
        # If the value present at the mid index is less than the target value
        else:
            lo = mid + 1
    
    # Return the answer
    return last

# Function to find out both the first as well as the last occurrence of the given target value from a given sorted array
def firstAndLastPosition (arr, n, x):
    
    # Store the result of the first occurrence
    first = findFirst(arr, n, x)
    
    # Check whether the first occurrence is available or not
    if first == -1:
        return [-1, -1]
    
    # Store the result of the last occurrence
    last = findLast(arr, n, x)
    
    # Return the result
    return [first, last]

# Main Function
def main():
    
    # Take User Input for the Size of the Array
    n = int (input ("Enter the Size of the Array:\n"))
    
    # Take User Input for the Elements of the Array
    arr = list (map (int, input ("Enter the Elements of the Array\n").split ()))
    
    # Take User Input for the Target Value
    x = int (input ("Enter the Target Element:\n"))
    
    # Store the result
    result = firstAndLastPosition (arr, n, x)
    
    # Output
    if result[0] == -1:
        print(f"The Target Element {x} is not present in the given Sorted Array.")
        print(f"Therefore the First Occurrence {x} is {result[0]}")
        print(f"The Last Occurrence of {x} is {result[1]}")
    else:
        print(f"The Target Element {x} is present in the given Sorted Array.")
        print(f"The First Occurrence of {x} is {result[0]}")
        print(f"The Last Occurrence of {x} is {result[1]}")

if __name__ == "__main__":
    main()

# Sample Input / Output

"""
Test Case 1 --> When Target is Present (Multiple Times)

Input:

Enter the Size of the Array:
n = 12

Enter the Elements of the Array:
arr = 0 1 2 3 4 4 5 6 6 7 8 8 9 10

Enter the Target Element:
x = 6

Output:

The Target Element 6 is present in the given Sorted Array.
The First Occurrence of 6 is 7
The Last Occurrence of 6 is 8

Test Case 1 --> When Target is Present (Single Time)

Input:

Enter the Size of the Array:
n = 12

Enter the Elements of the Array:
arr = 0 1 2 3 4 4 5 6 6 7 8 8 9 10

Enter the Target Element:
x = 7

Output:

The Target Element 7 is present in the given Sorted Array.
The First Occurrence of 7 is 9
The Last Occurrence of 7 is 9

Test Case 1 --> When Target is Absent

Input:

Enter the Size of the Array:
n = 12

Enter the Elements of the Array:
arr = 0 1 2 3 4 4 5 6 6 7 8 8 9 10

Enter the Target Element:
x = 12

Output:

The Target Element 12 is not present in the given Sorted Array.
Therefore the First Occurrence of 12 is -1
The Last Occurrence of 12 is -1
"""

# Link

"""
Access the Problem:-
    Take U Forward (TUF): https://takeuforward.org/plus/dsa/problems/first-and-last-occurrence
    Leetcode (Question No. 34): https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
    Geeks For Geeks (GFG): https://www.geeksforgeeks.org/problems/first-and-last-occurrences-of-x3116/1
    Naukri Code 360 (Coding Ninjas): https://www.naukri.com/code360/problems/first-and-last-position-of-an-element-in-sorted-array_1082549

Article: https://takeuforward.org/data-structure/last-occurrence-in-a-sorted-array/
"""