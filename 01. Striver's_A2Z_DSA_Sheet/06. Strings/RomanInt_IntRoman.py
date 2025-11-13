# Conversion of Roman Numerals to Integers and vice-versa

"""
This Python script contains the codes for both converting a given Roman number to an Integer and vice-versa.

    Problem 1 --> Conversion of Roman Numerals to Integer
    Problem 2 --> Conversion of Integer Numbers to Roman Numeral
"""

# Problem 1
# Conversion of Roman Numerals to Integer

"""
Problem Statement:-

    Roman to Integer
    
    Roman numerals are represented by seven different symbols:
        I = 1
        V = 5
        X = 10
        L = 50
        C = 100
        D = 500
        M = 1000
    
    Roman numerals are typically written from largest to smallest, left to right. 
    However, in specific cases, a smaller numeral placed before a larger one indicates subtraction.
    
    The following subtractive combinations are valid:
        I before V (5) and X (10) → 4 and 9
        X before L (50) and C (100) → 40 and 90
        C before D (500) and M (1000) → 400 and 900
    
    Given a Roman numeral, convert it to an integer.

Examples:-

    Example 1:
    
        Input: 
            s = "III"
        Output: 
            3
        Explanation: 
            III = 1 + 1 + 1 = 3
    
    Example 2:
    
        Input: 
            s = "XLII"
        Output: 
            42
        Explanation: 
            XL = 40, II = 2 → 40 + 2 = 42
"""

# Function to convert the given Roman number to an Integer number
def romanToInt(s):
    
    # Create a dictionary to store the values of Roman numerals
    roman_numbers = {
            'I': 1, 
            'V': 5, 
            'X': 10, 
            'L': 50, 
            'C': 100, 
            'D': 500, 
            'M': 1000
        }
    
    # Variable to store the result
    sum = 0
    
    # Iterate through the Roman numeral string
    for i in range(len(s) - 1):
        
        # If the next character is greater than the ith character, 
        # then subtract the present value
        if roman_numbers[s[i]] < roman_numbers[s[i + 1]]:
            sum -= roman_numbers[s[i]]
        
        # Otherwise, add the present value
        else:
            sum += roman_numbers[s[i]]
    
    # Add the value of the last character
    sum += roman_numbers[s[-1]]
    
    # Return the result
    return sum

# Problem 2
# Conversion of Integer Number to Roman Numeral

"""
Problem Statement:-

    Integer to Roman
    
    Seven different symbols represent Roman numerals with the following values:

        Symbol	Value
        I	    1
        V	    5
        X	    10
        L	    50
        C	    100
        D	    500
        M	    1000
    
    Roman numerals are formed by appending the conversions of decimal place values from highest to lowest. 
    Converting a decimal place value into a Roman numeral has the following rules:
        If the value does not start with 4 or 9, 
            select the symbol of the maximal value that can be subtracted from the input, 
            append that symbol to the result, 
            subtract its value, and 
            convert the remainder to a Roman numeral.
        If the value starts with 4 or 9 
            use the subtractive form representing one symbol subtracted from the following symbol, 
            for example, 4 is 1 (I) less than 5 (V): IV and 9 is 1 (I) less than 10 (X): IX. 
            Only the following subtractive forms are used: 4 (IV), 9 (IX), 40 (XL), 90 (XC), 400 (CD) and 900 (CM).
        Only powers of 10 (I, X, C, M) can be appended consecutively at most 3 times to represent multiples of 10. 
            You cannot append 5 (V), 50 (L), or 500 (D) multiple times. 
            If you need to append a symbol 4 times use the subtractive form.
    
    Given an integer, convert it to a Roman numeral.

Examples:-

    Example 1:
    
        Input: 
            num = 3749
        Output: 
            "MMMDCCXLIX"
        Explanation:
            3000 = MMM as 1000 (M) + 1000 (M) + 1000 (M)
            700 = DCC as 500 (D) + 100 (C) + 100 (C)
            40 = XL as 10 (X) less of 50 (L)
            9 = IX as 1 (I) less of 10 (X)
            Note: 
                49 is not 1 (I) less of 50 (L) because the conversion is based on decimal places
    
    Example 2:
    
        Input: 
            num = 58
        Output: 
            "LVIII"
        Explanation:
            50 = L
            8 = VIII
    
    Example 3:
    
        Input: 
            num = 1994
        Output: 
            "MCMXCIV"
        Explanation:
            1000 = M
            900 = CM
            90 = XC
            4 = IV
"""

# Function to convert a given integer number to roman numeral
def intToRoman(num):
    
    # Create a list of tuples containing the integer values and their corresponding Roman numeral symbols
    roman_numerals = [
        (1000, 'M'),
        (900, 'CM'),
        (500, 'D'),
        (400, 'CD'),
        (100, 'C'),
        (90, 'XC'),
        (50, 'L'),
        (40, 'XL'),
        (10, 'X'),
        (9, 'IX'),
        (5, 'V'),
        (4, 'IV'),
        (1, 'I')
    ]
    
    # Declare a variable to store the result
    result = []
    
    # Iterate through the list of tuples
    for value, symbol in roman_numerals:
        
        # Check if the given number is greater than or equal to the current integer value
        # If yes, then append the corresponding Roman value
        while num >= value:
            result.append(symbol)
            num -= value
    
    # Return the result as a string
    return ''.join(result)

# Main Function
def main():
    
    # Message
    print("Choose Conversion Type:\n")
    print("1. Roman to Integer")
    print("2. Integer to Roman\n")
    
    # Enter the Choice
    choice = input("Enter your choice:\n")
    
    # Roman to Integer
    if choice == '1':
        
        # Take User Input for the Roman numeral string
        s = input("Enter a Roman numeral: ")
        
        # Print the output
        print(f"Integer value: {romanToInt(s)}")
    
    # Integer to Roman
    elif choice == '2':
        
        # Take User Input for the Integer Number
        num = int(input("Enter an Integer: "))
        
        # Print the Output
        print(f"Roman numeral: {intToRoman(num)}")
    
    else:
        print("Invalid choice! Please enter 1 or 2.")

if __name__ == '__main__':
    main()

# Problem 1 --> Roman to Integer
# Sample Input / Output

"""
Message:

Choose Conversion Type:

1. Roman to Integer
2. Integer to Roman

Input:

Enter your choice:
1

Enter a Roman Numeral:
s = "VII"

Output:

Integer value: 7
"""

# Problem 2 --> Integer to Roman
# Sample Input / Output

"""
Message:

Choose Conversion Type:

1. Roman to Integer
2. Integer to Roman

Input:

Enter your choice:
2

Enter an Integer:
num = 6

Output:

Roman numeral: "VI"
"""

# Link

"""
Access the Problem:-
    Take U Forward (TUF): https://takeuforward.org/plus/dsa/problems/roman-to-integer
    Leetcode (Question No. 13) [Problem 1]: https://leetcode.com/problems/roman-to-integer/description/
    Leetcode (Question No. 12) [Problem 2]: https://leetcode.com/problems/integer-to-roman/description/
    Geeks For Geeks (GFG) [Problem 1]: https://www.geeksforgeeks.org/problems/roman-number-to-integer3201/1
    Geeks For Geeks (GFG) [Problem 2]: https://www.geeksforgeeks.org/problems/convert-to-roman-no/1
    Naukri Code 360 (Coding Ninjas) [Problem 1]: https://www.naukri.com/code360/problems/roman-number-to-integer_981308
    Naukri Code 360 (Coding Ninjas) [Problem 2]: https://www.naukri.com/code360/problems/integer-to-roman-numeral_981307

Article: https://takeuforward.org/data-structure/roman-numerals-to-integer
"""