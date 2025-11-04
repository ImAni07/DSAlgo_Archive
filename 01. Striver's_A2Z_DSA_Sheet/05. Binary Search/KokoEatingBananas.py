# Koko Eating Bananas

"""
Problem Statement:-

    A monkey is given n piles of bananas, where the 'ith' pile has piles[i] bananas. 
    An integer h represents the total time in hours to eat all the bananas.
    
    Each hour, the monkey chooses a non-empty pile of bananas and eats k bananas. 
    If the pile contains fewer than k bananas, 
        the monkey eats all the bananas in that pile and does not consume any more bananas in that hour.
    
    Determine the minimum number of bananas the monkey must eat per hour to finish all the bananas within h hours.

Examples:-

    Example 1:
    
        Input: 
            n = 4, 
            piles = [7, 15, 6, 3], 
            h = 8
        Output: 
            5
        Explanation: 
            If Koko eats 5 bananas/hr, 
                he will take 2, 3, 2, and 1 hour to eat the piles accordingly. 
                So, he will take 8 hours to complete all the piles.  
    
    Example 2:
    
        Input: 
            n = 5, 
            piles = [25, 12, 8, 14, 19], 
            h = 5
        Output: 
            25
        Explanation: 
            If Koko eats 25 bananas/hr, 
                he will take 1, 1, 1, 1, and 1 hour to eat the piles accordingly. 
                So, he will take 5 hours to complete all the piles.
"""

# Import requirement

import math

# Function to calculate the total number of hours required to eat all the bananas at a given speed
def totalHours (piles, speed):
    
    # Initialize the total hours to 0
    total_hours = 0
    
    # Size of the piles of bananas
    n = len (piles)
    
    # Traverse through the piles of bananas
    for i in range (n):
        total_hours += math.ceil (piles[i] / speed)
    
    # Return the total hours required to eat all the bananas
    return total_hours

# Function to find the minimum number of bananas that Koko can eat in a given number of hours
def minEatingSpeed (piles, h):
    
    # Initialize the left and right pointers
    lo = 1
    hi = max (piles)
    
    # Perform Binary Search
    while lo <= hi:
        
        # Calculate mid
        mid = (lo + hi) // 2
        
        # Check if the total hours required to eat all the bananas at the current speed is 
        # less than or equal to the given number of hours
        if totalHours (piles, mid) <= h:
            hi = mid - 1
        
        # If the total hours required is more than the given number of hours
        else:
            lo = mid + 1
        
    # Return the minimum speed required to eat all the bananas in the given number of hours
    return lo

# Main Function
def main ():
    
    # Take User Input for the Number of Piles of Bananas
    n = int (input ("Enter the Number of Piles of Bananas:\n"))
    
    # Take User Input for the Size of the Piles of Bananas
    piles = list (map (int, input ("Enter the Size of the Piles of the Bananas:\n").split ()))
    
    # Take User Input for the Number of Hours
    h = int (input ("Enter the Number of Hours:\n"))
    
    # Find the minimum number of bananas that Koko can eat in the given number of hours
    print (f"The Minimum Speed with which Koko can eat all the Bananas in {h} hours:\n{minEatingSpeed (piles, h)}")
    
if __name__ == "__main__":
    main ()

# Sample Input / Output

"""
Input:

Enter the Number of Piles of Bananas:
n = 4

Enter the Size of the Piles of the Bananas:
piles = 3 6 7 11

Enter the Number of Hours:
h = 8

Output:

The Minimum Speed with which Koko can eat all the Bananas in 8 hours:
4
"""

# Link

"""
Access the Problem:-
    Take U Forward (TUF): https://takeuforward.org/plus/dsa/problems/koko-eating-bananas
    Leetcode (Question No. 875): https://leetcode.com/problems/koko-eating-bananas/description/
    Naukri Code 360 (Coding Ninjas): https://www.naukri.com/code360/problems/koko-eating-bananas_10870969

Article: https://takeuforward.org/binary-search/koko-eating-bananas/
"""