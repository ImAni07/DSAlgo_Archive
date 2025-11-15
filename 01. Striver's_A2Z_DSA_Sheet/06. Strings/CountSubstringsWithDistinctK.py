# Count Substrings with Distinct K
# Count Number of Substrings

"""
Problem Statement:-

    Count Number of Substrings
    
    You are given a string s and a positive integer k.
    Return the number of substrings that contain exactly k distinct characters.

Examples:-

    Example 1:
    
        Input: 
            s = "pqpqs", 
            k = 2  
        Output: 
            7  
        Explanation:  
            All substrings with exactly 2 distinct characters:  
                "pq", "pqp", "pqpq", "qp", "qpq", "pqs", "qs"  
            Total = 7.
    
    Example 2:
    
        Input: 
            s = "abcbaa", 
            k = 3  
        Output: 
            5  
        Explanation:  
            All substrings with exactly 3 distinct characters:  
                "abc", "abcb", "abcba", "bcba", "cbaa"  
            Total = 5.
"""

# Function to count substrings with at most k distinct characters
def count_k_distinct (s, k):
    
    # Declare the required variables
    left_pointer = 0
    answer = 0
    freq = {}
    distinct = 0 

    # Iterate using the right pointer
    for right_pointer in range(len(s)):
        
        # Add current character
        if freq.get(s[right_pointer], 0) == 0:
            distinct += 1
        
        freq[s[right_pointer]] = freq.get(s[right_pointer], 0) + 1

        # Shrink window when distinct > k
        while distinct > k:
            
            freq[s[left_pointer]] -= 1
            if freq[s[left_pointer]] == 0:
                distinct -= 1
            left_pointer += 1

        # Add all substrings ending at right
        answer += (right_pointer - left_pointer + 1)

    # Return the obtained answer
    return answer

# Function to count substrings with exactly k distinct characters
def count_substrings(s, k):
    
    # Return the count
    return count_k_distinct(s, k) - count_k_distinct(s, k - 1)

# Main Function
def main():
    
    # Take User Input for the String
    s = input ("Enter a String:\n")
    
    # Take User Input for the Window Length
    k = int (input ("Number of Distinct Characters Required:\n"))
    
    # Output
    print (f"The Number of Substrings with 'k' distinct characters are:\n{count_substrings(s,k)}")

if __name__ == "__main__":
    main()

# Sample Input / Output

"""
Input:

Enter a String:
s = "abc"

Number of Distinct Characters Required:
k = 2

Output:

The Number of Substrings with 'k' distinct characters are:
2
"""

# Link

"""
Access the Problem:-
    Geeks For Geeks (GFG): https://www.geeksforgeeks.org/problems/count-number-of-substrings4528/1

Article: https://takeuforward.org/data-structure/count-number-of-substrings
"""