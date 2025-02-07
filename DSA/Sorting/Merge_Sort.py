# Merge Sort is a divide and conquer algorithm. It works by:
    # Splitting the array into two halves.
    # Recursively sorting both halves.
    # Merging the sorted halves back together.

# Steps:
    # If the array has only one element or is empty, return it (base case).
    # Divide the array into two halves.
    # Recursively sort each half.
    # Merge the two sorted halves.
    
#Time Complexity:O(n log(n))
    
# Code:

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2  # Find the middle point
    left_half = merge_sort(arr[:mid])  # Recursively sort left half
    right_half = merge_sort(arr[mid:])  # Recursively sort right half

    return merge(left_half, right_half)

def merge(left, right):
    sorted_arr = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1

    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])

    return sorted_arr

arr = list(map(int, input("Enter numbers separated by spaces: ").split()))
sorted_arr = merge_sort(arr)
print("Sorted array using Merge Sort:", sorted_arr)
