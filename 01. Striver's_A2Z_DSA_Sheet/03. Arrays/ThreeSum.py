# 3 Sum

"""
Problem Statement:-

    Given an integer array arr. 
    Return all triplets such that:
        i!= j, i!= k, and j!= k
        arr[i] + arr[j] + arr[k] == 0.
    Notice that the solution set must not contain duplicate triplets. 
    One element can be a part of multiple triplets. 
    The output and the triplets can be returned in any order.

Examples:-

    Example 1:
    
        Input: 
            arr = [2, -2, 0, 3, -3, 5]
        Output: 
            [[-2, 0, 2], [-3, -2, 5], [-3, 0, 3]]
        Explanation:
            arr[1] + arr[2] + arr[0] = 0
            arr[4] + arr[1] + arr[5] = 0
            arr[4] + arr[2] + arr[3] = 0
    
    Example 2:
    
        Input: 
            arr = [2, -1, -1, 3, -1]
        Output: 
            [[-1, -1, 2]]
        Explanation:
            arr[1] + arr[2] + arr[0] = 0
            Note that we have used two -1s as they are separate elements with different indexes
            But we have not used the -1 at index 4 as that would create a duplicate triplet
"""

# Function to find all the required triplet that would give the target
def triplet (arr, n):
    
    # Declare an empty list that would consist of all the required triplets
    triplets = []
    
    # Sort the Array
    arr.sort()
    
    # Traverse through the array
    for i in range (n):
        
        # Skip the Duplicates
        if i > 0 and arr[i] == arr[i - 1]:
            continue
        
        # Declare 2 pointers
        j = i + 1
        k = n - 1
        
        # Iterate through the array with these 2 pointers, until the conditions do not meet
        while j < k:
            sum = arr[i] + arr[j] + arr[k]
            
            # Check whether the present sum is equal to 0 or not
            
            # If it is less:
            if sum < 0:
                j += 1
            
            # If it is more:
            elif sum > 0:
                k -= 1
            
            # If it is equal to 0
            else:
                
                # Add the triplet to the list
                temp = [arr[i], arr[j], arr[k]]
                triplets.append(temp)
                j += 1
                k -= 1
                
                # Skip the duplicates for j pointer
                while j < k and arr[j] == arr[j - 1]:
                    j += 1
                
                # Skip the duplicates for k pointer
                while j < k and arr[k] == arr[k + 1]:
                    k -= 1
    
    # Return the result
    return triplets

# Main Function
def main():
    
    # Take User Input for the Size of the Array
    n = int (input("Enter the Size of the Array:\n"))
    
    # Take User Input for the Elements of the Array
    arr = list(map(int, input("Enter the Elements of the Array:\n").split()))
    
    # Output
    print(f"Required Triplet:\n{triplet(arr,n)}")

if __name__ == "__main__":
    main()

# Sample Input / Output

"""
Input:

Enter the Size of the Array:
n = 6

Enter the Elements of the Array:
arr = -1 0 1 2 -1 -4

Output:

Required Triplet:
[[-1,-1,2],[-1,0,1]]
"""

# Link

"""
Access the Problem:
    Take U Forward (TUF): https://takeuforward.org/plus/dsa/problems/3-sum
    Leetcode (Question No. 15): https://leetcode.com/problems/3sum/description/
    Geeks For Geeks (GFG): https://www.geeksforgeeks.org/problems/three-sum/1
    Naukri Code 360 (Coding Ninjas): https://www.naukri.com/code360/problems/triplets-with-given-sum_893028

Article: https://takeuforward.org/data-structure/3-sum-find-triplets-that-add-up-to-a-zero/
"""