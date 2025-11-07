# Minimize Max Distance to Gas Station

"""
Problem Statement:-

    Minimize Max Distance to Gas Station
    
    Given a sorted array arr of size n, containing integer positions of n gas stations on the X-axis, and 
        an integer k, place k new gas stations on the X-axis.
    The new gas stations can be placed anywhere on the non-negative side of the X-axis, including non-integer positions.
    Let dist be the maximum distance between adjacent gas stations after adding the k new gas stations.
    Find the minimum value of dist.

Examples:-

    Example 1:
    
        Input: 
            n = 10, 
            arr = [1, 2, 3, 4, 5, 6 ,7, 8, 9, 10], 
            k = 9
        Output: 
            0.50000
        Explanation:
            One of the possible ways to place 10 gas stations is --
                [1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10].
            Thus the maximum difference between adjacent gas stations is 0.5.
            Hence, the value of dist is 0.5.
            It can be shown that there is no possible way to add 10 gas stations in such a way that the value of dist is lower than this.
    
    Example 2:
    
        Input: 
            n = 10, 
            arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 
            k = 1
        Output: 
            1.00000
        Explanation:
            One of the possible ways to place 1 gas station is --
                [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11].
            New Gas Station is at 11.
            Thus the maximum difference between adjacent gas stations is still 1.
            Hence, the value of dist is 1.
            It can be shown that there is no possible way to add 1 gas station in such a way that the value of dist is lower than this. 
"""

# Function to find the number of gas stations
def numberOfGasStationsRequired(dist, arr):
    
    # Size of the Array
    n = len(arr)
    
    # Count the number
    cnt = 0
    
    # Iterate
    for i in range(1, n):
        gap = arr[i] - arr[i - 1]
        cnt += int(gap / dist)
    
    # Return the count
    return cnt

# Function to find the minimum possible maximum distance
def minimizeMaxDistance(arr, k):
    
    # Size of the Array
    n = len(arr)
    
    # Pointers
    low = 0
    high = 0

    # Find maximum initial gap:
    for i in range(n - 1):
        high = max(high, arr[i + 1] - arr[i])

    # Apply Binary Search
    diff = 1e-6
    
    while high - low > diff:
        
        # Update the mid value
        mid = (low + high) / 2.0
        
        # Count the number of gas stations required
        cnt = numberOfGasStationsRequired(mid, arr)
        
        # Compare the value of count with k
        if cnt > k:
            low = mid
        else:
            high = mid

    return (low + high) / 2

# Main Function
def main ():
    
    # Take User Input for the Number of Gas Stations
    n = int (input ("Enter the Number of Gas Stations:\n"))
    
    # Take User Input for the Positions of the Gas Stations
    arr = list (map (int, input ("Enter the Position of Gas Stations:\n").split ()))
    
    # Take User Input for the Number of New Gas Stations
    k = int (input ("Enter the Number of New Gas Stations:\n"))
    
    # Output
    print (f"The Minimum Possible Maximum Distance between Gas Stations is: {minimizeMaxDistance(arr, k)}")

if __name__ == "__main__":
    main ()

# Sample Input / Output

"""
Input:

Enter the Number of Gas Stations:
n = 7

Enter the Position of Gas Stations:
arr = 1 2 3 4 5 6 7

Enter the Number of New Gas Stations:
k = 6

Output:

The Minimum Possible Maximum Distance between Gas Stations is: 0.5
"""

# Link

"""
Access the Problem:-
    Take U Forward (TUF): https://takeuforward.org/plus/dsa/problems/minimise-max-distance-to-gas-stations
    Leetcode (Premium): https://leetcode.com/problems/minimize-max-distance-to-gas-station/
    Naukri Code 360 (Coding Ninjas): https://www.naukri.com/code360/problems/minimise-max-distance_7541449

Article: https://takeuforward.org/arrays/minimise-maximum-distance-between-gas-stations/
"""