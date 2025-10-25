# Rotate Image
# Rotate Matrix

"""
Problem Statement:-

    Rotate matrix by 90 degrees
    
    Given an N * N 2D integer matrix, rotate the matrix by 90 degrees clockwise.
    The rotation must be done in place, meaning the input 2D matrix must be modified directly.

Examples:-

    Example 1:
    
        Input:
            mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        Output:
            mat =  [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
    
    Example 2:
    
        Input:
            mat = [[0, 1, 1, 2], [2, 0, 3, 1], [4, 5, 0, 5], [5, 6, 7, 0]]
        Output:
            mat = [[5, 4, 2, 0], [6, 5, 0, 1], [7, 0, 3, 1], [0, 5, 1, 2]]
"""

# Function to rotate an image or the given matrix by 90 degrees
def rotate (mat, n):
    
    # Step 1: Traverse through the matrix and make a transpose of the same
    for i in range(n):
        for j in range(i):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
    
    # Step 2: Reverse each row of the matrix, after transposing
    for i in range(n):
        
        left_pointer = 0
        right_pointer = n - 1
        
        while left_pointer < right_pointer:
            
            mat[i][left_pointer], mat[i][right_pointer] = mat[i][right_pointer], mat[i][left_pointer]
            
            left_pointer += 1
            right_pointer -= 1
            
    # Return the resultant matrix or image
    return mat

# Main Function
def main():
    
    # Take User Input for Matrix Size
    n = int (input ("Enter the Number of Dimensions of the Matrix:\n"))
        
    # Take User Input for Elements of the Matrix
    elements = list(map(int, input("Enter the Elements of the Matrix:\n").split()))

    # Convert 1D list into a 2D matrix
    mat = [elements[i*n:(i+1)*n] for i in range(n)]
        
    # Process the Matrix
    ans = rotate (mat, n)
        
    # Output the modified matrix
    print("Updated Matrix:")
    
    for row in ans:
        print(" ".join(map(str, row)))

if __name__ == "__main__":
    main()

# Sample Input / Output

"""
Input:

Enter the Number of Dimensions of the Matrix:
n = 3

Enter the Elements of the Matrix:
elements = 1 2 3 4 5 6 7 8 9

So,
    The Matrix becomes --
        mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    In 2D Form --
    mat = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]

Output:

Updated Matrix:
7 4 1
8 5 2
9 6 3

"""

# Link

"""
Access the Problem:-
    Take U Forward (TUF): https://takeuforward.org/plus/dsa/problems/rotate-matrix-by-90-degrees
    Leetcode (Question No. 48): https://leetcode.com/problems/rotate-image/description/
    Geeks For Geeks (GFG): https://www.geeksforgeeks.org/problems/rotate-by-90-degree0356/1
    Naukri Code 360 (Coding Ninjas): https://www.naukri.com/code360/problems/rotate-clockwise_4607762

Article: https://takeuforward.org/data-structure/rotate-image-by-90-degree/
"""