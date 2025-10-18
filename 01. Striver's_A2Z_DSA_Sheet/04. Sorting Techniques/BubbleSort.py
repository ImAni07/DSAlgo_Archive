# Bubble Sort

"""
Problem Statement:-

    Bubble Sort Algorithm
    
    Given an array of integers,
    sort the array in non-decreasing order using the bubble sort algorithm and 
    return the sorted array.
    
    A sorted array in non-decreasing order is an array 
    where each element is greater than or equal to all preceding elements in the array.

Examples:-

    Example 1:
    
        Input:
            n = 5
            arr = [7, 4, 1, 5, 3]

        Output: 
            [1, 3, 4, 5, 7]

        Explanation: 
            1 <= 3 <= 4 <= 5 <= 7.
            Thus the array is sorted in non-decreasing order.
    
    Example 2:
    
        Input:
            n = 5
            arr = [5, 4, 4, 1, 1]

        Output: 
            [1, 1, 4, 4, 5]

        Explanation: 
            1 <= 1 <= 4 <= 4 <= 5.
            Thus the array is sorted in non-decreasing order.
"""

# Function to implement Bubble Sort Algorithm to sort the array
def bubbleSort (arr):
    
    # Outer Loop --> Select the Range
    for i in range ((len (arr) - 1), 0, -1):
        
        # Inner Loop --> Sorting
        for j in range (i):
            
            # Check for the greater element, when it is out of order
            if (arr[j] > arr[j + 1]):
                
                # Swap
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    # Return the sorted array
    return arr

# Main Function
def main ():
    
    # Take User Input for the Size of the Array
    n = int (input ("Enter the Size of the Array:"))
    
    # Take User Input for the Elements of the Array
    arr = list(map(int, input("Enter the elements of the array: ").split()))
    
    # Print
    print (f"\nThe sorted array is:\n{bubbleSort(arr)}")

if __name__ == "__main__":
    main()

# Sample Input / Output

"""
Input:

Enter the Size of the Array:
n = 11

Enter the elements of the array: 
arr = [45 77 18 96 1 33 8 23 11 93 73]

Output:

The sorted array is:
[1, 8, 11, 18, 23, 33, 45, 73, 77, 93, 96]
"""

# Links

"""
Access the Problem:-
    Take U Forward (TUF): https://takeuforward.org/plus/dsa/problems/bubble-sort
    Geeks For Geeks (GFG): https://www.geeksforgeeks.org/problems/bubble-sort/1
    Naukri Code 360 (Coding Ninjas): https://www.naukri.com/code360/problems/bubble-sort_980524

Article: https://takeuforward.org/data-structure/bubble-sort-algorithm/
"""