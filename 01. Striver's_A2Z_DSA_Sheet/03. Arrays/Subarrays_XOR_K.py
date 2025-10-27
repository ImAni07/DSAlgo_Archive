# Count the Number of Subarrays with given XOR K

"""
Problem Statement:-

    Given an array of integers a and an integer k, 
        return the total number of subarrays whose XOR equals to k.

Examples:-

    Example 1:
    
        Input: 
            a = [4, 2, 2, 6, 4], 
            k = 6
        Output: 
            4
        Explanation: 
            The subarrays having XOR of their elements as 6 are 
                [4, 2], 
                [4, 2, 2, 6, 4], 
                [2, 2, 6], and 
                [6]

    Example 2:
    
        Input:
            a = [5, 6, 7, 8, 9], k = 5
        Output: 
            2
        Explanation: 
            The subarrays having XOR of their elements as 5 are 
                [5] and 
                [5, 6, 7, 8, 9]
"""

# Import Requirements
from collections import defaultdict

# Function to calculate the number subarrays with given xor k
def subarraysWithSumK (a, k):
    
    # Declare required variables
    x = 0
    hashmap = defaultdict(int)
    hashmap[x] = 1
    count = 0
    
    # Traverse through the array
    for i in range (len (a)):
        
        # Prefix xor till index i
        x = x ^ a[i]
        
        # Check if (x ^ k) exists in the hashmap
        if (x ^ k) in hashmap:
            count += hashmap[x ^ k]

        # Store the current prefix XOR in the hashmap
        hashmap[x] += 1
    
    # Return the count
    return count

# Main Function
def main():
    
    # Take User Input for the Size of the Array
    n = int (input("Enter the Size of the Array:\n"))
    
    # Take User Input for the Elements of the Array
    a = list (map (int, input("Enter the Elements of the Array:\n").split()))
    
    # Take User Input for the given integer
    k = int (input("Enter the Value of the Target Integer:\n"))
    
    # Output
    print (f"Number of Subarrays whose XOR equals to {k} is:\n{subarraysWithSumK (a, k)}")

if __name__ == "__main__":
    main()

# Sample Input / Output

"""
Input:

Enter the Size of the Array:
n = 4

Enter the Elements of the Array:
a = 1 2 3 2

Enter the Value of the Target Integer:
k = 2

Output:

Number of Subarrays whose XOR equals to 2 is:
3
"""

# Link

"""
Access the Problem:-
    Take U Forward (TUF):
    Geeks For Geeks (GFG):
    Naukri Code 360 (Coding Ninjas):

Article:
"""