
'''
This algorithm works by iteratively inserting elements from the unsorted portion of the list into their correct position in the sorted portion of the list. The key variable represents the current element being sorted, and the while loop moves all elements greater than key one position to the right, until key is in its correct position.
'''


def insertion_sort(arr):
    n = len(arr)
    # Traverse through 1 to len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key
    return arr

arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = insertion_sort(arr)
print(sorted_arr) # [11, 12, 22, 25, 34, 64, 90]
