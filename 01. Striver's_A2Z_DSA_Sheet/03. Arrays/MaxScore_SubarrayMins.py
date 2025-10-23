# Maximum Score from Subarray Minimums

"""
Problem Statement:-

    Max Score from Subarray Minimums
    
    You are given an array arr[] of integers. 
    Your task is to find the maximum sum of the smallest and second smallest elements 
        across all subarrays (of size >= 2) of the given array.

Examples:-

    Example 1:
    
        Input: 
            arr[] = [4, 3, 5, 1]
        Output: 
            8
        Explanation: 
            All subarrays with at least 2 elements and find the two smallest numbers in each:
                [4, 3] → 3 + 4 = 7
                [4, 3, 5] → 3 + 4 = 7
                [4, 3, 5, 1] → 1 + 3 = 4
                [3, 5] → 3 + 5 = 8
                [3, 5, 1] → 1 + 3 = 4
                [5, 1] → 1 + 5 = 6
            Maximum Score is 8.
    
    Example 2:
    
        Input: 
            arr[] = [1, 2, 3]
        Output: 
            5
        Explanation: 
            All subarray with at least 2 elements and find the two smallest numbers in each:
                [1, 2] → 1 + 2 = 3
                [1, 2, 3] → 1 + 2 = 3
                [2, 3] → 2 + 3 = 5
            Maximum Score is 5
"""

# Function to calculate the maximum score from subarray minimums
def pairWithMaxSum (arr):
    
    # Check for the Base Cases
    if len (arr) < 2:
        return -1

    # Declare a variable to store the required sum
    # initialize it by the sum of the 1st 2 elements of the given array
    requiredSum = arr [0] + arr [1]
    
    # Traverse in the Array
    for i in range (1, (len(arr)-1)):
        
        # Update the value of the resultant sum
        requiredSum = max (requiredSum, arr [i] + arr [i+1])
    
    # Return the resultant
    return requiredSum

# Main Function
def main():
    
    # Take User Input for the Size of the Array
    n = int (input ("Enter the Size of the Array:\n"))
    
    # Take User Input for the Elements of the Array
    arr = list (map (int, input ("Enter the Elements of the Array:\n").split ()))
    
    # Output
    print (f"The Maximum Score of the Subarray Minimums is: {pairWithMaxSum (arr)}")

if __name__ == "__main__":
    main()

# Sample Input / Output

"""
Input:

Enter the Size of the Array:
n = 4

Enter the Elements of the Array:
arr = 4 3 5 1

Output:

The Maximum Score of the Subarray Minimum is 8
"""

# Link

"""
Access the Problem:-
    Geeks For Geeks (GFG): https://www.geeksforgeeks.org/problems/max-sum-in-sub-arrays0824/1
"""