# Longest Common Prefix

"""
Problem Statement:-

    Write a function to find the longest common prefix string amongst an array of strings.
    If there is no common prefix, return an empty string "".

Examples:-

    Example 1:
    
        Input: 
            strs = ["flowers" , "flow" , "fly", "flight" ]
        Output: 
            "fl"
        Explanation:
            All strings given in array contains common prefix "fl".
    
    Example 2:
    
        Input: 
            strs = ["dog" , "cat" , "animal", "monkey" ]
        Output: 
            ""
        Explanation:
            There is no common prefix among the given strings in array.
"""

# Function to find longest common prefix in an array of strings
def longestCommonPrefix (strs):
    
    # If the array is empty or the array contains only an empty string
    if not strs:
        return ""
    
    # Find the string with the minimum length in the array
    min_len = min ([len (s) for s in strs])
    
    # Declare two pointers for binary search
    lo = 0
    hi = min_len
    
    # Apply Binary Search
    while lo <= hi:
        
        # Calculate the mid value
        mid = (lo + hi) // 2
        
        # Store the prefix in a variable
        lcp = strs[0][:mid]
        
        # Check if the prefix is common to all strings
        if all (s.startswith (lcp) for s in strs):
            
            # If the prefix is common, update the prefix
            lo = mid + 1
        
        # If not, try for a shorter one
        else:
            hi = mid - 1
    
    # Return the longest common prefix
    return strs[0][:lo - 1]

# Main Function
def main():
    
    # Input the number of strings
    n = int(input("Enter the Number of Strings:\n"))
    
    # Input the strings
    print("Enter the Strings:\n")
    strs = []
    
    for i in range(n):
        s = input()
        strs.append(s)
    
    # Print the result
    print(f"The Longest Common Prefix among the given strings:\n{longestCommonPrefix(strs)}")

if __name__ == '__main__':
    main()

# Sample Input / Output

"""
Input:

Enter the Number of Strings:
n = 4

Enter the Strings:
s = "information", "informatics", "infographs", "infograohics"

Output:

The Longest Common Prefix among the given strings:
"info"
"""

# Link

"""
Access the Problem:-
    Take U Forward (TUF): https://takeuforward.org/plus/dsa/problems/longest-common-prefix
    Leetcode (Question No. 14): https://leetcode.com/problems/longest-common-prefix/description/
    Geeks For Geeks (GFG): https://www.geeksforgeeks.org/problems/longest-common-prefix-in-an-array5129/1
    Naukri Code 360 (Coding Ninjas): https://www.naukri.com/code360/problems/longest-common-prefix_2090383

Article: https://takeuforward.org/data-structure/longest-common-prefix
"""