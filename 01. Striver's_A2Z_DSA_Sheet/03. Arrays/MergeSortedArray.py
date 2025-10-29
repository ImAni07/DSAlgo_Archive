# Merge Two Sorted Arrays Without Using Extra Space
# Merge Sorted Array

"""
Problem Statement:-

    Merge Sorted Array
    
    Given two sorted integer arrays a and b, 
        merge both the arrays into a single array sorted in non-decreasing order.
    The final sorted array should be stored inside the array a and it should be done in-place.
    Array a has a length of m + n, 
        where the first m elements denote the elements of a and 
        rest are 0s whereas nums2 has a length of n.

Examples:-

    Example 1:
    
        Input: 
            a = [-5, -2, 4, 5, 0, 0, 0], 
            b = [-3, 1, 8]
        Output: 
            [-5, -3, -2, 1, 4, 5, 8]
        Explanation: 
            The merged array is: 
                [-5, -3, -2, 1, 4, 5, 8], 
                    where [-5, -2, 4, 5] are from a and [-3, 1, 8] are from b
    
    Example 2:
    
        Input: 
            a = [0, 2, 7, 8, 0, 0, 0], 
            b = [-7, -3, -1]
        Output:  
            [-7, -3, -1, 0, 2, 7, 8]
        Explanation: 
            The merged array is: 
                [-7, -3, -1, 0, 2, 7, 8], 
                    where [0, 2, 7, 8] are from a and [-7, -3, -1] are from b
"""

# Way 1
# Using 2 Pointers

# Function to merge two sorted arrays without using any extra space
def merge (a, b):
    
    # Initialize two pointers
    left = len(a) - 1
    right = 0
    
    # Traverse through the arrays
    while left >= 0 and right < len(b):
        
        # If the current element in array a is greater than the current element in array b
        if a[left] > b[right]:
            
            # Swap the elements
            a[left], b[right] = b[right], a[left]
            
            # Move the pointer in array b to the next element
            right += 1
            
            # Move the pointer in array a to the previous element
            left -= 1
        
        # If the current element in array a is not greater than the current element in array b
        else:
            break
    
    # Sort the arrays individually
    a.sort()
    b.sort()

# Way 2
# Using Gap Method

# Function for Swapping the values
def swapValues (a, b, index1, index2):
    
    # Check whether the value present at index1 in Array a is greater than the value present at index2 in Array b
    if a[index1] > b[index2]:
        
        # If the condition is satisfied, swap the values
        a[index1], b[index2] = b[index2], a[index1]

# Function to merge two sorted arrays without using any extra space
def mergeTwoSortedArraysWithoutExtraSpace (a, b):
    
    # Determine the Length of the Combination of the given two arrays
    length = (len(a) + len(b))
    
    # Initialize the gap
    gap = int ((length / 2) + (length % 2))
    
    # Traverse through the loop, until the value of gap is greater than 0
    while gap > 0:
        
        # Declare and initialize two pointers
        left_pointer = 0
        right_pointer = left_pointer + gap
        
        # Iterate through the arrays
        while right_pointer < length:
            
            # Case 1 
            # When the left pointer is in Array a and the right pointer is in Array b
            if left_pointer < len(a) and right_pointer >= len(b):
                
                # Swap the values
                swapValues (a, b, left_pointer, (right_pointer - (len(a))))
            
            # Case 2 
            # When both the pointers are in Array b
            elif left_pointer >= len(a):
                
                # Swap the values
                swapValues (b, b, (left_pointer - (len(a))), (right_pointer - (len(a))))
            
            # Case 3 
            # When both the pointers are in Array a
            else:
                
                # Swap the vales
                swapValues (a, a, left_pointer, right_pointer)
            
            # Increase the value of left pointer by 1
            left_pointer += 1
            
            # Increase the value of right pointer by 1
            right_pointer += 1
            
        # If the gap value becomes 1, then break out
        if gap == 1:
            break
        
        # Update the value of gap
        gap = int ((gap / 2) + (gap % 2))

# Main Function
def main ():
    
    # Take User Input for the Size of the 1st Array
    n = int (input ("Enter the Size of the 1st Array:\n"))
    
    # Take User Input for the Size of the 2nd Array
    m = int (input ("Enter the Size of the 2nd Array:\n"))
    
    # Take User Input for the Elements of the 1st Array
    a = list(map(int, input("Enter the Elements of the 1st Array:\n").split()))
    a.sort()

    # Take User Input for the Elements of the 2nd Array
    b = list(map(int, input("Enter the Elements of the 2nd Array:\n").split()))
    b.sort()

    # Way of Merging
    print("\nChoose the merging method:")
    print("1. Using Two Pointers")
    print("2. Using Gap Method")

    # Choose
    choice = int(input("Enter your choice:\n"))

    if choice == 1:
        merge(a, b)
        method = "Two Pointer Method"
    
    elif choice == 2:
        mergeTwoSortedArraysWithoutExtraSpace(a, b)
        method = "Gap Method"
    
    else:
        print("Invalid choice! Please enter 1 or 2.")
        return

    # Output
    print(f"\nArrays merged successfully using {method}!")
    print("Merged Arrays:")
    print(*a, *b)

if __name__ == "__main__":
    main ()

# Sample Input / Output

"""
Test Case 1:

Input:

Enter the Size of the 1st Array:
n = 4

Enter the Size of the 2nd Array:
m = 3

Enter the Elements of the 1st Array:
a = 1 4 8 10

Enter the Elements of the 2nd Array:
b = 2 3 9

Message:

Choose the merging method:
1. Using Two Pointers
2. Using Gap Method

Choice:

Enter your choice:
1

Output:

Arrays merged successfully using Two Pointer Method!
Merged Arrays:
1 2 3 4 8 9 10

Test Case 2:

Input:

Enter the Size of the 1st Array:
n = 4

Enter the Size of the 2nd Array:
m = 3

Enter the Elements of the 1st Array:
a = 1 4 8 10

Enter the Elements of the 2nd Array:
b = 2 3 9

Message:

Choose the merging method:
1. Using Two Pointers
2. Using Gap Method

Choice:

Enter your choice:
2

Output:

Arrays merged successfully using Gap Method!
Merged Arrays:
1 2 3 4 8 9 10
"""

# Link

"""
Access the Problem:-
    Take U Forward (TUF): https://takeuforward.org/plus/dsa/problems/merge-two-sorted-arrays-without-extra-space
    Leetcode (Question No. 88): https://leetcode.com/problems/merge-sorted-array/description/
    Geeks For Geeks (GFG): https://www.geeksforgeeks.org/problems/merge-two-sorted-arrays-1587115620/1
    Naukri Code 360 (Coding Ninjas): https://www.naukri.com/code360/problems/merge-two-sorted-arrays-without-extra-space_6898839

Article: https://takeuforward.org/data-structure/merge-two-sorted-arrays-without-extra-space/
"""