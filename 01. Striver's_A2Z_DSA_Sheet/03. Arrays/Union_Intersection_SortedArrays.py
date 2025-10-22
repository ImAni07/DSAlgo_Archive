# Union (Merge) & Intersection of 2 Sorted Arrays

# Merge 2 Sorted Arrays

"""
Problem Statement:-

    Union of two sorted arrays
    
    Given two sorted arrays nums1 and nums2,
    return an array that contains the union of these two arrays. 
    The elements in the union must be in ascending order.
    
    The union of two arrays is an array 
    where all values are distinct and are present in either the first array, the second array, or both.

Examples:-

    Example 1:
    
        Input:
            nums1 = [1, 2, 3, 4, 5], 
            nums2 = [1, 2, 7]
        Output: 
            [1, 2, 3, 4, 5, 7]
        Explanation:
            The elements 1, 2 are common to both, 3, 4, 5 are from nums1 and 7 is from nums2
    
    Example 2:
    
        Input: 
            nums1 = [3, 4, 6, 7, 9, 9], 
            nums2 = [1, 5, 7, 8, 8]
        Output: 
            [1, 3, 4, 5, 6, 7, 8, 9]
        Explanation:
            The element 7 is common to both, 3, 4, 6, 9 are from nums1 and 1, 5, 8 is from nums2
"""

# Union (Merge) of 2 Sorted Arrays
# Way 1 --> Using Two Pointers

# Function to find Union of 2 given Sorted Arrays
def sortedArray (nums1, nums2):
    
    # Declare and initialize two pointers i and j, for arrays nums1 and nums2, respectively
    i = 0
    j = 0
    
    # Declare a separate list to store the resultant
    resultant_union = []
    
    # Traverse through the array as long as the values of the pointers are less than the lengths of the given arrays
    while i < len(nums1) and j < len(nums2):
        
        # Check if the ith element of Array nums1 is less than equal to the jth element of Array nums2
        if nums1[i] <= nums2[j]:
            
            # Check if either the resultant list is empty or the last appended element is not equal to the ith element of Array nums1
            if len (resultant_union) == 0 or resultant_union[-1] != nums1[i]:
                
                # If the conditions satisfy, then append the ith element of Array nums1 to the resultant list
                resultant_union.append(nums1[i])
            
            # Increase the value of the pointer
            i += 1
        
        else:
            
            # Check if either the resultant list is empty or the last appended element is not equal to the jth element of Array nums2
            if len (resultant_union) == 0 or resultant_union[-1] != nums2[j]:
                
                # If the conditions satisfy, then append the jth element of Array nums2 to the resultant list
                resultant_union.append(nums2[j])
            
            # Increase the value of the pointer
            j += 1
        
    # Traverse through the Array nums1, in order to append the left out elements to the resultant list
    while i < len(nums1):
        
        # Check if the last appended element is not equal to the ith element of Array a
        if resultant_union[-1] != nums1[i]:
            
            # If the conditions satisfy, then append the ith element of Array a to the resultant list
            resultant_union.append(nums1[i])
        
        # Increase the value of the pointer
        i += 1
    
    # Perform the same traversal for Array nums2
    while j < len(nums2):
        
        # Check if the last appended element is not equal to the jth element of Array nums2
        if resultant_union[-1] != nums2[j]:
            
            # If the conditions satisfy, then append the jth element of Array b to the resultant list
            resultant_union.append(nums2[j])
        
        # Increase the value of the pointer
        j += 1
    
    # Return the result
    return resultant_union

# Union (Merge) of 2 Sorted Arrays
# Way 2 --> Use the in-build sort()

# Function to merge two sorted arrays without using any extra space
def merge (nums1, nums2):
        
    # Extend nums1 with all elements from nums2
    nums1.extend(nums2)
    
    # Sort the combined list
    nums1.sort()
    
    # Remove duplicates to form a proper union
    union_list = []
    
    # Traverse through the combined list
    for num in nums1:
        if len(union_list) == 0 or union_list[-1] != num:
            union_list.append(num)
    
    return union_list

# Intersection of Two Sorted Arrays

"""
Problem Statement:-

    Find the Common Elements of the given 2 Arrays
    
    Given two integer arrays nums1 and nums2, 
    return an array of their intersection. 
    Each element in the result must be unique and you may return the result in any order.

Examples:-

    Example 1:
    
        Input: 
            nums1 = [1,2,2,1], 
            nums2 = [2,2]
        Output: 
            [2]
    
    Example 2:
    
        Input: 
            nums1 = [4,9,5], 
            nums2 = [9,4,9,8,4]
        Output: 
            [9,4]
        Explanation: 
            [4,9] is also accepted.
"""

# Intersection of Arrays
# Way 1 --> Using Two - pointer Approach

# Function to find the intersection of given sorted arrays
def findArrayIntersection (nums1, nums2):
    
    # Declare and initialize two pointers i and j, equal to 0, for the given two arrays, respectively
    i = 0
    j = 0
    
    # Declare a list to store the resultant
    intersection_list = []
    
    # Traverse through the array as long as the values of the pointers are less than the lengths of the given arrays
    while i < len(nums1) and j < len(nums2):
        
        # Check the conditions for appending
        
        # Condition 1: If the ith element of the 1st array is less than the jth element of the 2nd array
        if nums1[i] < nums2[j]:
            
            # Increment the value of pointer i
            i += 1
        
        # Condition 2: If the jth element of the 2nd array is less than the ith element of the 1st array
        elif nums2[j] < nums1[i]:
            
            # Increment the value of pointer j
            j += 1
        
        # Condition 3: If the ith element of the 1st array is equal to the jth element of the 2nd array
        else:
            
            # Append only if it's not a duplicate
            if len(intersection_list) == 0 or intersection_list[-1] != nums1[i]:
                intersection_list.append(nums1[i])
            i += 1
            j += 1
    
    # Return the result
    return intersection_list

# Intersection of Arrays
# Way 2 --> Using Set

# Function to find the intersection in one-line
def intersection (nums1, nums2):
    
    # Return the List of Set of both the arrays
    return list (set(nums1) & set(nums2))

# Main Function
def main ():
    
    # Take User Inputs
    
    # For the 1st Array
    
    # Size
    m = int (input ("Enter the Size of the 1st Array:\n"))
    
    # Elements
    nums1 = list (map (int, input ("Enter the Elements of the 1st Array:\n").split ()))
    
    # For the 2nd Array
    
    # Size
    n = int (input ("Enter the Size of the 2nd Array:\n"))
    
    # Elements
    nums2 = list (map (int, input ("Enter the Elements of the 2nd Array:\n").split ()))
    
    # Store the Results
    union1 = sortedArray(nums1, nums2)
    union2 = merge(nums1, nums2)
    intersection1 = findArrayIntersection(nums1, nums2)
    intersection2 = intersection(nums1, nums2)
    
    # Output
    print("\nUnion of 2 Arrays:-\n")
    print(f"Using Two - Pointer Approach:\n{union1}")
    print(f"\nUsing sort():\n{union2}")
    print()
    print("Intersection of 2 Arrays:-\n")
    print(f"Using Two - Pointer Approach:\n{intersection1}")
    print(f"Using set:\n{intersection2}")

if __name__ == "__main__":
    main ()

# Sample Input / Output

"""
Input:

Enter the Size of the 1st Array:
m = 3

Enter the Elements of the 1st Array:
nums1 = 1 2 3

Enter the Size of the 2nd Array:
n = 3

Enter the Elements of the 2nd Array:
nums2 = 2 5 6

Output:

Union of 2 Arrays:-

Using Two - Pointer Approach:
[1, 2, 3, 5, 6]

Using sort():
[1, 2, 3, 5, 6]

Intersection of 2 Arrays:-

Using Two - Pointer Approach:
[2]

Using set:
[2]
"""

# Links

"""
Access the Problems:-

    Union:
    
        Take U Forward (TUF): https://takeuforward.org/plus/dsa/problems/union-of-two-sorted-arrays
        Leetcode (Question No. 88): https://leetcode.com/problems/merge-sorted-array/description/
        Geeks For Geeks (GFG): https://www.geeksforgeeks.org/problems/union-of-two-sorted-arrays-1587115621/1
        Naukri Code 360 (Coding Ninjas): https://www.naukri.com/code360/problems/sorted-array_6613259
    
    Intersection:
    
        Leetcode (Question No. 349): https://leetcode.com/problems/intersection-of-two-arrays/submissions/1564093860/
        Geeks For Geeks (GFG): https://www.geeksforgeeks.org/problems/intersection-of-two-sorted-arrays-with-duplicate-elements/1
        Naukri Code 360 (Coding Ninjas): https://www.naukri.com/code360/problems/intersection-of-2-arrays_1082149
    
    Tutorial:
    
        Article: https://takeuforward.org/data-structure/union-of-two-sorted-arrays/
        Video: https://youtu.be/wvcQg43_V8U
"""