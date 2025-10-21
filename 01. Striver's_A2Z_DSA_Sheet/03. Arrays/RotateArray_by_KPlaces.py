# Rotate array by K elements

"""
Problem Statement:-

    Left Rotate Array by K Places
    
    Given an array of integers, rotating array of elements by k elements either left or right.

Examples:-

    Example 1:
        Input: 
            n = 7, 
            a = {1,2,3,4,5,6,7}, 
            k=2, 
            d = 'right'
        Output: 
            6 7 1 2 3 4 5
        Explanation: 
            The array is rotated to right by 2 position .

    Example 2:
        Input: 
            n = 6, 
            a = {3,7,8,9,10,11}, 
            k=3, 
            d = 'left' 
        Output: 
            9 10 11 3 7 8
        Explanation: 
            The array is rotated to right by 3 position.
"""

# Function to rotate the given array
def rotate_array(a, k, d, n):
    
    # Determine the rotating shift
    k = k % n
    
    # For Left
    if d.lower() == "left":
        
        # Store the first k elements temporarily
        temp = a[:k]
        
        # Shift the remaining elements to the left by k positions
        for i in range (k, n):
            a[i - k] = a[i]
        
        # Place the temporarily stored elements at the end
        a[n - k:] = temp
    
    # For Right
    elif d.lower() == "right":
        
        # Reverse the entire array
        a[:] = a[::-1]
        
        # Reverse the first k elements
        a[:k] = a[:k][::-1]
        
        # Reverse the remaining elements
        a[k:] = a[k:][::-1]
    
    else:
        print ("Invalid direction!")
        return None

    return a

# Main Function
def main ():
    
    # Take User Input for the Size of the Array
    n = int (input ("Enter the Size of the Array:\n"))
    
    # Take User Input for the Elements of the Array
    a = list (map (int, input ("Enter the Elements of the Array:\n").split ()))
    
    # Take User Input for the Magnitude of Left Shift Rotation of the Array
    k = int (input ("Enter the Steps:\n"))
    
    # Take user input for direction of rotation
    d = input("Enter the direction of rotation:\n")
    
    # Store the result
    result = rotate_array(a, k, d, n)
    
    # Output
    if result is not None:
        print(f"\nThe array after {k}-step {d.lower()} rotation is:\n{result}")
    
if __name__ == "__main__":
    main ()

# Sample Input / Output

"""
Test Case 1:

Input:

Enter the Size of the Array:
n = 5
Enter the Elements of the Array:
a = 1 2 3 4 5
Enter the Steps:
k = 2
Enter the direction of rotation:
d = left

Output:

The array after 2-step left rotation is:
[3, 4, 5, 1, 2]

Test Case 2:

Input:

Enter the Size of the Array:
n = 5
Enter the Elements of the Array:
a = 1 2 3 4 5
Enter the Steps:
k = 2
Enter the direction of rotation:
d = right

Output:

The array after 2-step right rotation is:
[4, 5, 1, 2, 3]
"""

# Links

"""
Access the Problem:-
    Take U Forward (TUF): https://takeuforward.org/plus/dsa/problems/left-rotate-array
    Leetcode (Question 189): https://leetcode.com/problems/rotate-array/description/
    Naukri Code 360 (Coding Ninjas): https://www.naukri.com/code360/problems/rotate-array_1230543

Article: https://takeuforward.org/data-structure/rotate-array-by-k-elements/
"""