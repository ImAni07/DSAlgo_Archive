# Next Permutation

"""
Problem Statement:-

    A permutation of an array of integers is an arrangement of its members into a sequence or linear order.
    
    For example, 
        
        in case of permutation = [1,2,3], 
            the following are all the permutations of arr:
                
                [1,2,3], 
                [1,3,2], 
                [2,1,3], 
                [2,3,1], 
                [3,1,2], 
                [3,2,1].
    
    The next permutation of an array of integers is the next lexicographically greater permutation of its integers.
    More formally, if all the permutations of the array are sorted in lexicographical order, then 
        the next permutation of that array is the permutation that follows it in the sorted order.
    
    If such arrangement is not possible (i.e., the array is the last permutation), 
        then rearrange it to the lowest possible order (i.e., sorted in ascending order).
    
    You must rearrange the numbers in-place and use only constant extra memory.

Examples:-

    Example 1:
    
        Input: 
            permutation = [1,2,3]
        Output: 
            [1,3,2]
        Explanation:
            The next permutation of [1,2,3] is [1,3,2].
    
    Example 2:
    
        Input: 
            permutation = [3,2,1]
        Output: 
            [1,2,3]
        Explanation:
            [3,2,1] is the last permutation. 
            So we return the first: [1,2,3].
"""

# Function to find out the next lexographically greater permutation
def nextPermutation (permutation, n):
    
    # Declare a variable to store the breakpoint
    breakpoint_index = -1
    
    # Step 1: Find the breakpoint index
    for i in range ((n - 2), -1, -1):
        if (permutation[i] < permutation[i + 1]):
            breakpoint_index = i
            break
    
    # If no breakpoint is found, reverse the whole array and return
    if (breakpoint_index == -1):
        permutation.reverse()
        return permutation
    
    # Step 2: Find the immediate next greater element than the element stored in the breakpoint index
    for i in range ((n - 1), breakpoint_index, -1):
        if (permutation[i] > permutation[breakpoint_index]):
            permutation[i], permutation[breakpoint_index] = permutation[breakpoint_index], permutation[i]
            break
    
    # Step 3: Reverse the right half of the array
    
    # Declare two pointers - left and right
    left = breakpoint_index + 1
    right = n - 1
    
    # Traverse through the right half of the array
    while (left < right):
        
        # Swap the elements
        permutation[left], permutation[right] = permutation[right], permutation[left]
        
        # Increase the value of the left pointer by 1
        left += 1
        
        # Decrease the value of the right pointer by 1
        right -= 1
    
    # Return the resultant
    return permutation

# Main Function
def main():
    
    # Take User Input for the Size of the Array
    n = int (input ("Enter the Size of the Array:\n"))
        
    # Take User Input for the Elements of the Array
    permutation = list (map (int, input ("Enter the Elements of the Array:\n").split ()))
        
    # Output
    print (f"\nThe Required Next Permutation is:\n{nextPermutation (permutation, n)}")

if __name__ == "__main__":
    main()

# Sample Input / Output:

"""
Input:

Enter the Size of the Array:
n = 3

Enter the Elements of the Array:
permutation = 1 2 3

Output:

The Required Next Permutation is:
1 3 2
"""

# Link

"""
Access the Problem:-
    Take U Forward (TUF): https://takeuforward.org/plus/dsa/problems/next-permutation
    Leetcode (Question No. 31): https://leetcode.com/problems/next-permutation/description/
    Geeks For Geeks (GFG): https://www.geeksforgeeks.org/problems/next-permutation5226/1
    Naukri Code 360 (Coding Ninjas): https://www.naukri.com/code360/problems/next-greater-permutation_6929564

Article: https://takeuforward.org/data-structure/next_permutation-find-next-lexicographically-greater-permutation/
"""