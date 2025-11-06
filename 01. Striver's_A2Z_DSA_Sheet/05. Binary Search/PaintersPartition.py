# Painter's Partition

"""
Problem Statement:-

    Given an array/list of length N, where the array/list represents the boards.
    Each element of the given array/list represents the length of each board. 
    Some K numbers of painters are available to paint these boards. 
    Consider that each unit of a board takes 1 unit of time to paint. 
    You are supposed to return the area of the minimum time to get this job done of painting all the N boards 
        under the constraint that any painter will only paint the continuous sections of boards.

Examples:-

    Input: 
        N = 4, 
        boards[] = {5, 5, 5, 5}, 
        k = 2
    Output: 
        10
    Explanation: 
        We can divide the boards into 2 equal-sized partitions, 
            so each painter gets 10 units of the board and the total time taken is 10.

    Example 2:
    
        Input: 
            N = 4, 
            boards[] = {10, 20, 30, 40},
            k = 2
        Output: 
            60
        Explanation: 
            We can divide the first 3 boards for one painter and the last board for the second painter.
"""

# Function to count the number of painters required to paint the boards with the given maximum time
def countPainters (boards, time):
    
    # Size of the boards
    n = len (boards)
    
    # Initialize the count of painters required
    painter_count = 1
    
    # Initialize the total time variable to keep track of the total time taken
    total_time = 0
    
    # Iterate through the boards
    for i in range (n):
        
        # Calculate the total time taken to paint the current board, 
        # given that it does not exceed the maximum time
        if total_time + boards[i] <= time:
            # Allocate the board to the current painter
            total_time += boards[i]
        
        else:
            # If the total time exceeds the maximum time, allocate the board to a new painter
            painter_count += 1
            total_time = boards[i]
    
    # Return the number of painters required
    return painter_count

# Function to find the minimum distance allowed to paint all the boards
def findLargestMinDistance (boards, k):
    
    # Initialize the low and high pointers
    lo = max (boards)
    hi = sum (boards)
    
    # Apply Binary Search
    while lo <= hi:
        
        # Update mid
        mid = (lo + hi) // 2
        
        # Check the number of painters required to paint the boards with the current maximum distance
        
        # If it is less than or equal to k
        if countPainters(boards, mid) <= k:
            # If yes, then try for a smaller maximum distance
            hi = mid - 1
        
        else:
            # If no, then try for a larger maximum distance
            lo = mid + 1
    
    # Return the minimum distance allowed to paint all the boards
    return lo

# Main Function
def main ():
    
    # Take User Input for the Size of the Boards
    n = int (input ("Enter the Number of Boards:\n"))
    
    # Take User Input for the Elements of the Boards
    boards = list (map (int, input ("Enter the Lengths of the Boards:\n").split ()))
    
    # Take User Input for the Number of Painters
    k = int (input ("Enter the Number of Painters:\n"))
    
    # Print the minimum distance required to paint all the boards
    print (f"The Required Output is: {findLargestMinDistance (boards, k)}")

if __name__ == "__main__":
    main ()

# Sample Input / Output

"""
Input:

Enter the Number of Boards:
n = 5

Enter the Lengths of the Boards:
boards = 5 10 30 20 15

Enter the Number of Painters:
k = 3

Output:

The Required Output is: 35
"""

# Link

"""
Access the Problem:-
    Take U Forward (TUF): https://takeuforward.org/plus/dsa/problems/painters-partition
    Geeks For Geeks (GFG): https://www.geeksforgeeks.org/problems/the-painters-partition-problem1535/1
    Naukri Code 360 (Coding Ninjas): https://www.naukri.com/code360/problems/painter-s-partition-problem_1089557

Article: https://takeuforward.org/arrays/painters-partition-problem/
"""