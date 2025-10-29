# Maximum Product Subarray

"""
Problem Statement:-

    Given an integer array arr. 
    Find the subarray with the largest product, and 
        return the product of the elements present in that subarray.
    
    A subarray is a contiguous non-empty sequence of elements within an array.

Examples:-

    Example 1:
    
        Input: 
            arr = [4, 5, 3, 7, 1, 2]
        Output: 
            840
        Explanation:
            The largest product is given by the whole array itself
    
    Example 2:
    
        Input: 
            arr = [-5, 0, -2]
        Output: 
            0
        Explanation:
            The largest product is achieved with the following subarrays 
                [0], 
                [-5, 0], 
                [0, -2], 
                [-5, 0, -2].
"""

# Function to calculate the Maximum Product Subarray from the given Array
def subarrayWithMaxProduct (arr):
    
    # Declare and initialize the required variables
    prefix_product = 1
    suffix_product = 1
    answer = float('-inf')
    
    # Traverse through the array
    for i in range(len(arr)):
        
        # Check whether the prefix becomes 0 or not, if yes, then reset the prefix to 1
        if prefix_product == 0:
            prefix_product = 1
        
        # Check whether the suffix becomes 0 or not, if yes, then reset the suffix to 1
        if suffix_product == 0:
            suffix_product = 1
        
        # If no 0s are encountered
        prefix_product *= arr[i]
        suffix_product *= arr[len(arr) - i - 1]
        
        # Update the answer
        answer = max(answer, max(prefix_product, suffix_product))
    
    # Return the result
    return answer

# Main Function
def main():
    
    # Take User Input for the Size of the Array
    n = int (input ("Enter the Size of the Array:\n"))
    
    # Take User Input for the Elements of the Array
    arr = list (map (int, input ("Enter the Elements of the Array:\n").split ()))
    
    # Output
    print (f"The Maximum Product of Subarray in the given Array is:\n{subarrayWithMaxProduct (arr)}")

if __name__ == "__main__":
    main ()

# Sample Input / Output

"""
Input:

Enter the Size of the Array:
n = 6

Enter the Elements of the Array:
arr = 2 6 -3 -10 0 2

Output:

The Maximum Product of Subarray in the given Array is"
180
"""

# Link

"""
Access the Problem:-
    Take U Forward (TUF): https://takeuforward.org/data-structure/maximum-product-subarray-in-an-array/
    Leetcode (Question No. 152): https://leetcode.com/problems/maximum-product-subarray/description/
    Geeks For Geeks (GFG): https://www.geeksforgeeks.org/problems/maximum-product-subarray3604/1
    Naukri Code 360 (Coding Ninjas): https://www.naukri.com/code360/problems/maximum-product-subarray_1115474

Article: https://takeuforward.org/plus/dsa/problems/maximum-product-subarray-in-an-array
"""