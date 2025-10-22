# Two Sum

"""
Problem Statement:-

    Two Sum with Input Array Sorted
    
    Given an array of integers nums, that is already sorted in non-decreasing order, 
    find two numbers such that they add up to a specific target number. 
    Let these two numbers be numbers[index1] and numbers[index2] 
    where 1 <= index1 < index2 <= numbers.length.
    
    Return the indices of the two numbers, index1 and index2, 
    [index1, index2] of length 2.

Examples:-

    Example 1:

        Input: 
            nums = [2,7,11,15], 
            target = 9
        Output: 
            [0,1]
        Explanation: 
            The sum of 2 and 7 is 9. 
            Therefore, index1 = 0, index2 = 1. 
            We return [0, 1].
    
    Example 2:
    
        Input: 
            nums = [2,3,4], 
            target = 6
        Output: 
            [0,2]
        Explanation: 
            The sum of 2 and 4 is 6. 
            Therefore index1 = 0, index2 = 2. 
            We return [0, 2].
    
    Example 3:
    
        Input: 
            nums = [-1,0], 
            target = -1
        Output: 
            [0,1]
        Explanation: 
            The sum of -1 and 0 is -1. 
            Therefore index1 = 0, index2 = 1. 
            We return [1, 2].
"""

# Variant 1
# Input Array is Sorted
# Return the indices of the required numbers

# Function to find the two numbers that would add up to the target number
def twoSum_sorted (nums, target):
    
    # Size of the array
    n = len (nums)
    
    # Declare and initialize two pointers
    i = 0
    j = n - 1
    
    # Traverse through the array
    while i < j:
        
        # Calculate the sum of the elements at the current positions of the two pointers
        current_sum = nums [i] + nums [j]
        
        # Check condition
        if current_sum < target:
            i += 1
        
        elif current_sum > target:
            j -= 1
        
        else:
            return [i, j]
    
    # If the target sum is not obtained, return -1
    return [-1, -1]

"""
Problem Statement:-

    Two Sum with Input Array Unsorted
    
    Given an array of integers nums and an integer target. 
    Return the indices(0 - indexed) of two elements in nums such that they add up to target.

Examples:-

    Example 1:
    
        Input: 
            nums = [1, 6, 2, 10, 3], 
            target = 7
        Output: 
            [0, 1]
        Explanation:
            nums[0] + nums[1] = 1 + 6 = 7
    
    Example 2:
    
        Input: 
            nums = [1, 3, 5, -7, 6, -3], 
            target = 0
        Output: 
            [1, 5]
        Explanation:
            nums[1] + nums[5] = 3 + (-3) = 0
"""

# Variant 2
# Input Array is not Sorted
# Return the indices of the required numbers

# Function to find the two numbers that would add up to the target number
def twoSum_unsorted (nums, target):
    
    # Declare a set to be used as hashmap
    number_map = {}
    
    # Traverse through the array
    for i in range(len(nums)):
        
        # Calculate the difference between the target and the current number
        diff = target - nums[i]
        
        # Check if the required number is in the map
        if diff in number_map:
            return [number_map[diff], i]
        
        # If the required number is not in the map, then add it to the map
        number_map[i] = i
    
    # If the numbers are not present, return -1
    return [-1, -1]

"""
Problem Statement:-

    Two Sum - Pair with Given Sum
    
    Given an array nums of integers and another integer target. 
    Determine if there exist two distinct indices such that the sum of their elements is equal to the target.

Examples:-

    Example 1:
    
        Input: 
            nums = [0, -1, 2, -3, 1], 
            target = -2
        Output: 
            YES
        Explanation: 
            nums[3] + nums[4] = -3 + 1 = -2
    
    Example 2:
    
        Input: 
            nums = [1, -2, 1, 0, 5], 
            target = 0
        Output: 
            NO
        Explanation: 
            None of the pair makes a sum of 0
    
    Example 3:
    
        Input: 
            nums = [11], 
            target = 11
        Output: 
            NO
        Explanation: 
            No pair is possible as only one element is present in nums
"""

# Variant 3
# Works for both sorted and unsorted input arrays
# Checks the availability of the numbers that would add up to the target number
# Returns YES or NO

# Function to check the availability of two numbers that would add up to the target number
def twoSum_check (nums, target):
    
    # Size of the array
    n = len (nums)
    
    # Declare a set to be used as hashmap
    number_map = {}
    
    # Traverse through the array
    for i in range(n):
        
        # Calculate the difference between the target and the current number
        diff = target - nums[i]
        
        # Check if the required number is in the map
        if diff in number_map:
            return "YES"
        
        # If the required number is not in the map, then add it to the map
        number_map[nums[i]] = i
    
    # If the numbers are not present, return -1
    return "NO"

# Function to check if the array is sorted
def is_sorted(nums):
    return all(nums[i] <= nums[i + 1] for i in range(len(nums) - 1))

# Main Function
def main ():
    
    print("Select Output Type:\n")
    print("1. Return Indices\n")
    print("2. Return Boolean\n")
    print("\n")
    
    # Enter the Choice
    choice = int (input ("Enter the Choice:\n"))
    
    # Take user input for the size of the array
    n = int(input("\nEnter the size of the array:\n"))
    
    # Take user input for the elements of the array
    nums = list(map(int, input("Enter the array elements:\n").split()))
    
    # Take user input for the required target sum
    target = int(input("Enter the target sum:\n"))

    # Check whether the array is sorted or not
    sorted_flag = is_sorted(nums)

    if sorted_flag:
        
        print("\nThe array is sorted.")
        
        if choice == 1:
            print("Output:", twoSum_sorted(nums, target))
        
        elif choice == 2:
            print("Output:", twoSum_check(nums, target))
        
        else:
            print("Invalid choice! Choose 1 or 2.")
    
    else:
        
        print("\nThe array is unsorted.")
        
        if choice == 1:
            print("Output:", twoSum_unsorted(nums, target))
        
        elif choice == 2:
            print("Output:", twoSum_check(nums, target))
        
        else:
            print("Invalid choice! Choose 1 or 2.")

if __name__ == "__main__":
    main()

# Sample Input / Output

"""
Test Case 1:

Input:

Select Output Type:
1. Return Indices
2. Return Boolean

Enter the Choice:
1

Enter the Size of the Array:
n = 5

Enter the Array Elements:
nums = 1 2 3 4 5

Enter the Target Sum:
target = 7

Output:

The array is sorted.

Output: [2, 3]


Test Case 2:

Input:

Select Output Type:
1. Return Indices
2. Return Boolean

Enter the Choice:
2

Enter the Size of the Array:
n = 5

Enter the Array Elements:
nums = 1 2 3 4 5

Enter the Target Sum:
target = 7

Output:

The array is sorted.

Output: YES


Test Case 3:

Input:

Select Output Type:
1. Return Indices
2. Return Boolean

Enter the Choice:
1

Enter the Size of the Array:
n = 5

Enter the Array Elements:
nums = 4 1 2 3 1

Enter the Target Sum:
target = 5

Output:

The array is unsorted.

Output: [0, 1]


Test Case 4:

Input:

Select Output Type:
1. Return Indices
2. Return Boolean

Enter the Choice:
2

Enter the Size of the Array:
n = 5

Enter the Array Elements:
nums = 2 6 5 8 11

Enter the Target Sum:
target = 14

Output:

The array is unsorted.

Output: YES
"""

# Links

"""
Access the Problem:-

    Variant 1:
        Leetcode (Question No. 167) --> https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
    
    Variant 2:
        Take U Forward (TUF) --> https://takeuforward.org/plus/dsa/problems/two-sum
        Leetcode (Question No. 1) --> https://leetcode.com/problems/two-sum/description/
    
    Variant 3:
        Geeks For Geeks (GFG) --> https://www.geeksforgeeks.org/problems/key-pair5616/1
        Naukri Code 360 (Coding Ninjas) --> https://www.naukri.com/code360/problems/reading_6845742?leftPanelTabValue=PROBLEM

Article: https://takeuforward.org/data-structure/two-sum-check-if-a-pair-with-given-sum-exists-in-array/
"""