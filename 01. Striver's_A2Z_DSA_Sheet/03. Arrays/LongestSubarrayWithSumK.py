# Longest Subarray with a given Sum K (Positive)

"""
Problem Statement:-

    Given an array of size n and an integer k, 
    find the length of the longest sub-array that sums to k. 
    If no such sub-array exists, return 0.

Examples:-

    Example 1:
    
        Input: 
            a = [10, 5, 2, 7, 1, 9],  
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
            a = [-3, 2, 1], k=6
        Output: 
            0
        Explanation:
            There is no sub-array in the array that sums to 6. 
            Therefore, the output is 0.
"""

# Function to find the longest subarray sum, which is equal to k
def longestSubarrayWithSumK (a, k):
    
    # Declare and initialize two pointers, i as left pointer and j as right pointer, both equal to 0
    i = 0
    j = 0
    
    # Declare two variables to store the sum of the subarray as well as the length of the subarray
    sum = a[0]
    maximumLength = 0
    
    # Traverse through the loop
    while j < len(a):
        
        while i <= j and sum > k:
            sum -= a[i]
            i += 1
        
        if sum == k:
            maximumLength = max(maximumLength, j - i + 1)
        
        j += 1
        
        if j < len(a):
            sum += a[j]
    
    return maximumLength

# Main Function
def main():
    
    # Take User Input for the Size of the Array
    n = int (input ("Enter the Size of the Array:\n"))
    
    # Take User Input for the Elements of the Array
    a = [int (x) for x in input("Enter the Elements of the Array:\n").split()]
    
    # Take User Input for the Required Value of Subarray Sum
    k = int (input ("Enter the Value of Subarray Sum:\n"))
    
    # Output
    print (f"The Length of the Longest Subarray Sum with a Value of {k} is {longestSubarrayWithSumK (a, k)}")

if __name__ == "__main__":
    main()

# Sample Input / Output

"""
Input:

Enter the Size of the Array:
n = 7

Enter the Elements of the Array:
a = 1 2 3 1 1 1 1

Enter the Value of Subarray Sum:
k = 3

Output:

The Length of the Longest Subarray Sum with a Value of 3 is 3
"""

# Link

"""
Access the Problem:-
    Take U Forward (TUF): https://takeuforward.org/plus/dsa/problems/longest-subarray-with-sum-k
    Naukri Code 360 (Coding Ninjas): https://www.naukri.com/code360/problems/longest-subarray-with-sum-k_6682399

Article: https://takeuforward.org/data-structure/longest-subarray-with-given-sum-k/
"""