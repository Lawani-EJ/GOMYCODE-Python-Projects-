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
# def power(a, b):
#     return a ** b

# Bubble Sort 
# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n-1):
#         for j in range(0, n-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#     return arr

# Sample Data
# data = [29, 13, 22, 37, 52, 49, 46, 71, 56]
# sorted_data = bubble_sort(data)
# print(sorted_data)


# Merge Sort 
# def merge_sort(arr):
#     if len(arr) > 1:
#         mid = len(arr) // 2
#         L = arr[:mid]
#         R = arr[mid:]

#         merge_sort(L)
#         merge_sort(R)

#         i = j = k = 0

#         while i < len(L) and j < len(R):
#             if L[i] < R[j]:
#                 arr[k] = L[i]
#                 i += 1
#             else:
#                 arr[k] = R[j]
#                 j += 1
#             k += 1

#         while i < len(L):
#             arr[k] = L[i]
#             i += 1
#             k += 1

#         while j < len(R):
#             arr[k] = R[j]
#             j += 1
#             k += 1
#     return arr


# Quick Sort 
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     else:
#         pivot = arr[0]
#         less_than_pivot = [x for x in arr[1:] if x <= pivot]
#         greater_than_pivot = [x for x in arr[1:] if x > pivot]
#         return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)