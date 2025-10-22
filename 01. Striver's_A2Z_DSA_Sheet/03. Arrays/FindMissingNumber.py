# Find the Missing Number from the given Array

"""
Problem Statement:-

    Given an integer array of size n containing distinct values in the range from 0 to n (inclusive), 
    return the only number missing from the array within this range.

Examples:-

    Example 1:
    
        Input: 
            a = [0, 2, 3, 1, 4]
        Output: 
            5
        Explanation:
            a contains 0, 1, 2, 3, 4 thus leaving 5 as the only missing number in the range [0, 5]
    
    Example 2:
    
        Input: 
            a = [0, 1, 2, 4, 5, 6]
        Output: 
            3
        Explanation:
            a contains 0, 1, 2, 4, 5, 6 thus leaving 3 as the only missing number in the range [0, 6]
"""

# Function to find the Missing Number from the given Array
def missingNumber (a, n):
    
    # Declare the required variables
    actual_sum = 0
    expected_sum = ((n * (n + 1)) // 2)
    
    # Traverse through the loop and update the sum of the array
    for i in range(n):
        actual_sum += a[i]
    
    # Find the difference between the sum of n natural numbers (expected_sum) 
    # and sum of the elements of the given array (actual_sum) and return it
    return (expected_sum - actual_sum)

# Main Function
def main():
    
    # Take User Input for the Size of the Array
    n = int (input ("Enter the Size of the Array:\n"))
    
    # Take User Input for the Elements of the Array
    a = list(map(int, input("Enter the Elements of the Array:\n").split()))
    
    # Output
    print(f"The Missing Number in the given Array is:\n{missingNumber(a, n)}")

if __name__ == "__main__":
    main ()

# Sample Input / Output

"""
Input:

Enter the Size of the Array:
n = 5

Enter the Elements of the Array:
a = 1 2 4 5

Output:

The Missing Number in the given Array is:
3
"""

# Links

"""
Access the Problem:-
    Take U Forward (TUF): https://takeuforward.org/plus/dsa/problems/find-missing-number
    Naukri Code 360 (Coding Ninjas): https://www.naukri.com/code360/problems/missing-number_6680467

Article: https://takeuforward.org/arrays/find-the-missing-number-in-an-array/
"""