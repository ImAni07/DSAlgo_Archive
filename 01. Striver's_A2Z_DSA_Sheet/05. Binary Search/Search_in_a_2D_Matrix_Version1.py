# Search in a 2D Matrix

"""
Problem Statement:-

    Given a 2-D array mat where the elements of each row are sorted in non-decreasing order, and 
        the first element of a row is greater than the last element of the previous row (if it exists), and an integer target, 
        determine if the target exists in the given mat or not.

Examples:-

    Example 1:
    
        Input: 
            mat = [ [1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12] ], 
            target = 8
        Output: 
            True
        Explanation: 
            The target = 8 exists in the 'mat' at index (1, 3).
    
    Example 2:
    
        Input: 
            mat = [ [1, 2, 4], [6, 7, 8], [9, 10, 34] ], 
            target = 78
        Output: 
            False
        Explanation: 
            The target = 78 does not exist in the 'mat'. 
            Therefore in the output, we see 'false'.
"""

# Function to search for the target in the 2D matrix
def searchMatrix (matrix, target):
    
    # Length of the matrix
    n = len (matrix)
    m = len (matrix[0])
    
    # Initialize the low and high pointers
    lo = 0
    hi = n * m - 1
    
    # Perform Binary Search
    while lo <= hi:
        
        # Calculate the mid index
        mid = (lo + hi) // 2
        
        # Calculate the row and column index of the mid element
        row = mid // m
        col = mid % m
        
        # If the mid element is equal to the target, 
        # return True
        if matrix[row][col] == target:
            return True
        
        # If the mid element is less than the target
        elif matrix[row][col] < target:
            
            # Eliminate the left half
            lo = mid + 1
        
        # If the mid element is greater than the target
        else:
            
            # Eliminate the right half
            hi = mid - 1
        
    # If the target is not found, return False
    return False

# Main Function
def main ():
    
    # Take User Input for the Size of the Matrix
    n, m = map (int, input ("Enter the number of rows and columns: ").split ())
    
    # Take User Input for the Elements of the Matrix
    print("Enter the elements of the matrix:\n")
    matrix = []
    for i in range (n):
        row = list (map (int, input (f"Row {i+1}: ").split ()))
        matrix.append(row)
    
    # Take User Input for the Target
    target = int (input ("Enter the Target Element:\n"))
    
    # Print whether the target is found in the matrix or not
    if searchMatrix (matrix, target):
        print (f"The Target Element {target} is present.")
    else:
        print (f"The Target Element {target} is not present.")

if __name__ == "__main__":
    main ()

# Sample Input / Output:

"""
Input:

Enter the number of rows and columns:
n, m = 4 4

Enter the elements of the matrix:

Row 1: 1 2 3 4
Row 2: 5 6 7 8
Row 3: 9 10 11 12
Row 4: 13 14 15 16

Enter the Target Element:
target = 7

Output:

The Target Element 7 is present.
"""

# Link

"""
Access the Problem:-
    Take U Forward (TUF): https://takeuforward.org/plus/dsa/problems/search-in-a-2d-matrix
    Leetcode (Question No. 74): https://leetcode.com/problems/search-a-2d-matrix/description/
    Naukri Code 360 (Coding Ninjas): https://www.naukri.com/code360/problems/search-in-a-sorted-2d-matrix_6917532

Article: https://takeuforward.org/data-structure/search-in-a-sorted-2d-matrix/
"""