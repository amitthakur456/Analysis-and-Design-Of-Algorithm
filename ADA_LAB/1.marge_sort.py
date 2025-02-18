# Function to merge two halves
def merge(left, right):
    merged = []
    i = j = 0

    # Merge the two sorted halves
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Append any remaining elements
    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged

# Recursive function for merge sort
def merge_sort(arr):
    # Base case: If the array has 1 or 0 elements, it's already sorted
    if len(arr) <= 1:
        return arr
    
    # Divide the array into two halves
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    # Recursively sort each half
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    # Merge the sorted halves
    return merge(left_sorted, right_sorted)

# Example array to be sorted
array = [38, 27, 43, 3, 9, 82, 10]

# Performing merge sort
sorted_array = merge_sort(array)

print("Sorted Array:", sorted_array)
