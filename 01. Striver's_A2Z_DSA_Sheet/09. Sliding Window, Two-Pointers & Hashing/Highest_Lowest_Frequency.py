# Highest / Lowest Frequency Elements in an Array

"""
Problem Statement:-

    Find the highest/lowest frequency element
    
    Given an array of size N. Find the highest and lowest frequency element.

Examples:-

    Example 1:
    
        Input: 
            array[] = {10,5,10,15,10,5};
        Output: 
            10 15
        Explanation: 
            The frequency of 10 is 3, i.e. the highest and the frequency of 15 is 1 i.e. the lowest.
    
    Example 2:
    
        Input: 
            array[] = {2,2,3,4,4,2};
        Output: 
            2 3
        Explanation: 
            The frequency of 2 is 3, i.e., the highest and the frequency of 3 is 1 i.e. the lowest.
"""

# Function to get the highest as well as the lowest frequency elements from the given array
def getFrequencies (n, v):
    
    # Handle the Edge Case --> When the arrayv is null
    if not v:
        return [0, 0]
    
    else:
        
        # Create a hashmap to store the frequency of each element in the array
        freqMap = {}
        
        # Create a resultant list
        result = []
        
        # Iterate through the array and update the corresponding frequencies
        for i in range(n):
            
            # If it is already present, increment the frequency by 1
            if v[i] in freqMap:
                freqMap[v[i]] += 1
            
            # If not present, then insert it and initialize the frequency to 1
            else:
                freqMap[v[i]] = 1
        
        # Determine the Highest as well as the Lowest Frequency Elements
        
        # For Highest Frequency
        maxFreq = max(freqMap.values())
        maxFreqElements = [key for key, value in freqMap.items() if value == maxFreq]
        
        # Choose the smallest value
        if len(maxFreqElements) > 1:
            highestCount = min(maxFreqElements)
        else:
            highestCount = maxFreqElements[0]
        
        # For Lowest Frequency
        minFreq = min(freqMap.values())
        minFreqElements = [key for key, value in freqMap.items() if value == minFreq]
        
        # Choose the smallest value
        if len(minFreqElements) > 1:
            lowestCount = min(minFreqElements)
        else:
            lowestCount = minFreqElements[0]
        
        # Append the required elements in the resultant list
        result.append(highestCount)
        result.append(lowestCount)
        
        # Return the result
        return result

# Main Function
def main():
    
    # Take User Input
    
    # Size of the Array
    n = int(input("Enter the number of elements in the array: "))
    
    # Elements of the Array
    v = list(map(int, input("Enter the elements of the array: ").split()))
    
    # Output
    print(getFrequencies(n, v))

if __name__ == "__main__":
    main()

# Sample Input / Output

"""
Input:

Enter the number of elements in the array: 
n = 6

Enter the elements of the array: 
v = [10 15 10 15 5 6]

Output:
[10, 5]
"""

# Links

"""
Access the Problem:-
    Take U Forward (TUF): https://takeuforward.org/plus/dsa/problems/highest-occurring-element-in-an-array
    Naukri Code 360 (Coding Ninjas): https://www.naukri.com/code360/problems/k-most-occurrent-numbers_625382

Article: https://takeuforward.org/arrays/find-the-highest-lowest-frequency-element/
"""