# Subarray Sum Equals K
# Count Subarrays with given Sum

"""
Problem Statement:-

    Given an array of integers arr and an integer k, 
    return the total number of subarrays whose sum equals to k.

Examples:-

    Example 1:
    
        Input: 
            arr = [1, 1, 1], 
            k = 2
        Output: 
            2
        Explanation: 
            In the given array [1, 1, 1], 
            there are two subarrays that sum up to 2: 
                [1, 1] and 
                [1, 1]. 
            Hence, the output is 2.
    
    Example 2:
    
        Input: 
            arr = [1, 2, 3], 
            k = 3
        Output: 
            2
        Explanation: 
            In the given array [1, 2, 3], 
            there are two subarrays that sum up to 3: 
                [1, 2] and 
                [3]. 
            Hence, the output is 2.
"""

# Import Requirements
from typing import List
from os import *
from sys import *
from collections import *
from math import *

# Function to find all the Subarrays whose summation is equal to k
def findAllSubarrayWithGivenSum (arr, k):
    
    # Declare the prerequisites
    map_ds = defaultdict(int)
    prefixSum = 0
    count = 0
    
    # Set 0 in the map
    map_ds[0] = 1
    
    # Iterate in the given array
    for i in range(len(arr)):
        
        # Add the ith element to the prefix sum
        prefixSum += arr[i]
        
        # Calculate the complement
        x = prefixSum - k
        
        # Add the number of subarrays
        count += map_ds[x]
        
        # Update the count of the Prefix Sum
        map_ds[prefixSum] += 1
    
    # Return the resultant count
    return count

# Main Function
def main():
        
    # Take User Input for the Size of the Array
    n = int(input("Enter the Size of the Array:\n"))
        
    # Take User Input for the Elements of the Array
    arr = list(map(int, input("Enter the Elements of the Array:\n").split()))
        
    # Take User Input for the Prescribed Subarray Sum
    k = int(input("Enter the Target Sum Value:\n"))
        
    # Output
    print(f"The Number of Subarrays whose Sum is equal to {k} is:\n{findAllSubarrayWithGivenSum(arr, k)}")

if __name__ == "__main__":
    main()

# Sample Input / Output

"""
Input:

Enter the Size of the Array:
n = 4

Enter the Elements of the Array:
arr = 3 1 2 4

Enter the Target Sum Value:
k = 6

Output:

The Number of Subarrays whose Sum is equal to 6 is:
2
"""

# Link

"""
Access the Problem:-
    Take U Forward (TUF): https://takeuforward.org/plus/dsa/problems/count-subarrays-with-given-sum
    Leetcode (Question No. 590): https://leetcode.com/problems/subarray-sum-equals-k/description/
    Geeks For Geeks (GFG): https://www.geeksforgeeks.org/problems/subarrays-with-sum-k/1
    Naukri Code 360 (Coding Ninjas): https://www.naukri.com/code360/problems/subarray-sums-i_1467103

Article: https://takeuforward.org/arrays/count-subarray-sum-equals-k/
"""