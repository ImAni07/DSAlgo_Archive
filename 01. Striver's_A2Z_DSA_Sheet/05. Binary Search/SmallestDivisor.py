# Smallest Divisor
# Find the smallest divisor given threshold

"""
Problem Statement:-

    Find the smallest divisor
    
    Given an array of integers nums and an integer limit as the threshold value, 
        find the smallest positive integer divisor such that upon dividing all the elements of the array by this divisor, 
        the sum of the division results is less than or equal to the threshold value.
    After dividing each element by the chosen divisor, take the ceiling of the result (i.e., round up to the next whole number).

Examples:-

    Example 1:
    
        Input: 
            nums = [1, 2, 3, 4, 5], 
            limit = 8
        Output: 
            3
        Explanation: 
            We can get a sum of 15(1 + 2 + 3 + 4 + 5) if we choose 1 as a divisor. 
            The sum is 9(1 + 1 + 2 + 2 + 3) if we choose 2 as a divisor. 
            Upon dividing all the elements of the array by 3, we get 1,1,1,2,2 respectively. 
                Now, their sum is equal to 7 <= 8 i.e. the threshold value. 
                So, 3 is the minimum possible answer.
    
    Example 2:
    
        Input: 
            nums = [8,4,2,3], 
            limit = 10
        Output: 
            2
        Explanation: 
            If we choose 1, we get 17 as the sum. 
            If we choose 2, we get 9 (4+2+1+2) <= 10 as the answer. 
            So, 2 is the answer.
"""

# Import requirement
import math

# Function to find the sum of the elements divided by the numbers
def sumArr (nums, div):
    
    # Size of the array
    n = len (nums)
    
    # Required summation
    total_sum = 0
    
    # Traverse through the array and calculate the total sum
    for i in range (n):
        total_sum += math.ceil(nums[i]/div)
    
    # Return the obtained sum
    return total_sum

# Function to find the smallest divisor within the given threshold
def smallestDivisor (nums, limit):
    
    # Size of the array
    n = len (nums)
    
    # Check whether the length of the array is greater than the given threshold, 
    # if yes then return -1
    if n > limit:
        return -1
    
    # Declare and initialize the low and the high pointer
    lo = 1
    hi = max (nums)
    
    # Apply Binary Search
    while lo <= hi:
        
        # Update the mid value
        mid = (lo + hi) // 2
        
        # Check whether the sum is less than equal to the given threshold
        if sumArr (nums, mid) <= limit:
            hi = mid - 1
        
        else:
            lo = mid + 1
    
    return lo

# Main Function
def main ():
    
    # Take User Input for the Size of the Array
    n = int (input ("Enter the Size of the Array:\n"))
    
    # Take User Input for the Elements of the Array
    nums = list (map (int, input ("Enter the Elements of the Array:\n").split ()))
    
    # Take User Input for the Limit
    limit = int (input ("Enter the Threshold or Limit:\n"))
    
    # Print the Result
    print (f"The Smallest Divisor within the given threshold of {limit} is {smallestDivisor (nums, limit)}")
    
if __name__ == "__main__":
    main ()

# Sample Input / Output

"""
Input:

Enter the Size of the Array:
n = 4

Enter the Elements of the Array:
nums = 1 2 5 9

Enter the Threshold or Limit:
limit = 6

Output:

The Smallest Divisor within the given threshold of 6 is 5
"""

# Link

"""
Access the Problem:-
    Take U Forward (TUF): https://takeuforward.org/plus/dsa/problems/find-the-smallest-divisor
    Leetcode (Question No. 1283): https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/description/
    Geeks For Geeks (GFG): https://www.geeksforgeeks.org/problems/smallest-divisor/1
    Naukri Code 360 (Coding Ninjas): https://www.naukri.com/code360/problems/smallest-divisor-with-the-given-limit_1755882

Article: https://takeuforward.org/arrays/find-the-smallest-divisor-given-a-threshold/
"""