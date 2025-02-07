#Selection Sort works by repeatedly selecting the smallest element from the unsorted portion of the array and swapping it with the first unsorted element.
# This process is repeated until the entire array is sorted.

#Steps:
    # Find the smallest element in the array.
    # Swap it with the first unsorted element.
    # Move to the next position and repeat the process.
    # Continue until the entire array is sorted.
    
#TimeComplexity : O(n^2)

#Code:

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

arr = list(map(int, input("Enter numbers separated by spaces: ").split()))
selection_sort(arr)
print("Sorted array using Selection Sort:", arr)
