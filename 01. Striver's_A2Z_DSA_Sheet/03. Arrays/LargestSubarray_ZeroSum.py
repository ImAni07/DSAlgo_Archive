# Longest Subarray with 0 Sum

"""
Problem Statement:-

    Largest Subarray with Sum 0
    
    You are given an integer array arr of size n which contains both positive and negative integers. 
    Your task is to find the length of the longest contiguous subarray with sum equal to 0.
    Return the length of such a subarray. 
    If no such subarray exists, return 0.

Examples:-

    Example 1:
    
        Input: 
            arr = [15, -2, 2, -8, 1, 7, 10, 23]
        Output: 
            5
        Explanation:
            The subarray [-2, 2, -8, 1, 7] sums up to 0 and has the maximum length among all such subarrays.
    
    Example 2:
    
        Input: 
            arr = [2, 10, 4]
        Output: 
            0
        Explanation:
            There is no subarray whose elements sum to 0.
"""

# Function to calculate the highest length of the subarray with sum equal to 0
def getLongestZeroSumSubarrayLength (arr):
    
    # Declare a hashmap
    hashmap = {}
    
    # Variable to store sum of the subarrays
    subarray_sum = 0
    
    # Variable to store the lengths of the subarrays
    subarray_maximum_length = 0
    
    # Iterate through the array
    for i in range (len(arr)):
        
        # Add the current element
        subarray_sum += arr[i]
        
        # Check if the subarray sum is equal to 0 or not
        if subarray_sum == 0:
            subarray_maximum_length = i + 1
        
        else:
            # Check if the subarray sum is already present in the hashmap or not
            if subarray_sum in hashmap:
                
                # If the subarray sum is already present in the hashmap, then update the subarray maximum
                subarray_maximum_length = max (subarray_maximum_length, i - hashmap[subarray_sum])
            
            else:
                # If the subarray sum is not present in the hashmap, then add it to the hashmap
                hashmap[subarray_sum] = i
    
    # Return the resultant
    return subarray_maximum_length

# Main Function
def main():
    
    # Take User Input for the Size of the Array
    n = int (input ("Enter the Size of the Array:\n"))
    
    # Take User Input for the Elements of the Array
    arr = list (map (int, input("Enter the Elements of the Array:\n").split()))
    
    # Output
    print (f"Length of the Longest Subarray with 0 Sum is:\n{getLongestZeroSumSubarrayLength (arr)}")

if __name__ == "__main__":
    main()

# Sample Input / Output

"""
Input:

Enter the Size of the Array:
n = 5

Enter the Elements of the Array:
arr = 3 -2 1 -2 1

Output:

Length of the Longest Subarray with 0 Sum is:
4
"""

# Link

"""
Access the Problem:-
    Take U Forward (TUF): https://takeuforward.org/plus/dsa/problems/largest-subarray-with-sum-0
    Geeks For Geeks (GFG): https://www.geeksforgeeks.org/problems/largest-subarray-with-0-sum/1
    Naukri Code 360 (Coding Ninjas): https://www.naukri.com/code360/problems/longest-subarray-zero-sum_757507

Article: https://takeuforward.org/data-structure/length-of-the-longest-subarray-with-zero-sum/
"""