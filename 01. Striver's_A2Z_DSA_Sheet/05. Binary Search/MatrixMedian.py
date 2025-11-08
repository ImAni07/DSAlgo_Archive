# Median of a Row-Wise Sorted Matrix
# Matrix Median

"""
Problem Statement:-

    Matrix Median
    
    Given a 2D array matrix that is row-wise sorted. 
    The task is to find the median of the given matrix.

Examples:-

    Example 1:
    
        Input: 
            mat = [ [1, 4, 9], [2, 5, 6], [3, 7, 8] ] 
        Output: 
            5
        Explanation: 
            If we find the linear sorted array, the array becomes 1 2 3 4 5 6 7 8 9. 
            So, median = 5
    
    Example 2:
    
        Input: 
            mat = [ [1, 3, 8], [2, 3, 4], [1, 2, 5] ] 
        Output: 
            3
        Explanation: 
            If we find the linear sorted array, the array becomes 1 1 2 2 3 3 4 5 8. 
            So, median = 3
"""

# Helper function to find the upper bound of x in a row
def upperBound (mat, x):
    
    # Initialize the low and the high pointers
    lo = 0
    hi = len (mat) - 1
    
    # Initialize an answer
    ans = len (mat)
    
    # Apply Binary Search
    while lo <= hi:
        
        # Calculate the mid value
        mid = (lo + hi) // 2
        
        # If the mid element is greater than x
        if mat[mid] > x:
            ans = mid
            
            # Eliminate the right half
            hi = mid - 1
        
        # If the mid element is less than or equal to x
        else:
            
            # Eliminate the left half
            lo = mid + 1
    
    # Return the answer
    return ans

# Function to count the number of elements less than or equal to mid in the matrix
def countSmallEqual (mat, x):
    
    # Initialize the count variable
    count = 0
    
    # Traverse through the matrix
    for i in range (len (mat)):
        
        # Update the count variable
        count += upperBound (mat[i], x)
    
    # Return the count variable
    return count

# Function to find the median of a row-wise sorted matrix
def median (mat):
    
    # Declare the low and high pointers
    lo = float ('inf')
    hi = float ('-inf')
    
    # Traverse through the matrix
    for i in range (len (mat)):
        
        # Find the low and high elements
        lo = min (lo, mat[i][0])
        hi = max (hi, mat[i][len(mat[0])-1])
    
    # Calculate the required position of the median
    required = (len(mat) * len(mat[0])) // 2
    
    # Perform Binary Search
    while lo <= hi:
        
        # Calculate the mid element
        mid = (lo + hi) // 2
        
        # Check the number of elements less than or equal to mid
        if countSmallEqual (mat, mid) <= required:
            lo = mid + 1
        else:
            hi = mid - 1
    
    # Return the median
    return lo

# Main Function
def main ():
    
    # Take User Input for the Size of the Matrix
    m, n = map (int, input ("Enter the number of rows and columns: ").split ())
    
    # Take User Input for the Elements of the Matrix
    print("Enter the elements of the matrix:\n")
    mat = []
    for i in range (m):
        row = list (map (int, input (f"Row {i+1}: ").split ()))
        mat.append(row)
    
    # Print the median of the matrix
    print (f"The Median of the Matrix is: {median (mat)}")

if __name__ == "__main__":
    main ()

# Sample Input / Output:

"""
Input:

Enter the number od rows and columns:
n, m = 3 3 

Enter the elements of the matrix:

Row 1: 2 4 9
Row 2: 3 6 7
Row 3: 4 7 10

Output:
The Median of the Matrix is: 6
"""

# Link

"""
Access the Problem:-
    Take U Forward (TUF): https://takeuforward.org/plus/dsa/problems/matrix-median
    Geeks For Geeks (GFG): https://www.geeksforgeeks.org/problems/median-in-a-row-wise-sorted-matrix1527/1
    Naukri Code 360 (Coding Ninjas): https://www.naukri.com/code360/problems/median-in-matrix_981178

Article: https://takeuforward.org/data-structure/median-of-row-wise-sorted-matrix/
"""