# 4 Sum
# Find Quads that add up to a target value
# All Quadruples

"""
Problem Statement:-

    4 Sum
    Find Quads that add up to a target value
    All Quadruples
    
    Given an integer array nums and an integer target. 
    
    Return all quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
        a, b, c, d are all distinct valid indices of nums.
        nums[a] + nums[b] + nums[c] + nums[d] == target.
    
    Notice that the solution set must not contain duplicate quadruplets. 
    One element can be a part of multiple quadruplets. 
    The output and the quadruplets can be returned in any order.

Examples:-

    Example 1:
    
        Input: 
            nums = [1, -2, 3, 5, 7, 9], 
            target = 7
        Output: 
            [[-2, 1, 3, 5]]
        Explanation:
            nums[1] + nums[0] + nums[2] + nums[3] = 7
    
    Example 2:
    
        Input: 
            nums = [7, -7, 1, 2, 14, 3], 
            target = 9
        Output: 
            []
        Explanation:
            No quadruplets are present which add upto 9
"""

# Function to find quads that add up to the target value
def fourSum(nums, target):
    
    # Declare an empty list for result
    quads = []
    
    # Sort the given array
    nums.sort()
    
    # Traverse through the array and fix the 1st element of the quad
    for a in range (len(nums)):
        
        # Skip the Duplicates
        if a > 0 and nums[a] == nums[a - 1]:
            continue
        
        # Traverse through the array and fix the 2nd element of the quad
        for b in range (a + 1, len(nums)):
            
            # Skip the duplicates
            if b > a + 1 and nums[b] == nums[b - 1]:
                continue
            
            # Declare 2 pointers
            c = b + 1
            d = len(nums) - 1
            
            # Iterate through the array with these 2 pointers
            while c < d:
                
                # Calculate the sum of the quad
                quad_sum = nums[a] + nums[b] + nums[c] + nums[d]
                
                # Check whether the sum of the quad is equal to the target or not
                # If the sum of the quad is less than the target
                if quad_sum < target:
                    c += 1
                
                # If the sum of the quad is more than the target
                elif quad_sum > target:
                    d -= 1
                
                # If the sum of the quad is equal to the target
                else:
                    
                    # Add the quad to the list
                    x = [nums[a], nums[b], nums[c], nums[d]]
                    quads.append(x)
                    
                    # Move the pointers to find the next quad
                    c += 1
                    d -= 1
                    
                    # Skip the duplicates for j pointer
                    while c < d and nums[c] == nums[c - 1]:
                        c += 1
                
                    # Skip the duplicates for k pointer
                    while c < d and nums[d] == nums[d + 1]:
                        d -= 1
    
    # Return the result
    return quads

# Main Function
def main():
    
    # Take User Input for the Size of the Array
    n = int (input("Enter the Size of the Array:\n"))
    
    # Take User Input for the Target Sum Value
    target = int (input("Enter the Target Sum Value:\n"))
    
    # Take User Input for the Elements of the Array
    nums = list(map(int, input("Enter the Elements of the Array:\n").split()))
    
    # Store the result
    answer = fourSum(nums, target)
    
    # Output
    print(f"The Number of Required Quads that Add up to the Target Value of {target} is:\n{len(answer)}")
    print(f"The Required Quads List:\n{answer}")

if __name__ == "__main__":
    main()

# Sample Input / Output

"""
Input:

Enter the Size of the Array:
n = 6

Enter the Target Sum Value:
target = 8

Enter the Elements of the Array:
nums = 2 2 2 2 1 3

Output:

The Number of Required Quads that Add up to the Target Value of 8 is:
2

The Required Quads List:
[[2, 2, 2, 2], [2, 2, 1, 3]]
"""

# Link

"""
Access the Problem:-
    Take U Forward (TUF): https://takeuforward.org/plus/dsa/problems/4-sum
    Leetcode (Question No. 18): https://leetcode.com/problems/4sum/description/
    Geeks For Geeks (GFG): https://www.geeksforgeeks.org/problems/find-all-four-sum-numbers1732/1
    Naukri Code 360 (Coding Ninjas): https://www.naukri.com/code360/problems/4sum_5713771

Article: https://takeuforward.org/data-structure/4-sum-find-quads-that-add-up-to-a-target-value/
"""