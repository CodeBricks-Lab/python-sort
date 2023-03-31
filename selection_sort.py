'''
This algorithm works by iteratively selecting the smallest element from the unsorted portion of the list and swapping it with the leftmost unsorted element, effectively building up the sorted portion of the list from left to right. The min_idx variable keeps track of the index of the smallest element found in each iteration of the outer loop.
'''

def selection_sort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Find the minimum element in remaining
        # unsorted array
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Swap the found minimum element with
        # the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = selection_sort(arr)
print(sorted_arr) # [11, 12, 22, 25, 34, 64, 90]

