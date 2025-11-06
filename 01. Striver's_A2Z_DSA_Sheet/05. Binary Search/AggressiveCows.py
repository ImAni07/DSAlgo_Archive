# Aggressive Cows

"""
Problem Statement:-

    Given an array stalls of size n, which denotes the positions of stalls, and 
        an integer k, which denotes the number of aggressive cows.
    Assign stalls to k cows such that the minimum distance between any two cows is the maximum possible. 
    Find the maximum possible minimum distance.

Examples:-

    Example 1:
    
        Input: 
            n = 6, 
            k = 4, 
            stalls = [0, 3, 4, 7, 10, 9]
        Output: 
            3
        Explanation: 
            The maximum possible minimum distance between any two cows will be 3 when 4 cows are placed at positions [0, 3, 7, 10]. 
            Here the distances between cows are 3, 4, and 3 respectively. 
            We cannot make the minimum distance greater than 3 in any ways.
    
    Example 2:
    
        Input: 
            n = 5, 
            k = 2, 
            stalls = [4, 2, 1, 3, 6]
        Output: 
            5
        Explanation: 
            The maximum possible minimum distance between any two cows will be 5 when 2 cows are placed at positions [1, 6]. 
"""

# Function to check whether the given distance is feasible or not
def canWePlace (stalls, dist, cows):
    
    # Length of the stalls
    n = len (stalls)
    
    # Initialize the count of cows placed
    count = 1
    
    # Position of the last placed cow
    last_position = stalls[0]
    
    # Traverse through the stalls
    for i in range (1, n):
        
        # If the distance between the current stall and the last placed cow is greater than or equal to the given distance
        if stalls[i] - last_position >= dist:
            
            # Place the cow at the current stall
            count += 1
            
            # Update the position of the last placed cow
            last_position = stalls[i]
            
            # If all cows are placed, return True
            if count == cows:
                return True
            
    # If not all cows are placed, return False
    return False

# Function to find the maximum distance between the cows
def aggressiveCows (stalls, k):
    
    # Sort the stalls
    stalls.sort()
    
    # Initialize the low and high pointers
    lo = 1
    hi = stalls[-1] - stalls[0]
    
    # Apply Binary Search
    while lo <= hi:
        
        # Update the mid value
        mid = (lo + hi) // 2
        
        # Check if we can place cows with the current distance
        if canWePlace (stalls, mid, k):
            
            # If yes, then try for a larger distance
            lo = mid + 1
            
        else:
            # If no, then try for a smaller distance
            hi = mid - 1
        
    # Return the maximum distance found
    return hi

# Main Function
def main ():
    
    # Take User Input for the Size of the Stalls
    n = int (input ("Enter the Number of Stalls:\n"))
    
    # Take User Input for the Number of Cows
    k = int (input ("Enter the Number of Cows:\n"))
    
    # Take User Input for the Elements of the Stalls
    stalls = list (map (int, input ("Enter the Location / Distance of Stalls:\n").split ()))
    
    # Print the maximum possible minimum distance between the cows
    print (f"The Maximum Possible Minimum Distance between the Cows: {aggressiveCows (stalls, k)}")

if __name__ == "__main__":
    main ()

# Sample Input / Output

"""
Input:

Enter the Number of Stalls:
n = 5

Enter the Number of Cows:
k = 3

Enter the Location / Distance of Stalls:
stalls = 10 1 2 7 5

Output:

The Maximum Possible Minimum Distance between the Cows: 4
"""

# Link

"""
Access the Problem:-
    Take U Forward (TUF): https://takeuforward.org/plus/dsa/problems/aggressive-cows
    Geeks For Geeks (GFG): https://www.geeksforgeeks.org/problems/aggressive-cows/1
    Naukri Code 360 (Coding Ninjas): https://www.naukri.com/code360/problems/aggressive-cows_1082559

Article: https://takeuforward.org/data-structure/aggressive-cows-detailed-solution/
"""