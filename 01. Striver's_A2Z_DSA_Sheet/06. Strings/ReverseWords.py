# Reverse Words in a String

"""
Problem Statement:-

    Reverse every word in a string

    Given an input string, containing upper-case and lower-case letters, digits, and spaces( ' ' ). 
    A word is defined as a sequence of non-space characters. 
    The words in s are separated by at least one space.
    Return a string with the words in reverse order, concatenated by a single space.

Examples:-

    Example 1:
    
        Input: 
            s = "welcome to the jungle" 
        Output: 
            "jungle the to welcome"
        Explanation: 
            The words in the input string are --
                "welcome", "to", "the", and "jungle". 
            Reversing the order of these words gives --
                "jungle", "the", "to", and "welcome". 
            The output string should have exactly one space between each word.
    
    Example 2:
    
        Input: 
            s = " amazing  coding  skills "
        Output: 
            "skills coding amazing"
        Explanation: 
            The input string has leading and trailing spaces, as well as multiple spaces between the words "amazing", "coding", and "skills".
            After trimming the leading and trailing spaces and reducing the multiple spaces between words to a single space, 
                the words are "amazing", "coding", and "skills". 
            Reversing the order of these words gives "skills", "coding", and "amazing". 
            The output string should not have any leading or trailing spaces and should have exactly one space between each word.
"""

# Function to reverse words in a string
def reverseWords(s):
    
    # Split the string into words
    words = s.split()
    
    # Reverse the list of words
    words.reverse()
    
    # Join the words with a single space and return the result
    return ' '.join(words)

# Main Function
def main():
    
    # Take User Input for the String
    s = input("Enter the String:\n")
    
    # Call the function and print the result
    print(f"The String with Words in a Reversed Manner:\n{reverseWords(s)}")

if __name__ == "__main__":
    main()

# Sample Input / Output

"""
Input:

Enter the String:
s = "this is a good example"

Output:

The String with Words in a Reversed Manner:
"example good a is this"
"""

# Link

"""
Access the Problem:-
    Take U Forward (TUF): https://takeuforward.org/plus/dsa/problems/reverse-every-word-in-a-string
    Leetcode (Question No. 151): https://leetcode.com/problems/reverse-words-in-a-string/description/
    Geeks For Geeks (GFG): https://www.geeksforgeeks.org/problems/reverse-words-in-a-given-string5459/1
    Naukri Code 360 (Coding Ninjas): https://www.naukri.com/code360/problems/reverse-words_696444

Article: https://takeuforward.org/data-structure/reverse-words-in-a-string/
"""