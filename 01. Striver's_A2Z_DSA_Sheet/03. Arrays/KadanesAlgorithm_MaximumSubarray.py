# Kadane's Algorithm
# Maximum Subarray Sum

"""
Problem Statement:-

    Maximum Subarray
    Kadane's Algorithm
    
    Given an integer array, 
    find the subarray with the largest sum, and 
    return its sum.

Examples:-

    Example 1:

        Input: 
            arr = [2, 3, 5, -2, 7, -4]
        Output: 
            15
        Explanation:
            The subarray from index 0 to index 4 has the largest sum = 15
    
    Example 2:
    
        Input: 
            arr = [-2, -3, -7, -2, -10, -4]
        Output: 
            -2
        Explanation:
            The element on index 0 or index 3 make up the largest sum when taken as a subarray

Follow - up Question:

    Find the contiguous subarray (containing at least one number) 
    which has the largest sum and 
    print the subarray.

Examples:

    Example 1:
    
        Input: 
            arr = [1, 2, 3]
        Output: 
            [1, 2, 3]
        Explanation: 
            In the given array, every element is non-negative, 
            so the entire array [1, 2, 3] is the valid subarray with the maximum sum.
    
    Example 2:
    
        Input: 
            arr = [-1, 2]
        Output: 
            [2]
        Explanation: 
            The only valid non-negative subarray is [2], so the output is [2].
"""

# Function to Calculate the Maximum Subarray Sum from the given Array
def maxSubarraySum (arr, n):
    
    # Approach Used --> Kadane's Algorithm
    
    # Declare maximum element of the array to the 0th element and sum to 0
    maximum_subarray_sum = arr [0]
    subarray_sum = 0
    
    # Traverse through the array
    for i in range (n):
        
        # Calculate the current subarray sum
        subarray_sum += arr [i]
        
        # Update the maximum value
        maximum_subarray_sum = max (maximum_subarray_sum, subarray_sum)
        
        # Check if the current sum is positive or negative, 
        # Reset the value, if it is negative
        if subarray_sum < 0:
            subarray_sum = 0
    
    # Check for the Base Cases
    if n == 0:
        return 0
    
    elif n == 1:
        return arr [0]
    
    # Return 0 if none of the subarray sum is positive
    if maximum_subarray_sum < 0:
        return 0
    
    return maximum_subarray_sum

# Function to print the subarray with the maximum sum
def print_max_subarray (arr, n):
    
    # Initialize the maximum sum with the 1st element
    max_sum = arr[0]
    
    # Initalize the current sum to be 0
    current_sum = 0
    
    # Declare the pointers
    start = 0
    end = 0
    temp = 0
    
    # Traverse through the array
    for i in range (n):
        current_sum += arr[i]
        
        # Update the maximum sum and the indices
        if current_sum > max_sum:
            max_sum = current_sum
            start = temp
            end = i
        
        # Reset if the current sum becomes negative
        if current_sum < 0:
            current_sum = 0
            temp = i + 1
    
    # Print the Subarray with Maximum Sum
    
    print(f"Subarray with Maximum Sum:\n{arr[start:end+1]}")
    print(f"Maximum Subarray Sum:\n{max_sum}")

# Main Function
def main():
    
    # Take User Input for the Size of the Array
    n = int (input ("Enter the Size of the Array:\n"))
    
    # Take User Input for the Elements of the Array
    arr = list (map (int, input ("Enter the Elements of the Array:\n").split()))
    
    # Compute the Maximum Subarray Sum
    max_subarray_sum = maxSubarraySum(arr, n)
    
    # Print the Subarray having Maximum Sum
    print_max_subarray(arr, n)

if __name__ == "__main__":
    main()

# Sample Input / Output

"""
Input:

Enter the Size of the Array:
n = 5

Enter the Elements of the Array:
arr = 5 4 -1 7 8

Output:

Subarray with Maximum Sum:
[5, 4, -1, 7, 8]

Maximum Subarray Sum:
23
"""

# Link

"""
Access the Problem:-
    Take U Forward (TUF): https://takeuforward.org/plus/dsa/problems/kadane's-algorithm
    Leetcode (Question No. 53): https://leetcode.com/problems/maximum-subarray/description/
    Geeks For Geeks (GFG): https://www.geeksforgeeks.org/problems/kadanes-algorithm-1587115620/1
    Naukri Code 360 (Coding Ninjas): https://www.naukri.com/code360/problems/maximum-subarray-sum_630526

Article: https://takeuforward.org/data-structure/kadanes-algorithm-maximum-subarray-sum-in-an-array/
"""