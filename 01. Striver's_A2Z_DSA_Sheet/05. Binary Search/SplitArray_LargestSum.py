# Split Array Largest Sum

"""
Problem Statement:-

    Given an integer array nums of size n and an integer k. 
    Split the array a into k non-empty subarrays such that the largest sum of any subarray is minimized. 
    Return the minimized largest sum of the split.

Examples:-

    Example 1:
    
        Input: 
            nums = [1, 2, 3, 4, 5], 
            k = 3
        Output:
            6
        Explanation: 
            There are many ways to split the array a[] into k consecutive subarrays. 
            The best way to do this is to split the array a[] into -
                [1, 2, 3], 
                [4], and 
                [5], 
                    where the largest sum among the three subarrays is only 6.
    
    Example 2:
    
        Input: 
            nums = [3,5,1], 
            k = 3
        Output: 
            5
        Explanation: 
            There is only one way to split the array a[] into 3 subarrays - 
                [3], 
                [5], and 
                [1]. 
                    The largest sum among these subarrays is 5.
"""

# Function to count the number of subarrays required to split the array with the given maximum sum
def countPartitions (nums, max_sum):
    
    # Count of partitions required
    partition_count = 1
    
    # Total sum variable to keep track of the total sum of the current partition
    total_sum = 0
    
    # Length of the array
    n = len (nums)
    
    # Iterate through the array
    for i in range (n):
        
        # Calculate the total sum of the current partition, 
        # given that it does not exceed the maximum sum
        if total_sum + nums[i] <= max_sum:
            total_sum += nums[i]
        
        else:
            # If the total sum exceeds the maximum sum, create a new partition
            partition_count += 1
            total_sum = nums[i]
    
    # Return the number of partitions required
    return partition_count

# Function to find the minimum largest sum of the partitions
def splitArray (nums, k):
    
    # Initialize the low and high pointers
    lo = max (nums)
    hi = sum (nums)
    
    # Apply Binary Search
    while lo <= hi:
        
        # Update mid
        mid = (lo + hi) // 2
        
        # Check the number of partitions required to split the array with the current maximum sum
        
        # If it is less than or equal to k
        if countPartitions(nums, mid) <= k:
            
            # If yes, then try for a smaller maximum sum
            hi = mid - 1
            
        else:
            # If no, then try for a larger maximum sum
            lo = mid + 1
            
    # Return the minimum largest sum of the partitions
    return lo

# Main Function
def main ():
    
    # Take User Input for the Size of the Array
    n = int (input ("Enter the Size of the Array:\n"))
    
    # Take User Input for the Elements of the Array
    nums = list (map (int, input ("Enter the Elements of the Array:\n").split ()))
    
    # Take User Input for the Number of Partitions
    k = int (input ("Enter the Value of k --> Number of Partitions:\n"))
    
    # Print the minimum largest sum of the partitions
    print (f"The Minimum Largest Sum of the Partitions with {k} Subarrays is {splitArray (nums, k)}")

if __name__ == "__main__":
    main ()

# Sample Input / Output

"""
Input:

Enter the Size of the Array:
n = 5

Enter the Elements of the Array:
nums = 1 2 3 4 5

Enter the Value of k --> Number of Partitions:
k = 2

Output:

The Minimum Largest Sum of the Partitions with 2 Subarrays is 9
"""

# Link

"""
Access the Problem:-
    Take U Forward (TUF): https://takeuforward.org/plus/dsa/problems/split-array---largest-sum
    Leetcode (Question No. 410): https://leetcode.com/problems/split-array-largest-sum/description/
    Geeks For Geeks (GFG): https://www.geeksforgeeks.org/problems/split-array-largest-sum--141634/1
    Naukri Code 360 (Coding Ninjas): https://www.naukri.com/code360/problems/split-the-given-array-into-k-sub-arrays_1215015

Article: https://takeuforward.org/arrays/split-array-largest-sum/
"""