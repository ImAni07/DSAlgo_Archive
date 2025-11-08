# Find Peak Element in a 2D Matrix
# Find Peak Element - Part II

"""
Problem Statement:-

    Find Peak Element - II
    
    Given a 0-indexed n x m matrix mat where no two adjacent cells are equal, 
        find any peak element mat[i][j] and return the array [i, j].
    A peak element in a 2D grid is an element that is strictly greater than all of its adjacent neighbours to the left, right, top, and bottom.
    Assume that the entire matrix is surrounded by an outer perimeter with the value -1 in each cell.

Examples:-

    Example 1:
    
        Input: 
            mat = [[10, 20, 15], [21, 30, 14], [7, 16, 32]]
        Output: 
            [1, 1]
        Explanation: 
            The value at index [1, 1] is 30, which is a peak element because all its neighbours are smaller or equal to it. 
            Similarly, {2, 2} can also be picked as a peak.
    
    Example 2:
    
        Input: 
            mat = [[10, 7], [11, 17]]
        Output: 
            [1, 1]
        Explanation:
            The value at index [1, 1] is 17, which is the only peak element because all its neighbours are smaller or equal to it.
"""

# Function to find a peak element in a 2D matrix
def findPeakGrid (mat):
    
    # Length of the matrix
    n = len (mat)
    m = len (mat[0])
    
    # Initialize the low and high pointers
    lo = 0
    hi = m - 1
    
    # Perform Binary Search on columns
    while lo <= hi:
        
        # Calculate the mid column
        mid = (lo + hi) // 2
        
        # Find the index of the maximum element in the mid column
        max_row_index = 0
        
        # Traverse through the mid column to find the maximum element
        for i in range (n):
            if mat[i][mid] > mat[max_row_index][mid]:
                max_row_index = i
        
        # Find the left counterpart of the maximum element
        if mid - 1 >= 0:
            left = mat[max_row_index][mid - 1]
        else:
            left = float ('-inf')
        
        # Find the right counterpart of the maximum element
        if mid + 1 < m:
            right = mat[max_row_index][mid + 1]
        else:
            right = float ('-inf')
        
        # If the maximum element is greater than or equal to its left and right counterparts, 
        # return its position
        if mat[max_row_index][mid] > left and mat[max_row_index][mid] > right:
            return [max_row_index, mid]
        
        # If the maximum element is less than its left counterpart, 
        # search in the left half of the mid column
        elif mat[max_row_index][mid] < left:
            hi = mid - 1
        
        # If the maximum element is less than its right counterpart, 
        # search in the right half of the mid column
        else:
            lo = mid + 1
    
    # Dummy return statement, if no peak element is found
    return [-1, -1]

# Main Function
def main ():
    
    # Take User Input for the Number of Rows of the Matrix
    n = int (input ("Number of Rows:\n"))
    
    # Take User Input for the Number of Columns of the Matrix
    m = int (input ("Number of Columns:\n"))
    
    # Take User Input for the Elements of the Matrix
    print("Enter the elements of the matrix:\n")
    mat = []
    for i in range (n):
        row = list (map (int, input (f"Row {i+1}: ").split ()))
        mat.append(row)
    
    # Find the peak element in the matrix
    result = findPeakGrid (mat)
    
    # Print the position of the peak element
    print (f"The Position of the Peak Element in the Matrix: {result[0], result[1]}")

if __name__ == "__main__":
    main ()

# Sample Input / Output

"""
Input:

Number of Rows:
n = 2

Number of Columns:
m = 2

Enter the elements of the matrix:

Row 1: 1 4
Row 2: 2 3

Output:
The Position of the Peak Element in the Matrix: [0, 1]
"""

# Link

"""
Access the Problem:-
    Take U Forward (TUF): https://takeuforward.org/plus/dsa/problems/find-peak-element-ii
    Leetcode (Question No. 1901): https://leetcode.com/problems/find-a-peak-element-ii/description/
    Geeks For Geeks (GFG): https://www.geeksforgeeks.org/problems/find-the-peak-element-in-a-2d-matrix/1
    Naukri Code 360 (Coding Ninjas): https://www.naukri.com/code360/problems/find-peak-element_7449073

Article: https://takeuforward.org/data-structure/find-peak-element-2d-matrix
"""