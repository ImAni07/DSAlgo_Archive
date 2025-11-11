# Rotate Strings
# Check whether one string is a rotation of another

"""
Problem Statement:-

    Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.
    A shift on s consists of moving the leftmost character of s to the rightmost position.
    
    For example, 
        if s = "abcde", 
        then it will be "bcdea" after one shift.

Examples:-

    Example 1:
    
        Input: 
            s = "abcde", 
            goal = "cdeab"
        Output: 
            true
        Explanation:
            After performing 2 shifts we can achieve the goal string from string s.
                After first shift the string s is => bcdea
                After second shift the string s is => cdeab.
    
    Example 2:
    
        Input: 
            s = "abcde", 
            goal = "adeac"
        Output: 
            false
        Explanation:
            Any number of shift operations cannot convert string s to string goal.
"""

# Check if the string 'goal' can be obtained by rotating s
def rotateString (s, goal):
    
    # Check if both the strings have the same length
    # If no, then return False
    if len (s) != len (goal):
        return False
    
    # Check if 'goal' is a substring of s when concatenated with itself
    if goal in (s + s):
        
        # If yes
        return True
    
    else:
        return False

# Main Function
def main ():
    
    # Take User Input for the String
    s = input ("Enter a String:\n")
    
    # Take User Input for the 'goal' String
    goal = input ("Enter the Goal String:\n")
    
    # Output
    print(f"Can {s} become {goal} after some shifts?")
    
    if rotateString(s, goal):
        print(True)
    
    else:
        print(False)

if __name__ == "__main__":
    main ()

# Sample Input / Output

"""
Input:

Enter a String:
s = "abcxyz"

Enter the Goal String:
goal = "xyzabc"

Output:

Can "abcxyz" become "xyzabc" after some shifts?
True
"""

# Link

"""
Access the Problem:-
    Take U Forward (TUF): https://takeuforward.org/plus/dsa/problems/rotate-string
    Leetcode (Question No. 796): https://leetcode.com/problems/rotate-string/description/

Article: https://takeuforward.org/data-structure/check-if-one-string-is-rotation-of-another
"""