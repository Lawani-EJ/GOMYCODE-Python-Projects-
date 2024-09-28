# Binary search 
# defined a function binary_search with parameters (arr and x) 
def binary_search(arr, x):
    low = 0 #assigned low to 0
    high = len(arr) - 1 #assigned the length of the array subtracting / subtracted by 1 to high
    mid = 0 #assigned 0 to the medium

#a conditional loop is performed here:
# while the low variable is lesser than or equal to the high variable index 
    while low <= high:
        # therefore the medium will be assigned the operation highest added to the lowest divided by 2  
        mid = (high + low) // 2
        # if the middle variable index is less than x 
        if arr[mid] < x:  
            # the low variable index is going to store the operation of the middle index varaible plus 1 
            low = mid + 1
                    # else if the middle variable index is greater than x 
        elif arr[mid] > x:
            # the high variable indes is going to store the operation of the middle index variable minus 1 
            high = mid - 1
        else:
            # else if x is found it will return true 
            return True
                    # else if x is not found it will return false 
    return False

# Test array with the test cases
print(binary_search([1,2,3,5,8], 6)) # it should return False if 6 is not found eihter wise it will return False
print(binary_search([1,2,3,5,8], 5)) # it should return True if 5 is found eihter wise it will return False 


# Power Calculation 
# defined a function named power with parameters
def power(a, b):
    # and performed the power operation on these parameters 
    return a ** b

# Bubble Sort 
# defined the function and named it bubble_sort with an arr parameter 
def bubble_sort(arr):
    # gave n variable the length of the array 
    n = len(arr)
    # performed a loop from 0 to n-1
    for i in range(n-1):
        # performed a loop from 0 to n-2
        for j in range(0, n-i-1):
            # if the current element is greater than the next element then swap them
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Began Testing the  array with the test cases
# Sample Data
data = [29, 13, 22, 37, 52, 49, 46, 71, 56]
sorted_data = bubble_sort(data)
print(sorted_data)


# Merge Sort 
# defined the function and named it merge_sort with an arr parameter
def merge_sort(arr):
    # if the array has only one element then return the array
    if len(arr) > 1:
        # performed this operation to find the middle index of the array
        mid = len(arr) // 2
        # performed a loop from 0 to mid to store the left half of the array 
        L = arr[:mid]
        # performed a loop from mid to the end of the array to store the right half of the array
        R = arr[mid:]

        # called the merge_sort function on the left half of the array
        merge_sort(L)
        # called the merge_sort function on the right half of the array
        merge_sort(R)

        # performed a loop from 0 to the length of the left array to merge the left and right
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

# Began Testing the  array with the test cases
# Sample Data
data = [38, 27, 43, 3, 9, 82, 10]
sorted_data = merge_sort(data)
print("The Sorted data = ", sorted_data)

# Quick Sort 
# defined the function and named it quick_sort with an arr parameter
def quick_sort(arr):
    # if the array has only one element then return the array
    if len(arr) <= 1:
        return arr
    else:
        # perform this operation to find the middle index of the array
        pivot = arr[0]
        # performed a loop from 1 to the length of the array to store the elements less than
        less_than_pivot = [x for x in arr[1:] if x <= pivot]
        # performed a loop from 1 to the length of the array to store the elements greater than
        greater_than_pivot = [x for x in arr[1:] if x > pivot]
        return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)

# Began Testing the  array with the test cases
# Sample Data
data = [38, 27, 43, 3, 9, 82, 10]
sorted_data = quick_sort(data)
print("The Sorted data = ", quick_sort)