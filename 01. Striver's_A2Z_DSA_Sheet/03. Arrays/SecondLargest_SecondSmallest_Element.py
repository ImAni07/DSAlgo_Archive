# Find the 2nd Largest Element and the 2nd Smallest Element from the Array

"""
Problem Statement:-

    Find Second Smallest and Second Largest Element in an array
    
    Given an array, 
    find the second smallest and second largest element in the array. 
    Print -1 in the event that either of them doesn't exist.

Examples:-

    Example 1:
        Input: 
            arr = [1,2,4,7,7,5]
        Output: 
            Second Smallest : 2
            Second Largest : 5
        Explanation: 
            The elements are as follows 1,2,3,5,7,7 and hence 
            second largest of these is 5 and second smallest is 2
    
    Example 2:
        Input: 
            arr = [1]
        Output: 
            Second Smallest : -1
            Second Largest : -1
        Explanation: 
            Since there is only one element in the array, 
            it is the largest and smallest element present in the array. 
            There is no second largest or second smallest element present.
"""

# Function to Calculate the 2nd Smallest Element
def secondSmallest (arr):
    
    # Size of the array
    n = len (arr)
    
    # Handle the Base Case --> Return -1, if the Array contains less than 2 elements
    if n < 2:
        return -1
    
    # Declare variables to store the smallest as well as the second smallest numbers from the array
    smallest = float ('inf')
    second_smallest = float ('inf')
    
    # Traverse through the array
    for i in range (n):
        
        # Compare the ith element to the huge value
        if arr[i] < smallest:
            second_smallest = smallest
            smallest = arr[i]
        
        elif smallest < arr[i] < second_smallest:
            second_smallest = arr[i]
        
    return second_smallest

# Function to Calculate the 2nd Largest Element
def secondLargest (arr):
    
    # Size of the array
    n = len (arr)
    
    # Handle the Base Case --> Return -1, if the Array contains less than 2 elements
    if n < 2:
        return -1
    
    # Declare variables to store the largest as well as the second largest numbers from the array
    largest = float ('-inf')
    second_largest = float ('-inf')
    
    # Traverse through the array
    for i in range (n):
        
        # Compare the ith element to the already stored small value
        if arr[i] > largest:
            second_largest = largest
            largest = arr[i]
        
        elif largest > arr[i] > second_largest:
            second_largest = arr[i]
    
    return second_largest

# Main Function
def main():
    
    # Take User Input for the Elements of the Array
    arr = list (map (int, input ("Enter the Elements of the Array:\n").split ()))
    
    # Output
    resultant_list = [(secondLargest(arr)), (secondSmallest(arr))]
    print(f"Second Smallest Element: {resultant_list[0]}")
    print(f"Second Largest Element: {resultant_list[-1]}")

if __name__ == "__main__":
    main()

# Sample Input / Output

"""
Input:

Enter the Elements of the Array:
arr = 8 8 7 6 5

Output:

Second Smallest Element: 7
Second Largest Element: 6
"""

# Links

"""
Access the Problem:-
    Take U Forward (TUF): https://takeuforward.org/plus/dsa/problems/second-largest-element
    Geeks For Geeks (GFG): https://www.geeksforgeeks.org/problems/second-largest3735/1
    Naukri Code 360 (Coding Ninjas): https://www.naukri.com/code360/problems/ninja-and-the-second-order-elements_6581960

Article: https://takeuforward.org/data-structure/find-second-smallest-and-second-largest-element-in-an-array/
"""