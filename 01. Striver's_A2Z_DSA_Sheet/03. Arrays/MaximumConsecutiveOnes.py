# Find the Maximum Number of Consecutive Ones in the given binary array

"""
Problem Statement:-

    Maximum Consecutive Ones
    
    Given a binary array nums, 
    return the maximum number of consecutive 1s in the array.

    A binary array is an array that contains only 0s and 1s.

Examples:-

    Example 1:
    
        Input: 
            nums = [1, 1, 0, 0, 1, 1, 1, 0]
        Output: 
            3
        Explanation:
            The maximum consecutive 1s are present from index 4 to index 6, amounting to 3 1s
    
    Example 2:
    
        Input: 
            nums = [0, 0, 0, 0, 0, 0, 0, 0]
        Output: 
            0
        Explanation:
            No 1s are present in nums, thus we return 0
"""

# Function to count the maximum number of consecutive ones from the given binary array
def findMaxConsecutiveOnes (nums):
    
    # Declare and initialize 2 variables for counting, both equal to 0
    max_count = 0
    count_1s = 0
    
    # Traverse through the array
    for i in range (len (nums)):
        
        # Check if whether the ith element of the array is equal to 1 or not
        if nums [i] == 1:
            
            # Increase the value of count of ones by 1
            count_1s += 1
            
            # Find the maximum value of max_count and count of ones and update it to max_count
            max_count = max (count_1s, max_count)
        
        else:
            
            # Set the value of count of ones to 0, 
            # as there are no more consecutive ones in the given binary array
            count_1s = 0
    
    # Return the max_count
    return max_count

# Main Function
def main():
    
    # Take User Input for the Elements of the Array
    nums = list (map (int, input ("Enter the Elements of the Binary Array:\n").split ()))
    
    # Output
    print (f"The Maximum Number of Consecutive 1s in the given Binary Array is:\n{findMaxConsecutiveOnes (nums)}")
    
if __name__ == "__main__":
    main ()

# Sample Input / Output

"""
Input:

Enter the Elements of the Binary Array:
nums = 1 1 0 0 1 1 1 0 1

Output:

The Maximum Number of Consecutive 1s in the given Binary Array is:
3
"""

# Links

"""
Access the Problem:-
    Take U Forward (TUF): https://takeuforward.org/plus/dsa/problems/maximum-consecutive-ones
    Leetcode (Question No. 485): https://leetcode.com/problems/max-consecutive-ones/description/
    Naukri Code 360 (Coding Ninjas): https://www.naukri.com/code360/problems/maximum-consecutive-ones_3843993

Article: https://takeuforward.org/data-structure/count-maximum-consecutive-ones-in-the-array/
"""