# Set Matrix Zeroes

"""
Problem Statement:-

    Given an m x n integer matrix matrix, 
        if an element is 0, 
        set its entire row and column to 0. 
    You must do it in place.

Examples:-

    Example 1:
    
        Input: 
            matrix = [[1,1,1],[1,0,1],[1,1,1]]
        Output: 
            [[1,0,1],[0,0,0],[1,0,1]]
        Explanation:
            Element at position (1,1) is 0, 
            so set entire row 1 and column 1 to 0.
    
    Example 2:
    
        Input: 
            matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
        Output: 
            [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
        Explanation:
            There are two zeroes: 
                (0,0) and 
                (0,3).
            Row 0 → all elements become 0
            Column 0 and column 3 → all elements become 0
"""

# Function to set the zeroes of the matrix
def zeroMatrix (matrix, n, m):
    
    # Tracker for the 1st column
    col1_tracker = False
    
    # Step 1 --> Mark the 1st row and the 1st column
    for i in range (n):
        for j in range (m):
            if (matrix[i][j] == 0):
                
                # Mark the 1st column
                matrix[i][0] = 0
            
            if j == 0:
                col1_tracker = True
            else:
                
                # Mark the 1st row
                matrix[0][j] = 0
    
    # Step 2 --> Mark with 0 from (n - 1) to (m - 1)
    for i in range (1, n):
        for j in range (1, m):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0
    
    # Step 3 --> Mark the 1st row
    if matrix[0][0] == 0:
        for j in range (m):
            matrix[0][j] = 0
    
    # Step 4 --> Mark the 1st column
    if col1_tracker:
            for i in range (n):
                matrix[i][0] = 0
    
    # Return the matrix with all the zeroes set
    return matrix

# Main Function
def main():
    
    # Take User Input for the Lengths of the Matrix
    n = int(input("Enter number of rows:\n"))
    m = int(input("Enter number of columns:\n"))

    # Take User Input for the Elements of the Matrix
    print(f"Enter {n*m} elements separated by space:")
    elements = list(map(int, input().split()))

    # Convert 1D list into a 2D matrix
    matrix = [elements[i*m:(i+1)*m] for i in range(n)]

    # Process the matrix
    result = zeroMatrix(matrix, n, m)

    # Output the modified matrix
    print("Updated Matrix:")
    
    for row in result:
        print(" ".join(map(str, row)))

if __name__ == "__main__":
    main()

# Sample Input / Output

"""
Input:

Enter the number of rows:
n = 3

Enter the number of columns:
m = 3

Enter 9 elements separated by space:
elements = 0 1 1 1 0 1 1 1 0

Output:

Updated Matrix:
0 0 0
0 0 0
0 0 0
"""

# Link

"""
Access the Problem:-
    Take U Forward (TUF): https://takeuforward.org/plus/dsa/problems/set-matrix-zeroes
    Leetcode (Question No. 73): https://leetcode.com/problems/set-matrix-zeroes/description/
    Geeks For Geeks (GFG): https://www.geeksforgeeks.org/problems/set-matrix-zeroes/1
    Naukri Code 360 (Coding Ninjas): https://www.naukri.com/code360/problems/set-matrix-zeros_3846774

Article: https://takeuforward.org/data-structure/set-matrix-zero/
"""