# Sort Characters by Frequency

"""
Problem Statement:-

    You are given a string s. 
    Return the array of unique characters, sorted by highest to lowest occurring characters.
    If two or more characters have same frequency then arrange them in alphabetic order.

Examples:-

    Example 1:
    
        Input: 
            s = "tree"
        Output: 
            ['e', 'r', 't' ]
        Explanation:
            The occurrences of each character are as shown below :
                e --> 2
                r --> 1
                t --> 1.
            The r and t have same occurrences , so we arrange them by alphabetic order.

    Example 2:
    
        Input: 
            s = "raaaajj"
        Output: 
            ['a' , 'j', 'r' ]
        Explanation:
            The occurrences of each character are as shown below :
                a --> 4
                j --> 2
                r --> 1
"""

# Function to sort the characters of the given string by frequency
def sortByFrequency (s):
    
    # Create a frequency map to store the frequency of each character of the given string
    frequecy_map = {}
    
    # Iterate over the string
    for char in s:
        
        # If the character is already present in the frequency map, 
        # increment its count
        if char in frequecy_map:
            frequecy_map[char] += 1
        
        # If the character is encountered for the first time, 
        # add it to the frequency map with count 1
        else:
            frequecy_map[char] = 1
    
    # Sort the frequency map by values in descending order and 
    # by characters in a lexographical order
    sorted_map = sorted (frequecy_map.items(), key = lambda item: (-item[1], item[0]))
    
    # (-item[1] --> refers to the sorting of the character in a decreasing order, 
    # with respect to the frequency of the character)
    
    # (item[0] --> refers to the sorting of the character in a lexicographical order)
    
    # Declare a variable to store the resultant sorted string
    answer = ''
    
    # Iterate over the sorted map:
    for ch, count in sorted_map:
        
        # Append the character to the resultant string
        answer += ch * count
    
    # Return the resultant 
    return answer

# Main Function
def main ():
    
    # Take User Input for the String
    s = input ("Enter a String:\n")
    
    # Print the Output
    print (f"The answer is:\n{sortByFrequency (s)}")

if __name__ == '__main__':
    main ()

# Sample Input / Output

"""
Input:

Enter a String:
s = "tree"

Output:

The answer is:
"eert"
"""

# Link

"""
Access the Problem:-
    Take U Forward (TUF): https://takeuforward.org/plus/dsa/problems/sort-characters-by-frequency
    Leetcode (Question No. 451): https://leetcode.com/problems/sort-characters-by-frequency/description/
    Geeks For Geeks (GFG): https://www.geeksforgeeks.org/problems/sort-string-according-to-increasing-frequency/1
    Naukri Code 360 (Coding Ninjas): https://www.naukri.com/code360/problems/sorting-characters-by-frequency_1263699

Article: https://takeuforward.org/data-structure/sort-characters-by-frequency
"""