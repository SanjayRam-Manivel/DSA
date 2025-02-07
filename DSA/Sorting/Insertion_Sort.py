#Insertion Sort works by taking one element at a time and inserting it into its correct position relative to the sorted part of the array.

# Steps:
    # Consider the first element as sorted.
    # Take the next element and place it in the correct position within the sorted part.
    # Repeat for all elements.

#Time Complexity: O(n^2)

#Code:

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

arr = list(map(int, input("Enter numbers separated by spaces: ").split()))
insertion_sort(arr)
print("Sorted array using Insertion Sort:", arr)
