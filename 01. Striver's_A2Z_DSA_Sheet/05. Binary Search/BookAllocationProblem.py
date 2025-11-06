# Book Allocation Problem
# Allocate Books
# Allocate Minimum Number of Pages

"""
Problem Statement:-

    Book Allocation Problem
    
    Given an array arr of n integers, 
        where arr[i] represents the number of pages in the i-th book, and 
        an integer k representing the number of students.
    Allocate all the books to the students so that each student gets at least one book, 
        each book is allocated to only one student, and 
        the allocation is contiguous.
    Allocate the books to k students in such a way that the maximum number of pages assigned to a student is minimized. 
    If the allocation of books is not possible, return -1.

Examples:-

    Example 1:
    
        Input: 
            arr = [12, 34, 67, 90], 
            k = 2
        Output: 
            113
        Explanation: 
            The allocation of books will be 12, 34, 67 | 90. 
            One student will get the first 3 books and the other will get the last one.
    
    Example 2:
    
        Input: 
            arr = [25, 46, 28, 49, 24], 
            k = 4
        Output: 
            71
        Explanation: 
            The allocation of books will be 25, 46 | 28 | 49 | 24.
"""

# Function to count the number of students required to allocate the books with the given maximum pages
def countStudents (arr, pages):
    
    # Initialize the count of students required
    student_count = 1
    
    # Initialize the total_pages variable to keep track of the total pages allocated
    total_pages = 0
    
    # Length of the array of pages
    n = len(arr)
    
    # Iterate through the array of pages
    for i in range (n):
        
        # Calculate the total pages allocated to the current student, 
        # given that it does not exceed the maximum pages
        if total_pages + arr[i] <= pages:
            total_pages += arr[i]
        
        else:
            # If the total pages exceed the maximum pages, allocate the books to a new student
            student_count += 1
            total_pages = arr[i]
    
    # Return the total number of students required
    return student_count

# Function to find the minimum number of pages that can be allocated to the students
def findPages (arr, k):
    
    # Length of the array of pages
    n = len(arr)
    
    # If the number of students is greater than the number of books
    if k > n:
        return -1
    
    # Initialize the low and high pointers
    lo = max(arr)
    hi = sum(arr)
    
    # Apply Binary Search
    while lo <= hi:
        
        # Update the mid value
        mid = (lo + hi) // 2
        
        # Check the number of students required to allocate the books with the current maximum pages 
        
        # If it is less than or equal to k
        students = countStudents(arr, mid)
        
        # If it is greater than k
        if students > k:
            lo = mid + 1
        
        else:
            hi = mid - 1
    
    # Return the minimum number of pages that can be allocated to the students
    return lo

# Main Function
def main ():
    
    # Take User Input for the Size of the Array
    n = int (input ("Enter the Number of Books:\n"))
    
    # Take User Input for the Elements of the Array
    arr = list (map (int, input ("Enter the Pages of the Books:\n").split ()))
    
    # Take User Input for the Number of Students
    k = int (input ("Enter the Number of Students:\n"))
    
    # Print the minimum number of pages that can be allocated to the students
    print (f"The Minimum Number of Pages that can be Allocated to {k} students = {findPages(arr, k)}")

if __name__ == "__main__":
    main ()

# Sample Input / Output

"""
Input:

Enter the Number of Books:
n = 5

Enter the Pages of the Books:
arr = 25 46 28 49 24

Enter the Number of Students:
k = 4

Output:

The Minimum Number of Pages that can be Allocated to 4 students = 71
"""

# Link

"""
Access the Problem:-
    Take U Forward (TUF): https://takeuforward.org/plus/dsa/problems/book-allocation-problem
    Geeks For Geeks (GFG): https://www.geeksforgeeks.org/problems/allocate-minimum-number-of-pages0937/1
    Naukri Code 360 (Coding Ninjas): https://www.naukri.com/code360/problems/allocate-books_1090540

Article: https://takeuforward.org/data-structure/allocate-minimum-number-of-pages/
"""