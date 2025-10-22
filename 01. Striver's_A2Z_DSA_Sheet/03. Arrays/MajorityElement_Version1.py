# Majority Element --> N/2

"""
Problem Statement:-

    Find the Majority Element that occurs more than N/2 times
    
    Given an integer array nums of size n, return the majority element of the array.
    
    The majority element of an array is an element that appears more than n/2 times in the array. 
    The array is guaranteed to have a majority element.

Examples:-

    Example 1:
    
        Input: 
            nums = [7, 0, 0, 1, 7, 7, 2, 7, 7]
        Output: 
            7
        Explanation:
            The number 7 appears 5 times in the 9 sized array
    
    Example 2:
    
        Input: 
            nums = [1, 1, 1, 2, 1, 2]
        Output: 
            1
        Explanation:
            The number 1 appears 4 times in the 6 sized array
"""

# Approach Used: Moore's Voting Algorithm

# Function to find the majority element (the element that occurs more than (n / 2) times)
def majorityElements (nums):
    
    # Declare and initialize a variable to store the candidate elements to None
    element = None
    
    # Declare and initialize a counter variable to 0
    count = 0
    
    # Size of the given array
    n = len(nums)
    
    # Traverse through the array
    for i in range(n):
        
        # Check whether count is 0, 
        # if yes, update the candidate element with the ith element of the given array and 
        # update the value of count to 1
        
        if count == 0:
            count = 1
            element = nums[i]
        
        # Check whether the ith element of the array is equal to the candidate element, 
        # if yes, increase the value of count by 1
        
        elif element == nums[i]:
            count += 1
        
        # If the ith element of the array is not equal to the candidate element, 
        # then decrease the value of count by 1
        
        else:
            count -= 1
    
    # Store the frequency
    freq = 0
    
    # Traverse through the array
    for i in range(n):
        
        # Check whether the ith element is equal to the candidate element, 
        # if yes, then increase the value of frequency by 1
        
        if nums[i] == element:
            freq += 1
    
    # Check whether the frequency is in majority or not, with respect to the size of the array, 
    # if yes, then return the element
    
    if freq > n / 2:
        return element
    
    # If no majority element is obtained by traversing through the array, then return -1
    return -1

# Main Function
def main():
    
    # Take User Input for the Size of the Array
    n = int (input ("Enter the Size of the Array:\n"))
    
    # Take User Input for the Elements of the Array
    nums = list (map (int, input ("Enter the Elements of the Array:\n"). split()))
    
    # Output
    print (f"Result:\n{majorityElements (nums)}")

if __name__ == "__main__":
    main()

# Sample Input / Output

"""
Input:

Enter the Size of the Array:
n = 10

Enter the Elements of the Array:
nums = 4 4 2 4 3 4 4 3 2 4

Output:

Result:
4
"""

# Link

"""
Access the problem:-
    Take U Forward (TUF): https://takeuforward.org/plus/dsa/problems/majority-element-i
    Leetcode (Question No. 169): https://leetcode.com/problems/majority-element/description/
    Geeks For Geeks (GFG): https://www.geeksforgeeks.org/problems/majority-element-1587115620/1
    Naukri Code 360 (Coding Ninjas): https://www.naukri.com/code360/problems/majority-element_842495

Article: https://takeuforward.org/data-structure/find-the-majority-element-that-occurs-more-than-n-2-times/
"""