# Longest Palindromic Substring

"""
Problem Statement:-

    Given a string s, return the longest palindromic substring in s.

Examples:-

    Example 1:
    
        Input: 
            s = "babad"
        Output: 
            "bab"
        Explanation: 
            It is the longest palindromic substring. 
            "aba" is also a valid answer.
    
    Example 2:
    
        Input: 
            s = "cbbd"
        Output: 
            "bb"
        Explanation: 
            It is the longest palindromic substring.
"""

# Helper function to expand around center
def expand_around_center (s, left, right):
    
    # Expand while valid and characters match
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    
    return right - left - 1

# Function to find the longest palindromic substring
def longestPalindrome (s):
    
    # If the string is empty, return an empty string
    if not s:
        return ""
    
    # Initialize the start and end pointers
    start = 0
    end = 0
    
    # Iterate through each character as center
    for center in range (len(s)):
        
        # Expand around odd length
        odd_length = expand_around_center(s, center, center)
        
        # Expand around even length
        even_length = expand_around_center(s, center, center + 1)
        
        # Take the maximum length from both cases
        max_length = max (odd_length, even_length)
        
        # Update the boundaries if longer palindrome found
        if max_length > end - start:
            start = center - (max_length - 1) // 2
            end = center + max_length // 2
    
    # Return the longest palindromic substring
    return s[start:end + 1]

# Main Function
def main ():
    
    # Take User Input for String
    s = input ("Enter a String:\n")
    
    # Output
    print (f"Longest Palindromic Substring:\n{longestPalindrome(s)}")

if __name__ == "__main__":
    main ()

# Sample Input / Output

"""
Input:

Enter a String:
s = "noon"

Output:

Longest Palindromic Substring:
noon
"""

# Link

"""
Access the Problem:-
    Leetcode (Question No. 5): https://leetcode.com/problems/longest-palindromic-substring/description/

Article: https://takeuforward.org/data-structure/longest-palindromic-substring
"""