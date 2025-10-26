# Majority Element - II
# Find the majority element that occurs more n/3 times in the given array

"""
Problem Statement:-

    Majority Element - II
    
    Given an integer array v of size n. 
    Return all elements which appear more than n/3 times in the array. 
    The output can be returned in any order.

Examples:-

    Example 1:
    
        Input: 
            v = [1, 2, 1, 1, 3, 2]
        Output: 
            [1]
        Explanation:
            Here, 
                n / 3 = 6 / 3 = 2.
            Therefore the elements appearing 3 or more times is: 
                [1]
    
    Example 2:
    
        Input: 
            v = [1, 2, 1, 1, 3, 2, 2]
        Output: 
            [1, 2]
        Explanation:
            Here, 
                n / 3 = 7 / 3 = 2.
            Therefore the elements appearing 3 or more times is: 
                [1, 2]
"""

# Function that finds the majority element(s) that occur more than n/3 times in the given array
def majorityElement (v):
    
    # Initialize the counter variables to 0
    count1 = 0
    count2 = 0
    
    # Initialize the element variables to a minimum value
    element1 = float('-inf')
    element2 = float('-inf')
    
    # Declare an empty list to store the required candidate elements
    candidate_elements = []
    
    # Iterate through the array, in order to look for the candidate elements
    for i in range(len(v)):
        
        # Check if the frequency of 1st element is 0 and the ith element is not the 2nd element
        if count1 == 0 and element2 != v[i]:
            
            # Increase the value of counter for the 1st element by 1
            count1 += 1
            
            # Assign the ith element of the array to the variable element1
            element1 = v[i]
        
        # Check if the frequency of 2nd element is 0 and the ith element is not the 1st element
        elif count2 == 0 and element1 != v[i]:
            
            # Increase the value of counter for the 2nd element by 1
            count2 += 1
            
            # Assign the ith element of the array to the variable element2
            element2 = v[i]
        
        # Check if the ith element is equal to the 1st element
        elif v[i] == element1:
            
            # Increase the value of counter for the 1st element by 1
            count1 += 1
        
        # Check if the ith element is equal to the 2nd element
        elif v[i] == element2:
            
            # Increase the value of counter for the 2nd element by 1
            count2 += 1
        
        else:
            # If the ith element is neither equal to the 1st element nor the 2nd element
            # Decrease the value of counters for both 1st element and 2nd element by 1
            count1 -= 1
            count2 -= 1
    
    # Manual Verification
    
    # Set the counter elements to 0
    count1 = 0
    count2 = 0
    
    # Traverse the array and count their frequencies
    for i in range(len(v)):
        
        # If the present element is equal to the 1st element
        if v[i] == element1:
            count1 += 1
        
        # If the present element is equal to the 2nd element
        if v[i] == element2:
            count2 += 1
    
    # Set the minimum threshold frequency
    threshold_frequency = int (len(v)/3)
    
    # Check whether the frequency of the 1st element is greater than the minimum threshold frequency
    if count1 > threshold_frequency:
        candidate_elements.append(element1)
    
    # Check whether the frequency of the 2nd element is greater than the minimum threshold frequency
    if count2 > threshold_frequency:
        candidate_elements.append(element2)
    
    # Sort the list of the candidate elements
    candidate_elements.sort()
    
    # Return the resultant list
    return candidate_elements

# Main Function
def main():
    
    # Take User Input for the Size of the Array
    n = int (input ("Enter the Size of the Array:\n"))
    
    # Take User Input for the Elements of the Array
    v = list (map (int, input ("Enter the Elements of the Array:\n").split ()))
    
    # Process the Output
    ans = majorityElement (v)
    
    # Print the Output
    print("The Majority Elements are:")
    for it in ans:
        print(it, end=" ")
    print()

if __name__ == "__main__":
    main()

# Sample Input / Output

"""
Input:

Enter the Size of the Array:
n = 8

Enter the Elements of the Array:
v = 11 33 33 22 11 33 11 22

Output:

The Majority Elements are:
11 33
"""

# Link

"""
Access the Problem:-
    Take U Forward (TUF): https://takeuforward.org/plus/dsa/problems/majority-element-ii
    Leetcode (Question No. 229): https://leetcode.com/problems/majority-element-ii/description/
    Geeks For Geeks (GFG): https://www.geeksforgeeks.org/problems/majority-vote/1
    Naukri Code 360 (Coding Ninjas): https://www.naukri.com/code360/problems/majority-element-ii_893027

Article: https://takeuforward.org/data-structure/majority-elementsn-3-times-find-the-elements-that-appears-more-than-n-3-times-in-the-array/
"""