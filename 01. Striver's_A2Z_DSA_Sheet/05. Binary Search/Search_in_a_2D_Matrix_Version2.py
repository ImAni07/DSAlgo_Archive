# Search in a Row and Column Wise Sorted Matrix

"""
Problem Statement:-

    Search in 2D matrix - II
    
    Given a 2D array matrix where 
        each row is sorted in ascending order from left to right and 
        each column is sorted in ascending order from top to bottom. 
    Write an efficient algorithm to search for a specific integer target in the matrix.

Examples:-

    Example 1:
    
        Input: 
            matrix = [ [1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30] ], 
            target = 5
        Output: 
            True
        Explanation: 
            The target 5 exists in the matrix in the index (1,1)
    
    Example 2:
    
        Input: 
            matrix = [ [1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30] ], 
            target = 20
        Output: 
            False
        Explanation: 
            The target 20 does not exist in the matrix.
"""

# Function to search for the target in the 2D matrix
def searchMatrix(matrix, target):
    
    # Initialize the row and column pointers
    row = 0
    col = len(matrix[0]) - 1
    
    # Traverse the matrix
    while row < len(matrix) and col >= 0:
        
        # If the current element is equal to the target, 
        # return True
        if matrix[row][col] == target:
            return True
        
        # If the current element is greater than the target, 
        # move left
        elif matrix[row][col] > target:
            col -= 1
        
        # If the current element is less than the target, 
        # move down
        else:
            row += 1
    
    # If the target is not found, 
    # return False
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
    target = int (input ("Enter the Target element:\n"))
    
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
n, m = 5 5

Enter the elements of the matrix:

Row 1: 1 4 7 11 15
Row 2: 2 5 8 12 19
Row 3: 3 6 9 16 22
Row 4: 10 13 14 17 24
Row 5: 18 21 23 26 30

Enter the Target element:
target = 5

Output:

The Target Element 5 is present.
"""

# Link

"""
Access the Problem:-
    Take U Forward (TUF): https://takeuforward.org/plus/dsa/problems/search-in-2d-matrix-ii
    Leetcode (Question No. 240): https://leetcode.com/problems/search-a-2d-matrix-ii/description/
    Geeks For Geeks (GFG): https://www.geeksforgeeks.org/problems/search-in-a-matrix17201720/1
    Naukri Code 360 (Coding Ninjas): https://www.naukri.com/code360/problems/search-in-a-row-wise-and-column-wise-sorted-matrix_839811

Article: https://takeuforward.org/arrays/search-in-a-row-and-column-wise-sorted-matrix/
"""