# Count Frequency in a Range

"""
Problem Statement:-

    Count Frequency in a range
    
    You are given an array 'arr' of length 'n' containing integers within the range '1' to 'x'.
    Your task is to count the frequency of all elements from 1 to n.
    
    Note:
        You do not need to print anything. 
        Return a frequency array as an array in the function such that 
            index 0 represents the frequency of 1, index 1 represents the frequency of 2, and so on.

Example:
    Input: 
        n = 6 
        x = 9 
        arr = [1, 3, 1, 9, 2, 7]    
    Output: 
        [2, 1, 1, 0, 0, 0]
    Explanation:
        Below Table shows the number and their counts, respectively, in the array
        Number         Count 
        1                2
        2                1
        3                1
        4                0
        5                0
        6                0
"""

# Function of counting frequency of elements in a given range within the given array
def countFrequency (n, x, arr):
    
    # Handle Edge Case, in case of empty array
    if not arr:
        return []
    
    # Filter the array by removing the elements that are greater than the size of the array
    arr = [i for i in arr if i <= n]
    
    # Declare and initialize the resultant array (list) with 0s
    frequency_array = [0] * (n)
    
    # Iterate over each element in the array
    for i in arr:
        if 1 <= i <= n:
            frequency_array[i - 1] += 1
    
    # Return the result
    return frequency_array

# Main Function
def main():
    
    # Take User Input
    
    # Size of the Array
    n = int(input("Enter the size of the array: "))
    x = int(input("Enter the Maximum Value: "))
    arr = list(map(int, input("Enter the elements of the array: ").split()))
    
    # Check if all elements are less than or equal to x
    if all(1 <= num <= x for num in arr):
        
        # Output
        countFrequency(n,x,arr)
        print ("The Resultant Frequencies of Each Element is:")
        print (countFrequency(n, x, arr))
    
    else:
        print("All elements must be in the range of", 1, "to", x)

if __name__ == "__main__":
    main()

# Sample Input / Output

"""
Input:

Enter the size of the array: 
n = 6
Enter the Maximum Value: 
x = 4
Enter the elements of the array: 
arr = [1 3 4 3 4 1]

Output:

The Resultant Frequencies of Each Element is:
[2, 0, 2, 2, 0, 0]
"""

# Link

"""
Access the Problem:-
    Naukri Code 360 (Coding Ninjas): https://www.naukri.com/code360/problems/count-frequency-in-a-range_8365446
"""