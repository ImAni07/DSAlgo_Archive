# Move Zeroes

"""
Problem Statement:-

    Move All Zeroes To The End
    
    Given an integer array, 
    move all the 0's to the end of the array. 
    The relative order of the other elements must remain the same.
    
    This must be done in place, without making a copy of the array.
    

Examples:-

    Example 1:
        Input: 
            a = [0, 1, 4, 0, 5, 2]
        Output: 
            [1, 4, 5, 2, 0, 0]
        Explanation:
            Both the zeroes are moved to the end and the order of the other elements stay the same
    
    Example 2:
        Input: 
            a = [0, 0, 0, 1, 3, -2]
        Output: 
            [1, 3, -2, 0, 0, 0]
        Explanation:
            All 3 zeroes are moved to the end and the order of the other elements stay the same
"""

# Function to move all the 0s to the end
def moveZeroes (n, a):
    
    # Declare and initialize a couple of pointers, i and j to 0
    i = 0
    j = 0
    
    # Traverse the array
    while i < n:
        
        # Check if the element is non-zero or not
        if a[i] != 0:
            
            # Swap them
            a[i], a[j] = a[j], a[i]
            
            # Move the non - zero pointer
            j += 1
        
        # Move the loop pointer
        i += 1
    
    return a

# Main Function
def main():
    
    # Take User Input for the Size of the Array
    n = int (input ("Enter the Size of the Array:\n"))
    
    # Take User Input for the Elements of the Array
    a = list (map (int, input ("Enter the Elements of the Array:\n").split ()))
    
    # Output
    print (f"The Array after Moving Zeroes to the End:\n{moveZeroes (n, a)}")

if __name__ == "__main__":
    main()

# Sample Input / Output

"""
Input:

Enter the Size of the Array:
n = 10  

Enter the Elements of the Array:
a = 1 0 2 0 4 0 3 0 0 5

Output:

The Array after Moving Zeroes to the End:
[1, 2, 4, 3, 5, 0, 0, 0, 0, 0]
"""

# Links

"""
Access the Problem:-
    Take U Forward (TUF): https://takeuforward.org/plus/dsa/problems/move-zeros-to-end
    Leetcode (Question No. 283): https://leetcode.com/problems/move-zeroes/description/
    Geeks For Geeks (GFG): https://www.geeksforgeeks.org/problems/move-all-zeroes-to-end-of-array0751/1
    Naukri Code 360 (Coding Ninjas): https://www.naukri.com/code360/problems/interview-shuriken-41-move-zeroes-to-end_240143

Article: https://takeuforward.org/data-structure/move-all-zeros-to-the-end-of-the-array/
"""