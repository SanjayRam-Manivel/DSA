#Quick Sort is also a divide and conquer algorithm. It works by:
    # Selecting a pivot element.
    # Partitioning the array so that elements smaller than the pivot go to the left, and elements greater go to the right.
    #Recursively sorting the left and right subarrays.

# Steps:
    # Pick a pivot (e.g., last element, first element, or random).
    # Partition the array into:
        # Left: Elements smaller than the pivot.
        # Right: Elements greater than the pivot.
    # Recursively apply Quick Sort to both partitions.
    # Combine sorted partitions.
    
#Time Complexity:O(n^2)

#Code:

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]  # Choose the middle element as pivot
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

arr = list(map(int, input("Enter numbers separated by spaces: ").split()))
sorted_arr = quick_sort(arr)
print("Sorted array using Quick Sort:", sorted_arr)
