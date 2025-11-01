# Search Insert Position

"""
Problem Statement:-

    Search Insert Position
    
    Given a sorted array arr consisting of distinct integers and a target value, 
        return the index if the target is found. 
    If not, return the index where it would be if it were inserted in order.

Examples:-

    Example 1:
    
        Input: 
            arr = [1, 3, 5, 6], 
            target = 5
        Output: 
            2
        Explanation: 
            The target value 5 is found at index 2 in the sorted array. 
            Hence, the function returns 2.
    
    Example 2:
    
        Input: 
            arr = [1, 3, 5, 6], 
            target = 2
        Output: 
            1
        Explanation: 
            The target value 2 is not found in the array. 
            However, it should be inserted at index 1 to maintain the sorted order of the array.
"""

# Function to find out the insert position of an element in a sorted array
def searchInsert(arr, target):
    
    # Declare and initialize the required pointers
    lo = 0
    hi = len(arr) - 1
    
    # Declare a variable to store the answer
    ans = len(arr)
    
    # Traverse through the array
    while lo <= hi:
        
        # Update the value of the mid pointer
        mid = (lo + hi) // 2
        
        # Check if the value present at the mid index is greater than or equal to the given target value
        if arr[mid] >= target:
            
            # If yes, then update the value of answer variable
            ans = mid
            
            # Check for other smaller indices
            hi = mid - 1
        
        else:
            
            # Check in the right half of the given array
            lo = mid + 1
    
    # Return the result
    return ans

# Main Function
def main():
    
    # Take User Input for the Size of the Array
    n = int (input ("Enter the Size of the Array:\n"))
    
    # Take User Input for the Elements of the Array
    arr = list(map(int, input("Enter the Elements of the Array:\n").split()))
    
    # Take User Input for the Target Element
    target = int (input ("Enter the Target Element:\n"))
    
    # Output
    print(f"The Index is: {searchInsert(arr, target)}")

if __name__ == "__main__":
    main()

# Sample Input / Output

"""
Test Case 1 --> If the Target is not present

Input:

Enter the  Size of the Array:
n = 4

Enter the Elements of the Array:
arr = 1 2 4 7

Enter the Target Element:
target = 6

Output:

The Index is: 3

Test Case 2 --> If the Target is present

Input:

Enter the  Size of the Array:
n = 4

Enter the Elements of the Array:
arr = 1 2 4 7

Enter the Target Element:
target = 2

Output:

The Index is: 1
"""

# Link

"""
Access the Problem:-
    Take U Forward (TUF): https://takeuforward.org/plus/dsa/problems/search-insert-position
    Leetcode (Question No. 35): https://leetcode.com/problems/search-insert-position/description/
    Geeks For Geeks (GFG): https://www.geeksforgeeks.org/problems/search-insert-position-of-k-in-a-sorted-array/1
    Naukri Code 360 (Coding Ninjas): https://www.naukri.com/code360/problems/algorithm-to-find-best-insert-position-in-sorted-array_839813

Article: https://takeuforward.org/arrays/search-insert-position/
"""