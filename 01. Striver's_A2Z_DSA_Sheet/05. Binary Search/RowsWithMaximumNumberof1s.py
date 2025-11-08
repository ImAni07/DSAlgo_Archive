# Rows with Maximum Number of 1s

"""
Problem Statement:-

    Find row with maximum 1's
    
    Given a non-empty grid mat consisting of only 0s and 1s,
        where all the rows are sorted in ascending order, 
        find the index of the row with the maximum number of ones.
    If two rows have the same number of ones, consider the one with a smaller index. 
    If no 1 exists in the matrix, return -1.

Examples:-

    Example 1:
    
        Input: 
            mat = [ [1, 1, 1], [0, 0, 1], [0, 0, 0] ]
        Output: 
            0
        Explanation: 
            The row with the maximum number of ones is 0 (0 - indexed).
    
    Example 2:
    
        Input: 
            mat = [ [0, 0], [0, 0] ]
        Output: 
            -1
        Explanation: 
            The matrix does not contain any 1. 
            So, -1 is the answer.
"""

# Helper function to find the lower bound of 1
def lowerBound (mat, n, x):
    
    # Initialize the pointers
    lo = 0
    hi = n - 1
    
    # Declare an answer
    ans = n
    
    # Perform Binary Search
    while lo <= hi:
        
        # Calculate the mid index
        mid = (lo + hi) // 2
        
        # If the mid element is greater than or equal to x
        if mat[mid] >= x:
            ans = mid
            
            # Eliminate the right half
            hi = mid - 1
        
        # If the mid element is less than x
        else:
            
            # Eliminate the left half
            lo = mid + 1
    
    # Return the lower bound of 1
    return ans

# Function to find the row with the maximum number of 1s
def rowAndMaximumOnes (mat):
    
    # Length of the matrix
    n = len (mat)
    m = len (mat[0])
    
    # Counter for maximum number of 1s
    max_1s = 0
    
    # Store the required row index
    row_index = -1
    
    # Iterate over each row
    for i in range (n):
        
        # Count the Number of 1s in the current row using lower bound
        count_1s = m - lowerBound (mat[i], m, 1)
        
        # If the current row has more 1s than the maximum found so far, 
        # update the maximum and row index
        if count_1s > max_1s:
            max_1s = count_1s
            row_index = i
    
    # Return the row index and the maximum number of 1s
    return [row_index, max_1s]

# Main Function
def main ():
    
    # Take User Input for the Size of the Matrix
    n, m = map (int, input ("Enter the number of rows and columns: ").split ())
    
    # Take User Input for the Elements of the Matrix
    print("Enter the elements of the matrix:\n")
    mat = []
    for i in range (n):
        row = list (map (int, input (f"Row {i+1}: ").split ()))
        mat.append(row)
    
    # Store the Output
    result = rowAndMaximumOnes(mat)
    
    # Print the result
    print (f"Output: {result}\n")
    print (f"The row with the maximum number of 1s is: Row {result[0]}\n")
    print (f"Maximum number of 1s in that row: {result[1]}\n")

if __name__ == "__main__":
    main ()

# Sample Input / Output

"""
Input:

Enter the number of rows and columns:
n, m = 3 3

Enter the elements of the matrix:

Row 1: 0 0 0
Row 2: 0 1 1
Row 3: 0 1 0

Output:

Output: [1, 2]
The row with maximum number of 1s is: Row 1
Maximum number of 1s in that row: 2
"""

# Link

"""
Access the Problem:-
    Take U Forward (TUF): https://takeuforward.org/plus/dsa/problems/find-row-with-maximum-1's
    Leetcode (Question No. 2643): https://leetcode.com/problems/row-with-maximum-ones/description/
    Geeks For Geeks (GFG): https://www.geeksforgeeks.org/problems/row-with-max-1s0023/1
    Naukri Code 360 (Coding Ninjas): https://www.naukri.com/code360/problems/row-with-maximum-1-s_1112656

Article: https://takeuforward.org/arrays/find-the-row-with-maximum-number-of-1s/
"""