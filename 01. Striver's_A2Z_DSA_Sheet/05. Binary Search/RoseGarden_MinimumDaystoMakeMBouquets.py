# Rose Garden
# Minimum Number of Days to Make M Bouquets

"""
Problem Solving:-

    You are given an integer array bloomDay, an integer m and an integer k.
    You want to make m bouquets. 
    To make a bouquet, you need to use k adjacent flowers from the garden.
    The garden consists of n flowers, the ith flower will bloom in the bloomDay[i] and then can be used in exactly one bouquet.
    Return the minimum number of days you need to wait to be able to make m bouquets from the garden. 
    If it is impossible to make m bouquets return -1.

Examples:-

    Example 1:
    
        Input: 
            bloomDay = [1,10,3,10,2], 
            m = 3, 
            k = 1
        Output: 
            3
        Explanation: 
            Let us see what happened in the first three days. 
                x means flower bloomed and _ means flower did not bloom in the garden.
                We need 3 bouquets each should contain 1 flower.
                    After day 1: [x, _, _, _, _]   // we can only make one bouquet.
                    After day 2: [x, _, _, _, x]   // we can only make two bouquets.
                    After day 3: [x, _, x, _, x]   // we can make 3 bouquets. The answer is 3.
    
    Example 2:
    
        Input:
            bloomDay = [1,10,3,10,2], 
            m = 3, 
            k = 2
        Output: 
            -1
        Explanation: 
            We need 3 bouquets each has 2 flowers, that means we need 6 flowers. 
            We only have 5 flowers so it is impossible to get the needed bouquets and we return -1.
    
    Example 3:
    
        Input: 
            bloomDay = [7,7,7,7,12,7,7], 
            m = 2, 
            k = 3
        Output: 
            12
        Explanation: 
            We need 2 bouquets each should have 3 flowers.
                Here is the garden after the 7 and 12 days:
                    After day 7: [x, x, x, x, _, x, x]
                        We can make one bouquet of the first three flowers that bloomed. 
                        We cannot make another bouquet from the last three flowers that bloomed because they are not adjacent.
                    After day 12: [x, x, x, x, x, x, x]
                It is obvious that we can make two bouquets in different ways.
"""

# Function to check whether it is possible 
# to make the required number of bouquets with the given number of roses and days
def possible (bloomDay, days, m, k):
    
    # Initialize the count of flowers
    flowers = 0
    
    # Initialize the count of bouquets
    bouquets = 0
    
    # Length of the bloomDay array
    n = len (bloomDay)
    
    # Iterate through the bloomDay array
    for i in range (n):
        
        # If the bloomDay of the current flower is less than or equal to the given number of days
        if bloomDay [i] <= days:
            
            # Increment the count of flowers
            flowers += 1
            
        else:
            
            # If the bloomDay of the current flower is greater than the given number of days, 
            # reset the count of flowers and calculate the number of bouquets made
            bouquets += flowers // k
            flowers = 0
    
    # Calculate the number of bouquets made with the remaining flowers
    bouquets += flowers // k
    
    # Return the number of bouquets made
    return bouquets >= m

# Function to find the minimum number of days required to make the required number of bouquets
def minDays (bloomDay, m, k):
    
    # Length of the bloomDay array
    n = len (bloomDay)
    
    # If the number of bouquets required is greater than the total number of flowers
    if m * k > n:
        return -1
    
    # Initialize the low and high pointers
    lo = min (bloomDay)
    hi = max (bloomDay)
    
    # Apply Binary Search
    while lo <= hi:
        
        # Update the mid value
        mid = (lo + hi) // 2
        
        # Check if it is possible to make the required number of bouquets with the current number of days
        if possible (bloomDay, mid, m, k):
            
            # If yes, then try for a smaller number of days
            hi = mid - 1
        
        else:
            
            # If no, then try for a larger number of days
            lo = mid + 1
    
    # Return the minimum number of days required to make the required number of bouquets
    return lo

# Main Function
def main ():
    
    # Take User Input for the Number of Roses
    n = int (input ("Enter the Number of Roses:\n"))
    
    # Take User Input for the Elements of the Bloom Day Array
    bloomDay = list (map (int, input ("Enter the BloomDays of the Roses:\n").split ()))
    
    # Take User Input for the Number of Bouquets Required
    m = int (input ("Enter the Number of Bouquets Required:\n"))
    
    # Take User Input for the Number of Flowers in Each Bouquet
    k = int (input ("Enter the Number of Flowers in each Bouquet:\n"))
    
    # Print the minimum number of days required to make the required number of bouquets
    print (f"The Minimum Number of Days Required to make {m} Bouquets with {k} Flowers in each of them:\n{minDays (bloomDay, m, k)}")

if __name__ == "__main__":
    main ()

# Sample Input / Output

"""
Input:

Enter the Number of Roses:
n = 8

Enter the BloomDays of the Roses:
bloomDay = 7 7 7 7 13 11 12 7

Enter the Number of Bouquets Required:
m = 2

Enter the Number of Flowers in each Bouquet:
k = 3

Output:

The Minimum Number of Days Required to make 2 Bouquets with 3 Flowers in each of them:
12
"""

# Link

"""
Access the Problem:-
    Take U Forward (TUF): https://takeuforward.org/plus/dsa/problems/minimum-days-to-make-m-bouquets
    Leetcode (Question No. 1482): https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/description/
    Geeks For Geeks (GFG): https://www.geeksforgeeks.org/problems/minimum-days-to-make-m-bouquets/1
    Naukri Code 360 (Coding Ninjas): https://www.naukri.com/code360/problems/rose-garden_2248080

Article: https://takeuforward.org/arrays/minimum-days-to-make-m-bouquets/
"""