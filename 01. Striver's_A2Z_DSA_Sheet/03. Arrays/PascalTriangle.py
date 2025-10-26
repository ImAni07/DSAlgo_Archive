# Pascal's Triangle

# Variant 1 --> Print only the nth row
# Variant 2 --> Print upto nth row

"""
Problem Statement:-

    Write a program to generate Pascal's triangle. 
    In Pascal's triangle, each number is the sum of the two numbers directly above it.

Examples:-

    Example 1:
    
        Input: 
            N = 5, 
            r = 5, 
            c = 3 
        Output: 
            Element at position (r, c): 
                6
            N-th row of Pascal’s triangle: 
                1 4 6 4 1
            First n rows of Pascal’s triangle:
                1 
                1 1 
                1 2 1 
                1 3 3 1 
                1 4 6 4 1  
        Explanation: 
            Pascal triangle for first 5 rows is shown above.

    Example 2:
    
        Input: 
            N = 1, 
            r = 1, 
            c = 1
        Output: 
            Element at position (r, c): 
                1
            N-th row of Pascal’s triangle: 
                1
            First n rows of Pascal’s triangle:
                1  
        Explanation: 
            N = 1 is the base case fof a pascal's triangle.
"""

# Variant 1
# Print the nth row of the Pascal's Triangle

# Function to compute the binomial coefficient
def pascalElement (r, c):
    
    # Initialize variable to hold the computed binomial coefficient
    result = 1
    
    # Convert the row and column to 0-based index
    n = r - 1
    k = c - 1
    
    # Compute C(n, k) using iterative formula
    for i in range(k):
        
        result *= (n - i)
        result //= (i + 1)

    # Return the obtained result
    return result

# Function to print the nth row
def nthRowPascalTriangle (n):
    
    row = [pascalElement(n, c) for c in range(1, n + 1)]
    return row

# Variant 2
# Print the Pascal's Triangle up to the nth row

# Function to generate Pascal's Triangle
def pascalTriangle (n):
    
    # Creating a 2D List
    triangle = []
    
    # Iterate
    for i in range(n):
        
        rows =  []
        triangle.append(rows)
        
        # Generate the elements
        for j in range(i+1):
            
            if j == 0 or j == i:
                triangle[i].append(1)
            
            else:
                triangle[i].append(triangle[i-1][j] + triangle[i-1][j-1])
    
    # Return
    return triangle

# Function to print the Pascal Triangle upto nth row
def print_PascalTriangle (n):
    
    # Store the result
    triangle = pascalTriangle(n)
    
    # Print the triangle
    print(f"\nPascal's Triangle up to {n} Rows:")
    
    for row in triangle:
        print(row, end=" ")
    print()

# Main Function
def main():
    
    # Options
    print ("1. Print the Pascal's Triangle only for the nth row")
    print ("2. Print the Pascal's Triangle up to the nth row")
    
    # Take User Input
    
    # Choice
    choice = int (input ("\nEnter your choice:\n"))
    
    # Range
    n = int (input ("Enter the Range:\n"))
    
    # Print the Result wrt choices
    if choice == 1:
        print (f"\nThe {n}th Row of the Pascal's Triangle is:")
        print (nthRowPascalTriangle (n))
    
    elif choice == 2:
        print (print_PascalTriangle (n))
    
    else:
        print ("INVALID CHOICE!")

if __name__ == "__main__":
    main()

# Sample Input / Output:

"""
Test Case 1:
    Variant 1 --> Print only the nth row

Message:

1. Print the Pascal's Triangle only for the nth row
2. Print the Pascal's Triangle up to the nth ro

Input:

Enter your choice:
choice = 1

Enter the Range:
n = 4

Output:

The 4th Row of the Pascal's Triangle is:
[1, 3, 3, 1]

Test Case 2:
    Variant 2 --> Print upto nth row

Message:

1. Print the Pascal's Triangle only for the nth row
2. Print the Pascal's Triangle up to the nth ro

Input:

Enter your choice:
choice = 2

Enter the Range:
n = 5

Output:

Pascal's Triangle up to 5 Rows:
[[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Output in Triangular form --

    1
    1 1
    1 2 1
    1 3 3 1
    1 4 6 4 1
"""

# Link

"""
Access the Problem:-
    Take U Forward (TUF): https://takeuforward.org/plus/dsa/problems/pascal's-triangle
    Leetcode (Question No. 118): https://leetcode.com/problems/pascals-triangle/description/
    Geeks For Geeks (GFG): https://www.geeksforgeeks.org/problems/pascal-triangle0652/1
    Naukri Code 360 (Coding Ninjas): https://www.naukri.com/code360/problems/pascal-s-triangle_1089580

Article: https://takeuforward.org/data-structure/program-to-generate-pascals-triangle/
"""