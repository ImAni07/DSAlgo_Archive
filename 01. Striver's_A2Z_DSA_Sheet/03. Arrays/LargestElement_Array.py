# Find the Largest Element of the Array

"""
Problem Statement:-

    Largest Element
    
    Given an array of integers, return the value of the largest element in the array.
    
Examples:-

    Example 1:
        Input: 
            nums = [3, 3, 6, 1]
    Output: 
        6
    Explanation: 
        The largest element in array is 6
"""

# Function to find the largest element of the array
def largest (arr):
    
    # Declare a variable to store the highest element of the array and initialize it with the first element of the array
    max_element = arr[0]
    
    # Iterate through the array
    for i in range (len (arr)):
        
        # Compare the ith element of the array with the value stored in the max_element variable
        if max_element < arr[i]:
            max_element = arr[i]
    
    return max_element

# Main Function
def main():
    
    # Take user input for the size of the array
    n = int (input ())
    
    # Take User Input for the elements of the array
    arr = list (map (int, input ().split ()))
    
    # Print the Output
    print (largest (arr))

if __name__ == "__main__":
    main()

# Sample Input / Output

"""
Input:

n = 11
arr = 45 77 18 96 1 33 8 23 11 93 73

Output:

96
"""

# Links

"""
Access the Problem:-
    Take U Forward (TUF): https://takeuforward.org/plus/dsa/problems/largest-element
    Geeks For Geeks (GFG): https://www.geeksforgeeks.org/problems/largest-element-in-array4009/1
    Naukri Code 360 (Coding Ninjas): https://www.naukri.com/code360/problems/largest-element-in-the-array-largest-element-in-the-array_5026279

Article: https://takeuforward.org/data-structure/find-the-largest-element-in-an-array/
"""