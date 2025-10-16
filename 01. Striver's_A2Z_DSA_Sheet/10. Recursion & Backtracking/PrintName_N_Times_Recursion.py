# Print something without using loop, but recursively

def printMyName (n):
    
    # Handle the Base Case
    if n == 0:
        return
    
    # If n is within the limit
    print ("Anirban", end=" ")
    
    # Return Statement (Call the function recursively)
    return printMyName (n-1)

# Main Function
def main():
    
    # Take User Input
    n = int (input ())
    
    # Print the Result
    printMyName (n)

if __name__ == "__main__":
    main()

# Sample Input / Output

"""
Input:
n = 7

Output:
Anirban Anirban Anirban Anirban Anirban Anirban Anirban
"""

# Link

"""
Access the problem:-
    Geeks For Geeks (GFG): https://www.geeksforgeeks.org/problems/print-gfg-n-times/1&selectedLang=python3
    Code Studio (Coding Ninjas): https://www.naukri.com/code360/problems/-print-n-times_8380707

Article: https://takeuforward.org/recursion/print-name-n-times-using-recursion/
"""