# Count Occurrences in Sorted Array
# Number of Occurrence

"""
Problem Statement:-

    You are given a sorted array of integers arr and an integer target (x). 
    Your task is to determine how many times target (x) appears in arr.
    Return the count of occurrences of target (x) in the array.

Examples:-

    Example 1:
    
        Input: 
            arr = [0, 0, 1, 1, 1, 2, 3], 
            x = 1
        Output: 
            3
        Explanation: 
            The number 1 appears 3 times in the array.
    
    Example 2:
    
        Input: 
            arr = [5, 5, 5, 5, 5, 5], 
            x = 5
        Output: 
            6
        Explanation: 
            All elements in the array are 5, so the target appears 6 times.
"""

# Function to find the 1st occurrence
def firstOccurrence (arr, n, x):
    
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

# Function to find the Last Occurrence
def lastOccurrence (arr, n, x):
    
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
    first = firstOccurrence(arr, n, x)
    
    # Check whether the first occurrence is available or not
    if first == -1:
        return [-1, -1]
    
    # Store the result of the last occurrence
    last = lastOccurrence(arr, n, x)
    
    # Return the result
    return [first, last]

# Function to count the number of times the target number occur
def countOccurrences (arr, n, x):
    
    # Store the first and the last occurrence of the target number in the respective variables
    first, last = firstAndLastPosition (arr, n, x)
    
    # Check if the first occurrence is equal to -1 or not
    if first == -1:
        return 0
    
    # Otherwise, return the required difference
    else:
        return last - first + 1

# Main Function
def main():
    
    # Take User Input for the Size of the Array
    n = int (input ("Enter the Size of the Array:\n"))
    
    # Take User Input for the Elements of the Array
    arr = list (map (int, input ("Enter the Elements of the Array:\n").split ()))
    
    # Take User Input for the Target Value
    x = int (input ("Enter the Target Value:\n"))
    
    # Output
    print (f"Number of Times the Target Value {x} occurs in the given Sorted Array is: {countOccurrences (arr, n, x)}")

if __name__ == "__main__":
    main()

# Sample Input / Output

"""
Test Case 1 --> When the Target Element is Present

Input:

Enter the Size of the Array:
n = 6

Enter the Elements of the Array:
arr = 1 1 2 2 2 2

Enter the Target Value:
x = 2

Output:

Number of Times the Target Value 2 occurs in the given Sorted Array is: 4

Test Case 2 --> When the Target Element is not Present

Input:

Enter the Size of the Array:
n = 6

Enter the Elements of the Array:
arr = 1 1 2 2 2 2

Enter the Target Value:
x = 4

Output:

Number of Times the Target Value 2 occurs in the given Sorted Array is: 0
"""

# Link

"""
Access the Problem:-
    Take U Forward (TUF): https://takeuforward.org/plus/dsa/problems/count-occurrences-in-a-sorted-array
    Geeks For Geeks (GFG): https://www.geeksforgeeks.org/problems/number-of-occurrence2259/1
    Naukri Code 360 (Coding Ninjas): https://www.naukri.com/code360/problems/occurrence-of-x-in-a-sorted-array_630456

Article: https://takeuforward.org/data-structure/count-occurrences-in-sorted-array/
"""