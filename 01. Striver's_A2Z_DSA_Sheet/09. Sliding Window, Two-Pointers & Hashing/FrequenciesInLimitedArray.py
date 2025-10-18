# Frequencies in a Limited Array

"""
Problem Statement:-

    Frequencies in a Limited Array
    
    You are given an array arr[] containing positive integers. 
    The elements in the array arr[] range from  1 to n (where n is the size of the array), and some numbers may be repeated or absent. 
    You have to count the frequency of all numbers in the range 1 to n and 
        return an array of size n such that result[i] represents the frequency of the number i (1-based indexing).

Examples:-

    Example 1:
    
        Input: 
            arr[] = [2, 3, 2, 3, 5]
        Output: 
            [0, 2, 2, 0, 1]
        Explanation: 
            We have: 
                1 occurring 0 times, 
                2 occurring 2 times, 
                3 occurring 2 times, 
                4 occurring 0 times, and 
                5 occurring 1 time.
    
    Example 2:
    
        Input: 
            arr[] = [3, 3, 3, 3]
        Output: 
            [0, 0, 4, 0]
        Explanation: 
            We have: 
                1 occurring 0 times, 
                2 occurring 0 times, 
                3 occurring 4 times, and 
                4 occurring 0 times.
    
    Example 3:
    
        Input: 
            arr[] = [1]
        Output: 
            [1]
        Explanation: 
            We have: 
                1 occurring 1 time, and there are no other numbers between 1 and the size of the array.
"""

# Function to check frequency of elements in an array (1-based indexing)
def frequencyCount (arr):
    
    # Handle Edge Case, in case of empty array
    if not arr:
        return []
    
    # Declare and initialize the resultant array (list) with 0s
    resultant_frequency_list = [0] * (len(arr))
    
    # Iterate over each element in the array
    for i in arr:
        if 1 <= i <= (len(arr)):
            resultant_frequency_list[i - 1] += 1
    
    # Return the result
    return resultant_frequency_list

# Main Function
def main():
    
    # Take User Input
    arr = list(map(int, input("Enter the elements of the array: ").split()))
    
    # Output
    frequencyCount(arr)
    print ("The Resultant Frequencies of Each Element is:")
    print (frequencyCount(arr))

if __name__ == "__main__":
    main()

# Sample Input / Output

"""
Input:

Enter the elements of the array: 2 3 2 3 5

Output:

The Resultant Frequencies of Each Element is:
[0, 2, 2, 0, 1]
"""

# Link

"""
Access the Problem:-
    Geeks For Geeks (GFG): https://www.geeksforgeeks.org/problems/frequency-of-array-elements-1587115620/1
"""