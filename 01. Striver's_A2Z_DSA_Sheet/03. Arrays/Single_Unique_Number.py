# Single Number Problem
# Unique Number

"""
Problem Statement:-

    Find the Number Appearing Only Once from an Array, where all the other Numbers appear Twice
    
    Given an array of nums of n integers. 
    Every integer in the array appears twice except one integer. 
    Find the number that appeared once in the array.

Examples:-

    Example 1:
    
        Input: 
            nums = [1, 2, 2, 4, 3, 1, 4]
        Output: 
            3
        Explanation: 
            The integer 3 has appeared only once.
"""

# Function to find the number appearing only once from an array, where all the other numbers appear twice
def singleNumber (nums):
    
    # Declare and initialize a variable to store the xor of all the elements of the given array
    resultant_xor = 0
    
    # Traverse the Array
    for i in range (len (nums)):
        
        # Perform Xor Operations upon the elements of the array
        resultant_xor ^= nums[i]
    
    # Return the result as the single number will be equal to the result of the xor
    return resultant_xor

# Main Function
def main():
    
    # Take User Input for the Size of the Array
    n = int (input ("Enter the Size of the Array:\n"))
    
    # Take User Input for the Elements of the Array
    nums = list (map (int, input ("Enter the Elements of the Array:\n").split ()))
    
    # Output
    print (f"The Unique Number in the given Array is:\n{singleNumber (nums)}")

if __name__ == "__main__":
    main()

# Sample Input / Output

"""
Input:

Enter the Size of the Array:
n = 5

Enter the Elements of the Array:
nums = 4 1 2 1 2

Output:

The Unique Number in the given Array is:
4
"""

# Links

"""
Access the Problem:-
    Take U Forward (TUF): https://takeuforward.org/plus/dsa/problems/single-number---i
    Leetcode (Question No. 136): https://leetcode.com/problems/single-number/description/ 
    Geeks For Geeks (GFG): https://www.geeksforgeeks.org/problems/find-unique-number/1
    Naukri Code 360 (Coding Ninjas): https://www.naukri.com/code360/problems/find-the-single-element_6680465

Articles: https://takeuforward.org/arrays/find-the-number-that-appears-once-and-the-other-numbers-twice/
"""