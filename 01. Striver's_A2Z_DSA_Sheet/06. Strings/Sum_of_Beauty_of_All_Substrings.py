# Sum of Beauty of All Substrings

"""
Problem Statement:-

    Sum of Beauty of All Substrings
    
    The beauty of a string is defined as the difference between 
        the frequency of the most frequent character and the least frequent character 
        (excluding characters that do not appear) in that string.
    
    Given a string s, return the sum of beauty values of all possible substrings of s.

Examples:-

    Example 1:
    
        Input: 
            s = "xyx"
        Output: 
            1
        Explanation: 
            The substrings with non-zero beauty are:
                - "xyx" → frequencies: x:2, y:1 → beauty = 2 - 1 = 1
                - "xy" → x:1, y:1 → beauty = 0
                - "yx" → y:1, x:1 → beauty = 0
                - "x" or "y" → beauty = 0
                Total sum = 1 (from "xyx") = 1
    
    Example 2:
    
        Input: 
            s = "aabcbaa"
        Output: 
            17
        Explanation: 
            Various substrings such as "aabc", "bcba", etc., have non-zero beauty values. 
            Summing all gives 17.
"""

# Function to compute the beauty sum of the given string
def beautySum (s):
    
    # Initialize the beauty sum to 0
    beauty_sum = 0
    
    # Iterate over the string
    for i in range (len (s)):
        
        # Initialize a list to contain all the frequencies
        freq = [0] * 26
        
        # Calculate frequency of the current character
        for j in range (i, len (s)):
            
            # Initialize the maximum frequency to a very small value (negative infinity)
            max_freq = float("-inf")
            
            # Initialize the minimum frequency to a very large value (positive infinity)
            min_freq = float("inf")
            
            freq[ord (s[j]) - ord ("a")] += 1
            
            # Update the maximum and minimum frequencies
            for k in freq:
                
                # If the character is present
                if k !=0:
                    
                    max_freq = max (max_freq, k)
                    min_freq = min (min_freq, k)
            
            # Calculate the beauty sum
            beauty_sum += max_freq - min_freq
    
    # Return the beauty sum
    return beauty_sum

# Main Function
def main ():
    
    # Take User Input for the String
    s = input ("Enter a String:\n")
    
    # Print the Output
    print (f"The Beauty Sum:\n{beautySum (s)}")

if __name__ == "__main__":
    main ()

# Sample Input / Output

"""
Input:

Enter a String:
s = "aabcb"

Output:

The Beauty Sum:
5
"""

# Link

"""
Access the Problem:-
    Take U Forward (TUF): https://takeuforward.org/plus/dsa/problems/sum-of-beauty-of-all-substrings
    Leetcode (Question No. 1781): https://leetcode.com/problems/sum-of-beauty-of-all-substrings/description/
    Geeks For Geeks (GFG): https://www.geeksforgeeks.org/problems/sum-of-beauty-of-all-substrings-1662962118/1
    Naukri Code 360 (Coding Ninjas): https://www.naukri.com/code360/problems/sum-of-beauty-of-all-substrings_8143656

Article: https://takeuforward.org/data-structure/sum-of-beauty-of-all-substring
"""