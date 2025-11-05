# Capacity To Ship Packages Within D Days

"""
Problem Statement:-

    You are given an array weights where weights[i] represents the weight of the i-th package on a conveyor belt. 
    All the packages must be shipped in the order given from one port to another within days days.
    Each day, the ship can carry a contiguous sequence of packages, 
        as long as the total weight does not exceed its maximum capacity.
    Your task is to find the minimum possible capacity of the ship so that 
        all packages can be shipped within the given number of days.

Examples:-

    Example 1:
    
        Input: 
            weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 
            days = 5
        Output: 
            15
        Explanation:
            Minimum ship capacity = 15. One way to ship in 5 days:
                Day 1: 1 + 2 + 3 + 4 + 5 = 15
                Day 2: 6 + 7 = 13
                Day 3: 8
                Day 4: 9
                Day 5: 10
            No day exceeds capacity 15 and all packages are shipped in order in 5 days.
    
    Example 2:
    
        Input: 
            weights = [3, 2, 2, 4, 1, 4], 
            days = 3
        Output: 
            6
        Explanation:
            One possible division with capacity 6:
                Day 1: 3 + 2 = 5
                Day 2: 2 + 4 = 6
                Day 3: 1 + 4 = 5
            All packages shipped in order within 3 days.
"""

# Function to count the number of days required to ship the packages with the given weight limit
def countDays (weights, capacity_limit):
    
    # Initialize the count of days required
    days_count = 1
    
    # Initialize the total weight variable to keep track of the total weight of the current day
    load = 0
    
    # Length of the weights array
    n = len (weights)
    
    # Iterate through the weights array
    for i in range (n):
        
        # Calculate the total weight of the current day, 
        # given that it does not exceed the capacity limit
        if load + weights[i] <= capacity_limit:
            load += weights[i]
        
        else:
            # If the total weight exceeds the capacity limit, create a new day
            days_count += 1
            load = weights[i]
    
    # Return the number of days required to ship all the packages
    return days_count

# Function to find the minimum capacity required to ship all the packages within D days
def shipWithinDays (weights, d):
    
    # Initialize the lower and upper bounds for binary search
    lo = max (weights)
    hi = sum (weights)
    
    # Perform binary search to find the minimum capacity required
    while lo <= hi:
        
        # Calculate the mid-point of the current search range
        mid = (lo + hi) // 2
        
        # Compare the number of days required to ship all packages with the current capacity
        if countDays(weights, mid) <= d:
            
            # If yes, then try for a smaller capacity, eliminate the right half
            hi = mid - 1
        
        else:
            # If no, then try for a larger capacity, eliminate the left half
            lo = mid + 1
    
    # Return the minimum capacity required to ship all packages within D days
    return lo

# Main Function
def main ():
    
    # Take User Input for the Size of the Weights Array
    n = int (input ("Enter the Size of the Array:\n"))
    
    # Take User Input for the Elements of the Weights Array
    weights = list (map (int, input ("Enter the Weights:\n").split ()))
    
    # Take User Input for the Number of Days
    d = int (input ("Enter the Number of Days:\n"))
    
    # Print the minimum capacity required to ship all packages within D days
    print (f"The Minimum Capacity Required to Ship all the Packages within {d} Days is:\n{shipWithinDays (weights, d)}")

if __name__ == "__main__":
    main ()

# Sample Input / Output

"""
Input:

Enter the Size of the Array:
n = 8

Enter the Weights:
weights = 5 4 5 2 3 4 5 6

Enter the Number of Days:
d = 5

Output:

The Minimum Capacity Required to Ship all the Packages within 5 Days is:
9
"""

# Link

"""
Access the Problem:-
    Take U Forward (TUF): https://takeuforward.org/plus/dsa/problems/capacity-to-ship-packages-within-d-days
    Leetcode (Question No. 1011): https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/description/
    Geeks For Geeks (GFG): https://www.geeksforgeeks.org/problems/capacity-to-ship-packages-within-d-days/1
    Naukri Code 360 (Coding Ninjas): https://www.naukri.com/code360/problems/capacity-to-ship-packages-within-d-days_1229379

Article: https://takeuforward.org/arrays/capacity-to-ship-packages-within-d-days/
"""