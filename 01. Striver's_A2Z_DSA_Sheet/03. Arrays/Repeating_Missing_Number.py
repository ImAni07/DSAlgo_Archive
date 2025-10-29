# Repating and Missing Number
# Repeating and Missing Value

# Version 1 --> 1D Array
# Version 2 --> 2D Grid

"""
Version 1

Problem Statement:-

    Given an integer array a of size n containing values from [1, n] and 
        each value appears exactly once in the array, except for A, which appears twice and B which is missing.
    Return the values A and B, as an array of size 2, 
        where A appears in the 0-th index and B in the 1st index.
    Note: You are not allowed to modify the original array.

Examples:-

    Example 1:
    
        Input: 
            a = [3, 5, 4, 1, 1]
        Output: 
            [1, 2]
        Explanation:
            1 appears two times in the array and 2 is missing from array
    
    Example 2:
    
        Input: 
            a = [1, 2, 3, 6, 7, 5, 7]
        Output: 
            [7, 4]
        Explanation:
            7 appears two times in the array and 4 is missing from nums.

Version 2

Problem Statement:-

    You are given a 0-indexed 2D integer matrix grid of size n * n with values in the range [1, n2]. 
    Each integer appears exactly once except a which appears twice and b which is missing. 
    The task is to find the repeating and missing numbers a and b.
    Return a 0-indexed integer array ans of size 2 where ans[0] equals to a and ans[1] equals to b.

Examples:-

    Example 1:
    
        Input: 
            grid = [[9,1,7],[8,9,2],[3,4,6]]
        Output: 
            [9,5]
        Explanation: 
            Number 9 is repeated and number
"""

# Version 1

# Function to find the repeating as well as the missing number from a given array
def findMissingRepeatingNumbers (a):
    
    # Determine the size of the given array
    n = len(a)
    
    # Declare the required variables
    sum_array = 0
    sum_array_squared = 0
    
    # Find the sum of n natural numbers
    sum = int ((n * (n + 1)) / 2)
    
    # Find the squared sum of n natural numbers
    sum_squared = int ((n * (n + 1) * (2 * n + 1)) / 6)
    
    # Iterate through the array
    for i in range (n):
        
        # Add the current element to the sum of the array
        sum_array += a[i]
        
        # Add the square of the current element to the squared sum of the array
        sum_array_squared += a[i] * a[i]
        
    # Find two equations
    
    # Equation 1 --> x - y
    eq1 = sum_array - sum
    
    # Equation 2 --> x^2 - y^2
    eq2 = sum_array_squared - sum_squared
    
    # Modify equation 2 into x + y
    eq2 = int (eq2 / eq1)
    
    # Find the repeating value
    repeating_number = int ((eq1 + eq2) / 2)
    
    # Find the missing value
    missing_number = repeating_number - eq1
    
    # Return the result
    return [repeating_number, missing_number]

# Version 2

# Function to find the missing as well as the repeated values
def findMissingAndRepeatedValues (grid):
    
    # Determine the size of the given array
    n = len (grid)
    size = n * n
    
    # Declare the required variables
    actual_sum = 0
    actual_squared_sum = 0
    
    # Find the sum of n natural numbers
    expected_sum = int ((size * (size + 1)) / 2)
    
    # Find the squared sum of n natural numbers
    expected_squared_sum = int ((size * (size + 1) * (2 * size + 1)) / 6)
    
    # Traverse through the given 2D Array
    for i in range (n):
        for j in range (n):
            
            # Add the current element to the sum of the array
            actual_sum += grid[i][j]
        
            # Add the square of the current element to the squared sum of the array
            actual_squared_sum += grid[i][j] * grid[i][j]
    
    # Find two equations
    
    # Equation 1 --> x - y
    equation1 = actual_sum - expected_sum
    
    # Equation 2 --> x^2 - y^2
    equation2 = actual_squared_sum - expected_squared_sum
    
    # Modify equation 2 into x + y
    equation2 = int (equation2 / equation1)
    
    # Find the repeating value
    repeating_value = int ((equation1 + equation2) / 2)
    
    # Find the missing value
    missing_value = repeating_value - equation1
    
    # Return the result
    return [repeating_value, missing_value]

# Main Function
def main ():
    
    # Choice
    print("Choose the version:")
    print("1. For 1D Array")
    print("2. For 2D Grid\n")
    
    # Enter choice
    choice = int (input ("Enter the Choice:\n"))
    
    # Version 1 → 1D Array
    if choice == 1:
        
        # Take User for the Size of the Array
        n = int(input("\nEnter the size of the array:\n"))
        
        # Take User Input for the Elements of the Array
        a = list(map(int, input("Enter the Elements of the Array:\n").split()))
        
        # Store the Result
        result = findMissingRepeatingNumbers(a)

        # Output
        print(f"Repeating Number:\n{result[0]}")
        print(f"Missing Number:\n{result[1]}")

    # Version 2 → 2D Grid
    elif choice == 2:
        
        # Take Input for the Size of the Array
        n = int(input("\nEnter the size of the 2D grid (n x n):\n"))

        print(f"Enter the {n*n} elements row-wise:")
        grid = []
        for i in range(n):
            row = list(map(int, input(f"Row {i+1}: ").split()))
            grid.append(row)

        # Store the Result
        result = findMissingAndRepeatedValues(grid)

        # Output
        print(f"Repeating Number:\n{result[0]}")
        print(f"Missing Number:\n{result[1]}")

    else:
        print("\nInvalid choice!")

if __name__ == "__main__":
    main()

# Sample Input / Output

"""
Test Case 1:

Choose the version:
1. For 1D Array
2. For 2D Grid

Choice:

Enter the Choice:
choice = 1

Input:

Enter the Size of the Array:
n = 3

Enter the Elements of the Array:
a = 1 3 3

Output:

Repeating Number:
3

Missing Number:
2

Test Case 2:

Choose the version:
1. For 1D Array
2. For 2D Grid

Choice:

Enter the Choice:
choice = 2

Input:

Enter the Size of the Array:
n = 2

grid = [[1,3], [2,2]]

Output:

Repeating Number:
2

Missing Number:
4
"""

# Link

"""
Access the Problem:-

    Version 1 --
        Take U Forward (TUF): https://takeuforward.org/plus/dsa/problems/find-the-repeating-and-missing-number
        Geeks For Geeks (GFG): https://www.geeksforgeeks.org/problems/find-missing-and-repeating2512/1
        Naukri Code 360 (Coding Ninjas): https://www.naukri.com/code360/problems/missing-and-repeating-numbers_873366
    
    Version 2 --
        Leetcode (Question No. 2965): https://leetcode.com/problems/find-missing-and-repeated-values/description/

Article: https://takeuforward.org/data-structure/find-the-repeating-and-missing-numbers/
"""