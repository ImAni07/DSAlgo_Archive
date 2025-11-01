# Floor and Ceil in Sorted Array

"""
Problem Statement:-

    Given a sorted array arr and an integer x. 
    Find the floor and ceil of x in arr. 
    The floor of x is the largest element in the array which is smaller than or equal to x. 
    The ceiling of x is the smallest element in the array greater than or equal to x. 
    If no floor or ceil exists, output -1.

Examples:-

    Example 1:
    
        Input: 
            arr = [3, 4, 4, 7, 8, 10], 
            x= 5
        Output: 
            4 7
        Explanation: 
            The floor of 5 in the array is 4, and the ceiling of 5 in the array is 7.

    Example 2:

        Input: 
            arr = [3, 4, 4, 7, 8, 10], 
            x= 8
        Output: 
            8 8
        Explanation: 
            The floor of 8 in the array is 8, and the ceiling of 8 in the array is also 8.
"""

# Function to find Floor
def findFloor (arr, n, x):
    
    # Declare the required variables
    lo = 0
    hi = n - 1
    ans_floor = -1
    
    # Traverse through the sorted array
    while lo <= hi:
        
        # Update the value of the mid pointer
        mid = (lo + hi) // 2
        
        # Check whether the mid value of the given array is less than or equal to x, 
        # if yes, then store it in the answer variable
        if arr[mid] <= x:
            ans_floor = arr[mid]
            
            # Check in the right half, for greater values within the range
            lo = mid + 1
        
        else:
            # If the mid value is greater than x, then update the value of the high pointer
            hi = mid - 1
    
    # Return the result
    return ans_floor

# Function to find Ceil
def findCeil (arr, n, x):
    
    # Declare the required variables
    lo = 0
    hi = n - 1
    ans_ceil = -1
    
    # Traverse through the sorted array
    while lo <= hi:
        
        # Update the value of the mid pointer
        mid = (lo + hi) // 2
        
        # Check whether the mid value of the given array is greater than or equal to x, 
        # if yes, then store it in the answer variable
        if arr[mid] >= x:
            ans_ceil = arr[mid]
            
            # Check in the left half, for other suitable values
            hi = mid - 1
        
        else:
            # Check in the right half
            lo = mid + 1
    
    # Return the result
    return ans_ceil

# Function to display the result
def getFloorAndCeil (arr, n, x):
    
    # Store the result of floor
    floor = findFloor(arr, n, x)
    
    # Store the result of ceil
    ceil = findCeil(arr, n, x)
    
    # Return the result
    return (floor, ceil)

# Main Function
def main():
    
    # Take User Input for the Size of the Array
    n = int (input ("Enter the Size of the Array:\n"))
    
    # Take User Input for the Elements of the Array
    arr = list(map(int, input("Enter the Elements of the Array:\n").split()))
    
    # Take User Input for the Target Element
    x = int (input ("Enter the Target Element:\n"))
    
    # Store the Answer
    answer = getFloorAndCeil (arr, n, x)
    
    # Output
    print (f"The Floor of {x} is {answer[0]}")
    print (f"The Ceil of {x} is {answer[1]}")

if __name__ == "__main__":
    main()

# Sample Input / Output

"""
Input:

Enter the Size of the Array:
n = 6

Enter the Elements of the Array:
arr = 3 4 4 7 8 10

Enter the Target Element:
x = 2

Output:

The Floor of 2 is -1
The Ceil of 2 is 3
"""

# Link

"""
Access the Problem:-
    Take U Forward (TUF): https://takeuforward.org/plus/dsa/problems/floor-and-ceil-in-sorted-array
    Naukri Code 360 (Coding Ninjas): https://www.naukri.com/code360/problems/ceiling-in-a-sorted-array_1825401

Article: https://takeuforward.org/arrays/floor-and-ceil-in-sorted-array/
"""