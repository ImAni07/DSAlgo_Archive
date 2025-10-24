# Longest Consecutive Sequence
# Longest Successive Elements

"""
Problem Statement:-

    Given an array nums of n integers.
    
    Return the length of the longest sequence of consecutive integers.
    The integers in this sequence can appear in any order.

Examples:-

    Example 1:
    
        Input: 
            nums = [100, 4, 200, 1, 3, 2]
        Output: 
            4
        Explanation:
            The longest sequence of consecutive elements in the array is [1, 2, 3, 4], which has a length of 4. 
            This sequence can be formed regardless of the initial order of the elements in the array.

    Example 2:
    
        Input: 
            nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
        Output: 
            9
        Explanation:
            The longest sequence of consecutive elements in the array is 
            [0, 1, 2, 3, 4, 5, 6, 7, 8], which has a length of 9. 
"""

# Function to find out the Longest Consecutive Subsequence from a given Array
def longestConsecutive (nums):
    
    # Handle the edge case of no elements
    if len(nums) == 0:
        return 0
    
    # Default considerations
    longest_subsequence = 1
    count = 0
    
    # Declare a set and append all the array elements to the set
    num_set = set(nums)
    
    # Find the longest sequence
    for ele in num_set:
        
        # If 'ele' is a starting number,
        if ele-1 not in num_set:
            count = 1
            x = ele
            
            # Check if the next element of ele is present in the set, 
            # if yes, then increase the value of both x and count by 1
            
            while x+1 in num_set:
                x += 1
                count += 1
            
            # Update the value of the longest_subsequence by taking the maximum out of the count and longest_subsequence
            longest_subsequence = max (longest_subsequence, count)
    
    # Return the result
    return longest_subsequence

# Main Function
def main():
    
    # Take User Input for the Size of the Array
    n = int (input ("Enter the Size of the Array:\n"))
    
    # Take User Input for the Elements of the Array
    nums = list (map (int, input ("Enter the Elements of the Array:\n").split ()))
    
    # Output
    print (f"\nThe Longest Consecutive Sequence is:\n{longestConsecutive (nums)}")

if __name__ == "__main__":
    main ()

# Sample Input / Output

"""
Input:

Enter the Size of the Array:
n = 7

Enter the Elements of the Array:
nums = 2 6 1 3 5 4 9

The Longest Consecutive Sequence is:
6
"""

# Link

"""
Access the Problem:-
    Take U Forward (TUF): https://takeuforward.org/plus/dsa/problems/longest-consecutive-sequence-in-an-array
    Leetcode (Question No. 128): https://leetcode.com/problems/longest-consecutive-sequence/description/
    Geeks For Geeks (GFG): https://www.geeksforgeeks.org/problems/longest-consecutive-subsequence2449/1
    Naukri Code 360 (Coding Ninjas): https://www.naukri.com/code360/problems/longest-successive-elements_6811740

Article: https://takeuforward.org/data-structure/longest-consecutive-sequence-in-an-array/
"""