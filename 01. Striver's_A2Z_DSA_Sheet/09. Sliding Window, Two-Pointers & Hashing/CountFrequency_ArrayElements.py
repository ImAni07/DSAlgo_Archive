# Count Frequency of Each Element in the Array

"""
Problem Statement:-

    Counting Frequencies of Array Elements
    
    Given an array nums of size n which may contain duplicate elements, 
    return a list of pairs where each pair contains a unique element from the array and its frequency in the array.
    
    You may return the result in any order, but each element must appear exactly once in the output.

Examples:-

    Example 1:
    
    Input: 
        nums = [1, 2, 2, 1, 3]
    Output: 
        [[1, 2], [2, 2], [3, 1]]
    Explanation:
        - 1 appears 2 times
        - 2 appears 2 times
        - 3 appears 1 time
    
    Example 2:
    
        Input: 
            nums = [5, 5, 5, 5]
        Output: 
            [[5, 4]]
        Explanation:
        - 5 appears 4 times.
"""

# Function to count Frequencies of the elements in the given array
def countFrequencies (nums):
    
    # Initialize a hashmap
    hashmap_dict = {}
    
    # Iterate through the given array
    for i in range (len (nums)):
        
        # Check if the element is present or not
        if nums[i] in hashmap_dict:
            
            # If it is present, then increase its frequency by 1
            hashmap_dict[nums[i]] += 1
        
        else:
            # Initialize its frequency to 1
            hashmap_dict[nums[i]] = 1
    
    # Print
    for x in hashmap_dict:
        print ([x, hashmap_dict[x]], end=" ")

# Main Function
def main ():
    
    # Take User Input
    nums = list(map(int, input("Enter the elements of the array: ").split()))
    
    # Output
    countFrequencies(nums)

if __name__ == "__main__":
    main ()

# Sample Input / Output

"""
Input:

Enter the elements of the array: 
nums = [10 5 10 15 10 5]

Output:

[10, 3] [5, 2] [15, 1]
"""

# Links

"""
Access the Problem:-
    Take U Forward (TUF): https://takeuforward.org/plus/dsa/problems/counting-frequencies-of-array-elements
    Geeks For Geeks (GFG): https://www.geeksforgeeks.org/problems/frequency-of-elements--111353/1

Article: https://takeuforward.org/data-structure/count-frequency-of-each-element-in-the-array/
"""