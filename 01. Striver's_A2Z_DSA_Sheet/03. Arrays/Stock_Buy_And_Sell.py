# Best Time to Buy and Sell Stock

"""
Problem Statement:-

    Stock Buy and Sell
    
    Given an array of n integers, 
    where the ith element represents price of the stock on the ith day. 
    Determine the maximum profit achievable by buying and selling the stock at most once.
    
    The stock should be purchased before selling it, and 
    both actions cannot occur on the same day.

Examples:-

    Example 1:
    
        Input: 
            prices = [10, 7, 5, 8, 11, 9]
        Output: 
            6
        Explanation: 
            Buy on day 3 (price = 5) and 
            sell on day 5 (price = 11), 
            profit = 11 - 5 = 6.
    
    Example 2:
    
        Input: 
            prices = [5, 4, 3, 2, 1]
        Output: 
            0
        Explanation: 
            In this case, no transactions are made. 
            Therefore, the maximum profit remains 0.
"""

# Function to Determine the Best Time to Buy and Sell Stock
def maxProfit (prices):
    
    # Declare the maximum profit and minimum cost price to 0 and the 0th element of the given array, respectively
    max_profit = 0
    min_cost_price = prices [0]
    
    # Travel through the array
    for i in range (len (prices)):
        
        # Update the minimum cost price
        min_cost_price = min (min_cost_price, prices [i])
        
        # Update the maximum profit
        max_profit = max (max_profit, prices [i] - min_cost_price)
    
    # Return the required result
    return max_profit

# Main Function
def main():
    
    # Take User Input for the Size of the Array
    n = int (input ("Enter the Number of Days:\n"))
    
    # Take User Input for the Prices of the Stocks for 'n' Number of Days
    prices = list (map (int, input ("Enter the Stock Prices:\n").split ()))
    
    # Output
    print (f"The Maximum Possible Profit is: {maxProfit (prices)}")

if __name__ == "__main__":
    main()

# Sample Input / Output

"""
Input:

Enter the Number of Days:
n = 6

Enter the Stock Prices:
prices = 7 1 5 3 6 4

Output:

The Maximum Possible Profit is: 5
"""

# Link

"""
Access the Problem:-
    Take U Forward (TUF): https://takeuforward.org/plus/dsa/problems/best-time-to-buy-and-sell-stock
    Leetcode (Question No. 121): https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
    Naukri Code 360 (Coding Ninjas): https://www.naukri.com/code360/problems/stocks-are-profitable_893405

Article: https://takeuforward.org/data-structure/stock-buy-and-sell/
"""