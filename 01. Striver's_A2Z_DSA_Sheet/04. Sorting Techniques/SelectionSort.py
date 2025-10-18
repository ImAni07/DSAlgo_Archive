# Selection Sort

"""
Problem Statement:-

    Selection Sort Algorithm
    
    Given an array of integers, 
    sort the array in non-decreasing order using the selection sort algorithm and 
    return the sorted array.
    
    A sorted array in non-decreasing order is an array 
    where each element is greater than or equal to all previous elements in the array.

Examples:-

    Example 1:
    
        Input:
            N = 5, 
            array[] = [7, 4, 1, 5, 3]
        Output:
            [1, 3, 4, 5, 7]
        Explanation: 
            1 <= 3 <= 4 <= 5 <= 7.
            Thus the array is sorted in non-decreasing order.

    Example 2:
    
        Input:
            N = 5, 
            array[] = [5, 4, 4, 1, 1]
        Output:
            [1, 1, 4, 4, 5]
        Explanation:
            1 <= 1 <= 4 <= 4 <= 5.
            Thus the array is sorted in non-decreasing order.
"""

# Function to apply Selection Sort
def selectionSort (arr):
    
    # Outer Loop --> Select the Range
    for i in range ((len (arr) - 1)):
        
        # Starting point of the iteration
        min_index = i
        
        # Inner Loop --> Select the minimum element from the range of the unsorted array
        for j in range (i, (len (arr))):
            
            # Check for minimum
            if arr[j] < arr[min_index]:
                
                # Swap
                arr[j], arr[min_index] = arr[min_index], arr[j]
    
    # Return the sorted array
    return arr

# Main Function
def main():
    
    # Take User Input for the Size of the Array
    n = int (input ("Enter the Size of the Array:\n"))
    
    # Take User Input for the Elements of the Array
    arr = list(map(int, input("Enter the elements of the array: ").split()))
    
    # Print
    print (f"\nThe sorted array is:\n{selectionSort(arr)}")

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
    Take U Forward (TUF): https://takeuforward.org/plus/dsa/problems/selection-sort
    Geeks For Geeks (GFG): https://www.geeksforgeeks.org/problems/selection-sort/1
    Naukri Code 360 (Coding Ninjas): https://www.naukri.com/code360/problems/selection-sort_981162

Article: https://takeuforward.org/sorting/selection-sort-algorithm/
"""