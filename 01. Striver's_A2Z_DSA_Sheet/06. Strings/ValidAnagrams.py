# Check if two strings are anagrams of each other
# Valid Anagram
# Anagram

"""
Problem Statement:-

    Given two strings s and t, return true if t is an anagram of s, and false otherwise.
    An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
        typically using all the original letters exactly once.

Examples:-

    Example 1:
    
        Input: 
            s = "anagram", 
            t = "nagaram"
        Output: 
            true
        Explanation:
            We can rearrange the characters of string s to get string t as frequency of all characters from both strings is same.
    
    Example 2:
    
        Input: 
            s = "dog", 
            t = "cat"
        Output: 
            false
        Explanation:
            We cannot rearrange the characters of string s to get string t as frequency of all characters from both strings is not same.
"""

# Function to check if two strings are anagrams of each other
def isAnagram (s, t):
    
    # Check if the lengths of both the strings are equal
    if len(s) != len(t):
        return False
    
    # Create a frequency array of size 26 to store the frequency of each character
    freq = [0] * 26
    
    # Traverse through the first string and increment the frequency of each character
    for ch in s:
        freq[ord(ch) - ord('a')] += 1
    
    # Traverse through the second string and decrement the frequency of each character
    for ch in t:
        freq[ord(ch) - ord('a')] -= 1
    
    # Check if all the frequencies are zero
    for count in freq:
        if count != 0:
            return False
    
    # If all the frequencies are zero, the strings are anagrams
    return True

# Main Function
def main():
    
    # Take User Input for the Strings
    s = input("Enter the 1st String:\n")
    t = input("Enter the 2nd String:\n")
    
    # Call the function and print the result
    print(f"Are {s} and {t} Anagrams?")
    
    if isAnagram(s, t):
        print(True)
    
    else:
        print(False)

if __name__ == "__main__":
    main()

# Sample Input / Output

"""
Input:

Enter the 1st String: 
s = listen

Enter the 2nd String: 
t = silent

Output:

Are listen and silent Anagrams?
True
"""

# Link

"""
Access the Problem:-
    Take U Forward (TUF): https://takeuforward.org/plus/dsa/problems/valid-anagram
    Leetcode (Question No. 242): https://leetcode.com/problems/valid-anagram/description/
    Geeks For Geeks (GFG): https://www.geeksforgeeks.org/problems/anagram-1587115620/1

Article: https://takeuforward.org/data-structure/check-if-two-strings-are-anagrams-of-each-other/
"""