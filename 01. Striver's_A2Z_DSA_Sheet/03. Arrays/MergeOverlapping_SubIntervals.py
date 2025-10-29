# Merge Overlapping Sub Intervals

"""
Problem Statement:-

    Given an array of intervals where,
        intervals[i] = [start(i), end(i)], 
    merge all overlapping intervals and 
        return an array of the non-overlapping intervals that cover all the intervals in the input.
    You can return the intervals in any order.

Examples:-

    Example 1:
    
        Input:
            intervals = [[1,5],[3,6],[8,10],[15,18]]
        Output: 
            [[1,6],[8,10],[15,18]]
        Explanation: 
            Intervals [1,5] and [3,6] overlap, so they are merged into [1,6].
    
    Example 2:
    
        Input:
            intervals = [[5,7],[1,3],[4,6],[8,10]]
        Output:
            [[1,3],[4,7],[8,10]]
        Explanation: 
            Intervals [4,6] and [5,7] overlap and are merged into [4,7].
"""

# Function to Merge All the Overlapping Intervals
def mergeOverlappingIntervals (intervals):
    
    # Declare an empty list to store the overlapped intervals
    answer = []
    
    # Step 1 --> Sort the given array
    intervals.sort ()
    
    # Step 2 --> Traverse the array
    for i in range (len (intervals)):
        
        # Case 1 --> If the current interval does not lie in the last interval or no interval exists
        if not answer or intervals [i][0] > answer [-1][1]:
            answer.append(intervals[i])
        
        # Case 2 --> If the current interval lies in the last interval
        else:
            answer [-1][1] = max (answer[-1][1], intervals[i][1])
    
    # Return the resultant
    return answer

# Main Function
def main():
    
    # Take User Input for the Size of the Interval List
    n = int (input ("Enter the Size:\n"))
    
    # Take User Input for the Interval List
    intervals = []
    print("Enter the Range:\n")
    for i in range (n):
        start, end = map (int, input ().split())
        intervals.append([start, end])
    
    # Output
    print (f"The Merged Sub Intervals are:\n{mergeOverlappingIntervals (intervals)}")

if __name__ == "__main__":
    main()

# Sample Input / Output

"""
Input:

n = 4

Enter the Range:
start, end = 1, 3
start, end = 2, 4
start, end = 6, 8
start, end = 9, 10

intervals = [[1, 3], [2, 4], [6, 8], [9, 10]]

Output:

The Merged Sub Intervals are:
[[1, 4], [6, 8], [9, 10]]
"""

# Link

"""
Access the Problem:-
    Take U Forward (TUF): https://takeuforward.org/plus/dsa/problems/merge-overlapping-subintervals
    Leetcode (Question No. 56): https://leetcode.com/problems/merge-intervals/description/
    Geeks For Geeks (GFG): https://www.geeksforgeeks.org/problems/overlapping-intervals--170633/1
    Naukri Code 360 (Coding Ninjas): https://www.naukri.com/code360/problems/merge-all-overlapping-intervals_6783452

Article: https://takeuforward.org/data-structure/merge-overlapping-sub-intervals/
"""