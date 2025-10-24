# Array Leaders
# Superior Elements

# Leaders in an Array

# Function to find the Superior Elements
def superiorElements (a):
    
    # Declare an empty list to store the result
    leaders = []
    
    # Declare a variable to store the maximum elements 
    # initialize it to the last element of the array, 
    # since the last element is always a superior element
    
    superior_element = a[(len(a)-1)]
    
    # Append this to the list of leaders
    leaders.append(superior_element)
    
    # Do a backward iteration through the array
    for i in range(len(a)-2,-1,-1):
        
        # Check whether the ith element is greater than the superior_element, 
        # if yes, then append it to the list and 
        # also update the value of superior_element
        
        if a[i] > superior_element:
            leaders.append(a[i])
            superior_element = a[i]
    
    # Since the elements are appended in a reverse manner, 
    # so arrange them in an order same as that of the given array
    leaders.reverse()
    
    # Sort the resultant list
    leaders.sort()
    
    # Return the result
    return leaders

# Main Function
def main():
    
    # Take User Input for the Size of the Array
    n = int (input ("Enter the Size of the Array:\n"))
    
    # Take User Input for the Elements of the Array
    a = list (map (int , input ("Enter the Elements of the Array:\n").split ()))
    
    # Output
    print (f"The Array Leaders are:\n{superiorElements (a)}")

if __name__ == "__main__":
    main ()

# Sample Input / Output

"""
Input:

Enter the Size of the Array:
n = 6

Enter the Elements of the Array:
a = 16 17 4 3 5 2

Output:

The Array Leaders are:
17 5 2
"""

# Links

"""
Access the Problem:-
    Take U Forward (TUF): https://takeuforward.org/plus/dsa/problems/leaders-in-an-array
    Geeks For Geeks (GFG): https://www.geeksforgeeks.org/problems/leaders-in-an-array-1587115620/1
    Naukri Code 360 (Coding Ninjas): https://www.naukri.com/code360/problems/leaders-in-an-array_873144

Article: https://takeuforward.org/data-structure/leaders-in-an-array/
"""