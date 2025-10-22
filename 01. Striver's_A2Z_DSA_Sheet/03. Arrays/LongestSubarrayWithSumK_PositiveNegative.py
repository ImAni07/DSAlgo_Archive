# Longest Subarray Sum with Sum K (Positive and Negative)

"""
Problem Statement:-

    Longest subarray with sum K
    
    Given an array nums of size n and an integer k, 
    find the length of the longest sub-array that sums to k. 
    If no such sub-array exists, return 0.

Examples:-

    Example 1:
    
        Input: 
            nums = [10, 5, 2, 7, 1, 9],
            k=15
        Output: 
            4
        Explanation:
            The longest sub-array with a sum equal to 15 is [5, 2, 7, 1], 
                which has a length of 4. 
            This sub-array starts at index 1 and ends at index 4, 
                and the sum of its elements (5 + 2 + 7 + 1) equals 15. 
            Therefore, the length of this sub-array is 4.
    
    Example 2:
    
        Input: 
            nums = [-3, 2, 1], 
            k=6
        Output: 
            0
        Explanation:
            There is no sub-array in the array that sums to 6. 
            Therefore, the output is 0.
"""

# Function to find the required longest subarray with the given sum
def getLongestSubarray (nums, k):
    
    # Declare variables to store the sum of the subarray and to store the maximum length
    currentSum = 0
    maxLength = 0
    
    # Declare a hashmap to store the required prefix sum
    prefixSumMap = {}
    
    # Traverse through the array
    for i in range (len(nums)):
        currentSum += nums[i]
        
        if currentSum == k:
            maxLength = max(maxLength, (i + 1))
        
        # Calculate the remaining sum
        remainingSum = currentSum - k
        
        if remainingSum in prefixSumMap:
            maxLength = max(maxLength, (i - prefixSumMap[remainingSum]))
        
        if currentSum not in prefixSumMap:
            prefixSumMap[currentSum] = i
    
    return maxLength

# Main Function
def main():
    
    # Take User Input for the Size of the Array
    n = int (input ("Enter the Size of the Array:\n"))
    
    # Take User Input for the Elements of the Array
    nums = list (map (int, input ("Enter the Elements of the Array:\n").split ()))
    
    # Take User Input for the Required Subarray Sum
    k = int (input ("Enter the Required Subarray Sum:\n"))
    
    # Output
    print (f"The Length of the Longest Subarray with a Required Subarray Sum of {k} is {getLongestSubarray (nums, k)}")

if __name__ == "__main__":
    main()

# Sample Input / Output

"""
Input:

Enter the Size of the Array:
n = 6

Enter the Elements of the Array:
nums = 10 5 2 7 1 -10

Enter the Required Subarray Sum:
k = 15

Output:

The Length of the Longest Subarray with a Required Subarray Sum of 15 is 6
"""

# Links

"""
Access the Problem:-
    Take U Forward (TUF): https://takeuforward.org/plus/dsa/problems/longest-subarray-with-sum-k
    Geeks For Geeks (GFG): https://www.geeksforgeeks.org/problems/longest-sub-array-with-sum-k0809/1
    Leetcode (Question No. 325): https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/description/

Article: https://takeuforward.org/arrays/longest-subarray-with-sum-k-postives-and-negatives/
"""