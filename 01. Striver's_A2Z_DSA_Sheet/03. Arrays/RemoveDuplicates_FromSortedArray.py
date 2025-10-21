# Remove Duplicate Elements from a given Sorted Array

"""
Problem Statement:-

    Remove duplicates from sorted array
    
    Given an integer array, sorted in non-decreasing order, 
    remove all duplicates in-place so that each unique element appears only once.
    
    An array sorted in non-decreasing order is an array 
    where every element to the right of an element is either equal to or greater in value than that element.

Examples:-

    Example 1:
    
        Input:
            nums = [0, 0, 3, 3, 5, 6]
        Output: 
            4
            [0, 3, 5, 6, _]
        Explanation:
            Resulting array = [0, 3, 5, 6, _, _]
            There are 4 distinct elements in nums and the elements marked as _ can have any value.
    
    Example 2:
    
        Input:
            nums = [-2, 2, 4, 4, 4, 4, 5, 5]
        Output: 
            4
            [-2, 2, 4, 5, _]
        Explanation:
            Resulting array = [-2, 2, 4, 5, _, _, _, _]
            There are 4 distinct elements in nums and the elements marked as _ can have any value.
"""

# Function to remove duplicate elements from the given sorted array
def removeDuplicates(nums):
    
    # Declare a pointer i and initialize it to 0
    i = 0
    
    # Traverse the array
    for j in range(1, len(nums)):
        if nums[i] != nums[j]:
            i += 1
            nums[i] = nums[j]
    
    return (i + 1)

# Function to print the unique elements of the array
def printUniqueElements(nums):

    for k in range (removeDuplicates(nums)):
        print(nums[k], end= " ")
    print ()

# Main Function
def main():
    
    # Take User Input for the Elements of the Array
    nums = list(map(int, input("Enter the Elements:\n").split()))
    
    # Call the function once and store the result
    unique_count = removeDuplicates(nums)

    # Output
    print(f"The Number of Unique Elements:\n{unique_count}")
    print("The Array with Unique Elements:")
    printUniqueElements(nums)
    
if __name__ == "__main__":
    main()

# Sample Input / Output

"""
Input:

Enter the Elements:
nums = 0 0 3 5 6 6

Output:

The Number of Unique Elements:
4

The Array with Unique Elements:
0 3 5 6
"""

# Links

"""
Access the Problem:-
    Take U Forward (TUF): https://takeuforward.org/plus/dsa/problems/remove-duplicates-from-sorted-array
    Leetcode (Question No. 26): https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
    Geeks For Geeks (GFG): https://www.geeksforgeeks.org/problems/remove-duplicate-elements-from-sorted-array/1
    Naukri Code 360 (Coding Ninjas): https://www.naukri.com/code360/problems/remove-duplicates-from-sorted-array_1102307

Article: https://takeuforward.org/data-structure/remove-duplicates-in-place-from-sorted-array/
"""