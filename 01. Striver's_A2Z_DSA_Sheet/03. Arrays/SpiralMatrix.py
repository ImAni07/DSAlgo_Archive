# Spiral Matrix
# Traverse the given Matrix in a Spiral Manner
# Spiral Traversal of Matrix
# Print the matrix in spiral manner

"""
Problem Statement:-

    Spiral Traversal of Matrix
    Print the matrix in spiral manner
    
    Given an M * N matrix, print the elements in a clockwise spiral manner.
    Return an array with the elements in the order of their appearance when printed in a spiral manner.

Examples:-

    Example 1:
    
        Input: 
            matrix = [[1, 2, 3], [4 ,5 ,6], [7, 8, 9]]
        Output: 
            [1, 2, 3, 6, 9, 8, 7, 4, 5]
        Explanation:
            The elements in the spiral order are 
                1, 2, 3 -> 6, 9 -> 8, 7 -> 4, 5
    
    Example 2:
    
        Input: 
            matrix = [[1, 2, 3, 4], [5, 6, 7, 8]]
        Output: 
            [1, 2, 3, 4, 8, 7, 6, 5]
        Explanation:
            The elements in the spiral order are 
                1, 2, 3, 4 -> 8, 7, 6, 5
"""

# Function to find a new 2D Array by spiral traversal of the given matrix (given 2D Array)
def spiralOrder (matrix):
    
    # Initialize 4 pointers
    top = 0
    bottom = len(matrix) - 1
    left = 0
    right = len(matrix[0]) - 1
    
    # Declare an empty list to store the spiral matrix
    spiral_matrix = []
    
    # Traverse the given matrix in a spiral order
    while top <= bottom and left <= right:
        
        # For going from Left to Right
        for j in range (left, right + 1):
            spiral_matrix.append(matrix[top][j])
        
        # Increase the value of top by 1
        top += 1
        
        # Check Point
        if top > bottom or left > right:
            break
        
        # For going from Up to Down
        for i in range (top, bottom + 1):
            spiral_matrix.append(matrix[i][right])
        
        # Decrease the value of right by 1
        right -= 1
        
        # Check Point
        if top > bottom or left > right:
            break
        
        # For going from Right to Left
        for j in range (right, left - 1, -1):
            spiral_matrix.append(matrix[bottom][j])
        
        # Decrease the value of bottom by 1
        bottom -= 1
        
        # Check Point
        if top > bottom or left > right:
            break
        
        # For going from Down to Up
        for i in range (bottom, top - 1, -1):
            spiral_matrix.append(matrix[i][left])
        
        # Increase the value of left by 1
        left += 1
        
        # Check Point
        if top > bottom or left > right:
            break
    
    # Return the resultant
    return spiral_matrix

# Main Function
def main():
    
    # Take User Input for the Number of Rows
    n = int (input ("Enter the Number of Rows of the Matrix:\n"))
    
    # Take User Input for the Number of Columns
    m = int (input ("Enter the Number of Columns of the Matrix:\n"))
    
    # Take User Input for the Elements
    elements = list(map(int, input("Enter the Elements of the Matrix:\n").split()))

    # Convert 1D list into a 2D matrix
    matrix = [elements[i*m:(i+1)*m] for i in range(n)]
        
    # Process the Matrix
    resultant = spiralOrder (matrix)
    
    # Print the Output
    print("The given Matrix in Spiral Order is:")
    print(" ".join(map(str, resultant)))

if __name__ == "__main__":
    main()

# Sample Input / Output

"""
Input:

Enter the Number of Rows of the Matrix:
n = 4

Enter the Number of Columns of the Matrix:
m = 4

Enter the Elements of the Matrix:
elements = 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16

So,
    The Matrix becomes:
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8,], [9, 10, 11, 12], [13, 14, 15, 16]]
    
    In 2D Form --
    
    matrix = [[1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]]

Output:

The given Matrix in Spiral Order is:
1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10

In 2D Form --

[[1 2 3 4]
[8 12 16 15]
[14 13 9 5]
[6 7 11 10]
"""

# Link

"""
Access the Problem:-
    Take U Forward (TUF): https://takeuforward.org/plus/dsa/problems/print-the-matrix-in-spiral-manner
    Leetcode (Question No. 54): https://leetcode.com/problems/spiral-matrix/description/
    Geeks For Geeks (GFG): https://www.geeksforgeeks.org/problems/spirally-traversing-a-matrix-1587115621/1
    Naukri Code 360 (Coding Ninjas): https://www.naukri.com/code360/problems/spiral-matrix_840698

Article: https://takeuforward.org/data-structure/spiral-traversal-of-matrix/
"""