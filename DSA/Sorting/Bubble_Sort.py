#Bubble Sort works by repeatedly swapping adjacent elements if they are in the wrong order. 
# The largest element "bubbles up" to its correct position in each pass.

# Steps:
    # Compare adjacent elements and swap if the first is greater than the second.
    # Repeat this process for all elements.
    # After each pass, the largest element moves to its correct position.
    # Continue until the array is sorted.
    
#Time Complexity: O(n^2)

#Code:

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

arr = list(map(int, input("Enter numbers separated by spaces: ").split()))
bubble_sort(arr)
print("Sorted array using Bubble Sort:", arr)
