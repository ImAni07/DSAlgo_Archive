# Remove Outermost Parenthesis

"""
Problem Statement:-

    Remove Outermost Parenthesis
    
    A valid parentheses string is defined by the following rules:
        a) It is the empty string "".
        b) If A is a valid parentheses string, then so is "(" + A + ")".
        c) If A and B are valid parentheses strings, then A + B is also valid.
    
    A primitive valid parentheses string is a non-empty valid string that cannot be split into two or more non-empty valid parentheses strings.
    Given a valid parentheses string s, consider its primitive decomposition: 
        s = P1 + P2 + ... + Pk, 
            where Pi are primitive valid parentheses strings.
    
    Return s after removing the outermost parentheses of every primitive string in the primitive decomposition of s.

Examples:-

    Example 1:
    
        Input: 
            s = "((()))"
        Output: 
            "(())"
        Explanation:
            The input string is a single primitive: 
                "((()))".
            Removing the outermost layer yields: 
                "(())".
    
    Example 2:
    
        Input: 
            s = "()(()())(())"
        Output: 
            "()()()"
        Explanation:
            Primitive decomposition: 
                "()" + "(()())" + "(())"
            After removing outermost parentheses: 
                "" + "()()" + "()"
            Final result: 
                "()()()".
"""

# Function to remove outermost parenthesis
def removeOuterParentheses (s):
    
    # Declare an empty list to store the result
    result = []
    
    # Declare a variable to keep track of the balance of parenthesis
    track_parenthesis = 0
    
    # Traverse through the string
    for char in s:
        
        # If the character is an opening parenthesis
        if char == '(':
            
            # If the balance is greater than 0, append the character to the result
            if track_parenthesis > 0:
                result.append(char)
                
            # Increment the balance
            track_parenthesis += 1
            
        # If the character is a closing parenthesis
        else:
            
            # Decrement the balance
            track_parenthesis -= 1
            
            # If the balance is greater than 0, append the character to the result
            if track_parenthesis > 0:
                result.append(char)
    
    # Return the result
    return ''.join(result)

# Main Function
def main():
    
    # Take User Input for the String
    s = input("Enter the Parenthesis:\n")
    
    # Call the function and print the result
    print(f"The Valid Parenthesis String after the Removal of Outermost Parenthesis:\n{removeOuterParentheses(s)}")

if __name__ == "__main__":
    main()

# Sample Input / Output

"""
Input:

Enter the Parenthesis:
s = "(()())(())"

Output:

The Valid Parenthesis String after the Removal of Outermost Parenthesis:
"()()()()(())"
"""

# Link

"""
Access the Problem:-
    Take U Forward (TUF): https://takeuforward.org/plus/dsa/problems/remove-outermost-parentheses
    Leetcode (Question No. 1021): https://leetcode.com/problems/remove-outermost-parentheses/description/
    Geeks For Geeks (GFG): https://www.geeksforgeeks.org/problems/outermost-parentheses/1

Article: https://takeuforward.org/data-structure/remove-outermost-parentheses
"""