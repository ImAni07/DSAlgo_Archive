# Left Rotate Array by one place

"""
Problem Statement:-

    Left Rotate the Array by One
    
    Given an integer array, rotate the array to the left by one.

Examples:-

    Example 1:
        Input: 
            arr = [1, 2, 3, 4, 5]
        Output: 
            [2, 3, 4, 5, 1]
        Explanation:
            Initially, 
                arr = [1, 2, 3, 4, 5]
            Rotating once to left -> arr = [2, 3, 4, 5, 1]
    
    Example 2:
        Input: 
            arr = [-1, 0, 3, 6]
        Output: 
            [0, 3, 6, -1]
        Explanation:
            Initially, 
                arr = [-1, 0, 3, 6]
            Rotating once to left -> nums = [0, 3, 6, -1]
"""

# Function to rotate array by one place
def rotateArray (arr):
    
    # Size of the array
    n = len (arr)
    
    # Declare a temporary variable and initialize it by storing the first value of the array
    temp = arr[0]
    
    # Traverse through the array
    for i in range (1, n):
        
        # Store the value of the current index of the array in the previous index of the array
        arr[i - 1] = arr[i]
    
    # Store the value of the 1st index of the array in the last index of the array
    arr[n - 1] = temp
    
    return arr

# Main Function
def main():
    
    # Take User Input for the Elements of the Array
    arr = list (map (int, input ("Enter the Elements of the Array:\n").split ()))
    
    # Output
    print (f"The new Array:\n{rotateArray (arr)}")

if __name__ == "__main__":
    main()

# Sample Input / Output

"""
Input:

Enter the Elements of the Array:
arr = 1 2 3 4 5

Output:

The new Array:
[2, 3, 4, 5, 1]
"""

# Links

"""
Access the Problem:-
    Take U Forward (TUF): https://takeuforward.org/plus/dsa/problems/left-rotate-array-by-one
    Naukri Code 360 (Coding Ninjas): https://www.naukri.com/code360/problems/left-rotate-an-array-by-one_5026278

Article: https://takeuforward.org/data-structure/left-rotate-the-array-by-one/
"""