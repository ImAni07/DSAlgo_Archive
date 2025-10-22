# Linear Search

"""
Problem Statement:-

    Array Search
    
    Given an array of integers and an integer target, 
    find the smallest index (0 based indexing) where the target appears in the array. 
    If the target is not found in the array, return -1.
    
Examples:-

    Example 1:
        Input:
            nums = [2, 3, 4, 5, 3], 
            target = 3
        Output: 
            1
        Explanation:
            The first occurence of 3 in nums is at index 1
"""

# Function to search a given element in the give array, linearly
def linearSearch(nums, target) :
    
    # Size of the array
    n = len (nums)
    
    # Traverse through the Array
    for i in range (0, n):
        
        # Check whether the element is present or not
        # If present, return the index of the first occurrence
        
        if (nums[i] == target):
            return i
    
    # If not present, return -1
    return -1

# Main Function
def main():
    
    # Take User Input for the Elements of the Array
    nums = list(map(int, input("Enter the Elements of the Array:\n").split()))
    
    # Take User Input for the Element to be Searched
    target = int (input ("Enter the Value of the Target Element:\n"))
    
    # Store the result
    result = linearSearch (nums, target)
    
    # Output
    if result == -1:
        print (f"The Target Value {target} is not present --> -1")
    else:
        print (f"The Target Value {target} is present at Index --> {linearSearch (nums, target)}")

if __name__ == "__main__":
    main()

# Sample Input / Output

"""
Test Case 1:

Input:

Enter the Elements of the Array:
nums = 1 2 3 4 5

Enter the Value of the Target Element:
target = 3

Output:
The Target Value 3 is present at Index --> 2

Test Case 2:

Input:

Enter the Elements of the Array:
nums = 5 4 3 2 1

Enter the Value of the Target Element:
target = 6

Output:
The Target Value 6 is not present --> -1

Test Case 3:

Input:

Enter the Elements of the Array:
nums = 7 8 9 5 9

Enter the Value of the Target Element:
target = 5

Output:
The Target Value 5 is present at Index --> 3
"""

# Links

"""
Access the Problem:-
    Take U Forward (TUF): https://takeuforward.org/plus/dsa/problems/linear-search
    Geeks For Geeks (GFG): https://www.geeksforgeeks.org/problems/search-an-element-in-an-array-1587115621/1
    Naukri Code 360 (Coding Ninjas): https://www.naukri.com/code360/problems/linear-search_624470

Article: https://takeuforward.org/data-structure/linear-search-in-c/
"""