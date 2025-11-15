# Reverse Words in a String
# Palindrome Check

"""
Problem Statement:-

    Reverse the words of the string and check for palindrome too.
"""

# Function to reverse words in a string
def reverseWords(s):
    
    # Split the string into words
    words = s.split()
    
    # Reverse the list of words
    words.reverse()
    
    # Join the words with a single space and return the result
    return ' '.join(words)

# Function to check if the string is a palindrome
def isPalindrome(s):
    
    # Remove spaces and convert to lowercase
    s_updated = ''.join(s.split()).lower()
    
    # Return the cleaned string
    return s_updated == s_updated[::-1]

# Main Function
def main():
    
    # Take User Input for the String
    s = input("Enter the String:\n")
    
    # Output
    
    # Print the string in a reversed manner
    print(f"The String with Words in a Reversed Manner:\n{reverseWords(s)}")
    
    # Palindrome Check
    if isPalindrome(s):
        print(f"Palindrome Check:\nThe given string is a Palindrome.")
    else:
        print(f"Palindrom Check:\nThe given string is not a Palindrome.")

if __name__ == "__main__":
    main()

# Sample Input / Output

"""
Input:

Enter the String:
s = "nurses run"

Output:

The String with Words in a Reversed Manner:
"run nurses"

Palindrome Check:
The given string is a Palindrome.
"""