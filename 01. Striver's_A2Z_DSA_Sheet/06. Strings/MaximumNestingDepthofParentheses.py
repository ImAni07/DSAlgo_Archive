# Maximum Nesting Depth of Parentheses

"""
Problem Statement:-

    A string s is a valid parentheses string (VPS) if it meets the following conditions:
        a) It only contains digits 0-9, arithmetic operators +, -, *, /, and parentheses (, ).
        b) The parentheses are balanced and correctly nested.
    
    The task is to compute the maximum nesting depth of parentheses in s. 
    The nesting depth is the highest number of parentheses that are open at the same time at any point in the string.

Examples:-

    Example 1:
    
        Input: 
            s = "(1+(2*3)+((8)/4))+1"
        Output: 
            3
        Explanation: 
            The deepest nested sub-expression is ((8)/4), which has 3 layers of parentheses.

    Example 2:
    
        Input: 
            s = "(1)+((2))+(((3)))"
        Output: 
            3
        Explanation: 
            The digit '3' is enclosed in 3 pairs of parentheses.
"""

# Function to find the maximum depth of nesting parentheses
def maxDepth (s):
    
    # Keep track of the maximum depth
    max_depth = 0
    
    # Keep track of the current depth
    current_depth = 0
    
    # Iterate over each character of the given string
    for char in s:
        
        # If the character is an opening parenthesis, 
        # increase the value of current depth by 1
        if char == '(':
            current_depth += 1
            
            # If the current depth is greater than the maximum depth, 
            # update the maximum depth
            if current_depth > max_depth:
                max_depth = current_depth
        
        # If the character is a closing parenthesis, 
        # decrease the value of current depth by 1
        if char == ')':
            current_depth -= 1
    
    # Return the value of the maximum depth
    return max_depth

# Main Function
def main ():
    
    # Take User Input for the String
    s = input ("Enter the Required String:\n")
    
    # Print the Output
    print (f"The Maximum Nesting Depth of Parentheses is: {maxDepth (s)}")

if __name__ == '__main__':
    main ()

# Sample Input / Output

"""
Input:

Enter the Required Strength:
s = "((5+2)(3+4)((6)))"

Output:

The Maximum Nesting Depth of Parentheses is: 3
"""

# Link

"""
Access the Problem:-
    Take U Forward (TUF): https://takeuforward.org/plus/dsa/problems/maximum-nesting-depth-of-the-parentheses
    Leetcode (Question No. 1614): https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/description/
    Geeks For Geeks (GFG): https://www.geeksforgeeks.org/problems/maximum-nesting-depth-of-the-parentheses/1
    Naukri Code 360 (Coding Ninjas): https://www.naukri.com/code360/problems/maximum-nesting-depth-of-the-parentheses_8144741

Article: https://takeuforward.org/data-structure/maximum-nesting-depth-of-parenthesis
"""