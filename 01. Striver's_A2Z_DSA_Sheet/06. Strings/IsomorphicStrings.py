# Isomorphic Strings

"""
Problem Statement:-

    Given two strings s and t, determine if they are isomorphic. 
    Two strings s and t are isomorphic if the characters in s can be replaced to get t.
    
    All occurrences of a character must be replaced with another character while preserving the order of characters. 
    No two characters may map to the same character, but a character may map to itself.

Examples:-

    Example 1:
    
        Input: 
            s = "egg", 
            t = "add"
        Output: 
            true
        Explanation:
            The 'e' in string s can be replaced with 'a' of string t.
            The 'g' in string s can be replaced with 'd' of t.
            Hence all characters in s can be replaced to get t.
    
    Example 2:
    
        Input: 
            s = "apple", 
            t = "bbnbm"
        Output: 
            false
        Explanation:
            It can be proved that no solution exists for this example.
            All the "b"s in t have to take places of "a", "p", "l", which requires "p" to be mapped to "b", 
                but that makes it impossible for "p" at index 2 (0-indexed) to become "n". 
                Thus no solution exists.
"""

# Approach 1: Using Hash Map

# Function to check if two strings are isomorphic
def isIsomorphic_hashmap (s, t):
    
    # Check the lengths of both the strings, if they are not equal, return False
    if len (s) != len (t):
        return False
    
    # Create two dictionaries to store the mapping of characters from s to t and vice versa
    map_s_to_t = {}
    map_t_to_s = {}
    
    # Iterate over the characters of both the strings
    for char_s, char_t in zip (s, t):
        
        # Check if the character from s is already mapped to a different character in t
        if char_s in map_s_to_t:
            
            # If it is, check if the mapped character in t is the same as the current character in t
            if map_s_to_t[char_s] != char_t:
                return False
        
        # If the character is not mapped, add the mapping to the dictionaries
        else:
            map_s_to_t[char_s] = char_t
            
        # Check if the character from t is already mapped to a different character in s
        if char_t in map_t_to_s:
            
            # If it is, check if the mapped character in s is the same as the current character in s
            if map_t_to_s[char_t] != char_s:
                return False
        
        # If the character is not mapped, add the mapping to the dictionaries
        else:
            map_t_to_s[char_t] = char_s
    
    # Return the result
    return True

# Approach 2: Last Seen Index

# Function to check if two strings are isomorphic
def isIsomorphic_lastseenindex (s, t):
    
    # Check the lengths of both the strings, if they are not equal, return False
    if len (s) != len (t):
        return False
    
    # Create two dictionaries to store the last seen index of characters of both the strings
    last_seen_index_s = {}
    last_seen_index_t = {}
    
    # Iterate over the characters of both the strings
    for i, (char_s, char_t) in enumerate (zip (s, t)):
        
        # Check the last seen index of the both the strings
        if last_seen_index_s.get (char_s, -1) != last_seen_index_t.get (char_t, -1):
            return False
        
        # Update the last seen index of the both the strings
        last_seen_index_s[char_s] = i
        last_seen_index_t[char_t] = i
    
    # Return the result
    return True

# Approach 3: Using Set

# # Function to check if two strings are isomorphic
def isIsomorphic_set (s, t):
    
    # Return the lengths of the set of the characters of both the strings
    return len (set (s)) == len (set (t)) and len (set (t)) == len (set (zip (s, t)))

# Main Function
def main():

    # Take user input
    s = input("Enter first string:\n")
    t = input("Enter second string:\n")
    
    # Message
    print("\nChecking if the given strings are isomorphic\n")

    # Output
    
    # Approach 1
    result1 = isIsomorphic_hashmap(s, t)
    
    if result1:
        print("Approach 1 (Using Hash Map): Isomorphic")
    
    else:
        print("Approach 1 (Using Hash Map): Not Isomorphic")

    # Approach 2
    result2 = isIsomorphic_lastseenindex(s, t)
    
    if result2:
        print("Approach 2 (Using Last Seen Index): Isomorphic")
    
    else:
        print("Approach 2 (Using Last Seen Index): Not Isomorphic")

    # Approach 3
    result3 = isIsomorphic_set(s, t)
    
    if result3:
        print("Approach 3 (Using Set): Isomorphic")
    
    else:
        print("Approach 3 (Using Set): Not Isomorphic")

    # Summary
    print("Result Summary\n")
    
    if result1 == result2 == result3:
        
        if result1:
            print("All approaches agree: Isomorphic")
        
        else:
            print("All approaches agree: Not Isomorphic")
    
    else:
        print("The approaches differ in their results. Please verify input or logic.")

if __name__ == '__main__':
    main()

# Sample Input / Output

"""
Input:

Enter first string:
s = egg
Enter second string:
t = add

Checking if the given strings are isomorphic

Output:

Approach 1 (Using Hash Map): Isomorphic
Approach 2 (Using Last Seen Index): Isomorphic
Approach 3 (Using Set): Isomorphic

Result Summary
All approaches agree: Isomorphic
"""

# Link

"""
Access the Problem:-
    Take U Forward (TUF): https://takeuforward.org/plus/dsa/problems/isomorphic-string
    Leetcode (Question No. 205): https://leetcode.com/problems/isomorphic-strings/description/
    Geeks For Geeks (GFG): https://www.geeksforgeeks.org/problems/isomorphic-strings-1587115620/1
    Naukri Code 360 (Coding Ninjas): https://www.naukri.com/code360/problems/isomorphic-strings-_1117636

Article: https://takeuforward.org/data-structure/isomorphic-string
"""