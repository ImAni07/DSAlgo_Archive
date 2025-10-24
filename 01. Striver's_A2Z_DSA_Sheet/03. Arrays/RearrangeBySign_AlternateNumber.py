# Rearrange by Sign
# Alternate Number

# Variant 1
# When the Number of Positive Elements are equal to the Number of Negative Elements

"""
Problem Statement:-

    Rearrange array elements by sign

    Given an integer array nums of even length consisting of an equal number of positive and negative integers.
    
    Return the answer array in such a way that the given conditions are met:
        
        Every consecutive pair of integers have opposite signs.
        For all integers with the same sign, the order in which they were present in the given array is preserved.
        The rearranged array begins with a positive integer.

Example:-

    Example 1:
    
        Input: 
            a = [2, 4, 5, -1, -3, -4]
        Output: 
            [2, -1, 4, -3, 5, -4]
        Explanation:
            The positive number 2, 4, 5 maintain their relative positions and 
            -1, -3, -4 maintain their relative positions
    
    Example 2:
    
        Input: 
            a = [1, -1, -3, -4, 2, 3]
        Output: 
            [1, -1, 2, -3, 3, -4]
        Explanation:
            The positive number 1, 2, 3 maintain their relative positions and 
            -1, -3, -4 maintain their relative positions
"""

# Code for Variant 1

# Function to rearrange the elements of the given array by sign
def rearrangeArray (a):
    
    # Define a list to store the result
    result = [0] * len(a)
    
    # Declare two pointers for the indices of positive and negative numbers
    pos = 0
    neg = 1
    
    # Traverse in the array
    for i in range(len(a)):
        
        # Check whether the ith element is positive or negative
        if a[i] > 0:
            result[pos] = a[i]
            pos += 2
        
        else:
            result[neg] = a[i]
            neg += 2
    
    # Return the rearranged array
    return result

# Variant 2
# When the Number of Positive Elements are not equal to the Number of Negative Elements

"""
Problem Statement:-

    Alternate Numbers
    
    There is an array a of size n with positive and negative elements (not necessarily equal). 
    Without altering the relative order of positive and negative elements, return an array of alternately positive and negative values. 
    The leftover elements should be placed at the very end in the same order as in the given array a.
    
    Note: Start the array with positive elements.

Examples:-

    Example 1:
    
        Input:
            a = {1,2,-4,-5,3,4}, 
            n = 6
        Output:
            1 -4 2 -5 3 4
        Explanation: 
            Positive elements = 1,2
            Negative elements = -4,-5
            To maintain relative ordering, 1 must occur before 2, and -4 must occur before -5.
            Leftover positive elements are 3 and 4 which are then placed at the end of the array.
    
    Example 2:
    
        Input:
            a = {1,2,-3,-1,-2,-3}, 
            n = 6
        Output:
            1 -3 2 -1 3 -2
        Explanation: 
            Positive elements = 1,2
            Negative elements = -3,-1,-2,-4
            To maintain relative ordering, 1 must occur before 2.
            Also, -3 should come before -1, and -1 should come before -2.
            After alternate ordering, -2 and -4 are left, which would be placed at the end of the ans array.
"""

# Code for Variant 2

# Function to alter the numbers according to their signs
def alternatenumbers (a):
    
    # Define 2 lists to store positive and negative numbers
    positive_num = []
    negative_num = []
    
    # Segregate the array into positives and negatives
    for i in range (len (a)):
        if a[i] >= 0:
            positive_num.append(a[i])
        else:
            negative_num.append(a[i])
    
    # Case 1 --> When Positives are lesser than Negatives
    if len (positive_num) < len (negative_num):
        
        # Fill the array alternatively, until the number of pos = neg
        for i in range (len (positive_num)):
            a[2 * i] = positive_num[i]
            a[2 * i + 1] = negative_num[i]
        
        # Fill the remaining negatives at the end of the array.
        index = len(positive_num)*2
        for i in range(len(negative_num)-len(positive_num)):
            a[index] = negative_num[len(positive_num)+i]
            index += 1
    
    # Case 2 --> When Positives are more than Negatives
    else:
        
        # Fill the array alternatively, until the number of pos = neg
        for i in range (len (negative_num)):
            a[2 * i] = positive_num[i]
            a[2 * i + 1] = negative_num[i]
        
        # Fill the remaining positives at the end of the array.
        index = len(negative_num)*2
        for i in range(len(positive_num)-len(negative_num)):
            a[index] = positive_num[len(negative_num)+i]
            index += 1
    
    # Return the modified array
    return a

# Main Function
def main ():
    
    # Take User Input for the Size of the Array
    n = int (input ("Enter the Size of the Array:\n"))
    
    # Take User Input for the Elements of the Array
    a = list (map (int, input ("Enter the Elements of the Array:\n").split ()))
    
    # Count the number of positive elements and negative elements
    positive_count = len ([i for i in a if i > 0])
    negative_count = len ([i for i in a if i < 0])
    
    # Choose the function to use
    if positive_count == negative_count:
        answer = rearrangeArray (a)
        print("\nEqual Number of Positive Elements and Negative Elements have been Detected!")
    else:
        answer = alternatenumbers (a)
        print("\nUnequal Number of Positive Elements and Negative Elements have been Detected!")
    
    # Output
    print(f"\nRearranged by Array Sign:\n{answer}")

if __name__ == "__main__":
    main ()

# Sample Input / Output

"""
Test Case 1 --> Variant 1

Input:

Enter the Size of the Array:
n = 6

Enter the Elements of the Array:
a = 1 2 -1 -2 -3 3

Output:

Equal Number of Positive Elements and Negative Elements have been Detected!

Rearranged by Array Sign:
[1, -1, 2, -2, 3, -3]

Test Case 2 --> Variant 2

Input:

Enter the Size of the Array:
n = 6

Enter the Elements of the Array:
a = 1 2 3 -4 4 -5

Output:

Unequal Number of Positive Elements and Negative Elements have been Detected!

Rearranged by Array Sign:
[1, -4, 2, -5, 3, 4]
"""

# Link

"""
Access the Problem:-
    Take U Forward (TUF): https://takeuforward.org/plus/dsa/problems/rearrange-array-elements-by-sign
    Leetcode (Question No. 2149): https://leetcode.com/problems/rearrange-array-elements-by-sign/description/
    Geeks For Geeks (GFG): https://www.geeksforgeeks.org/problems/array-of-alternate-ve-and-ve-nos1401/1
    Naukri Code 360 (Coding Ninjas): https://www.naukri.com/code360/problems/alternate-numbers_6783445

Article: https://takeuforward.org/arrays/rearrange-array-elements-by-sign/
"""