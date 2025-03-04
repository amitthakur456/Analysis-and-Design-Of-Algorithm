def partition(arr, low, high):
    pivot = arr[high]  # Last element as pivot
    i = low - 1  # Pointer for smaller element
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap elements
    arr[i+1], arr[high] = arr[high], arr[i+1]  # Swap pivot to correct position
    return i+1

def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)  # Find pivot index
        quick_sort(arr, low, pi-1)  # Sort left part
        quick_sort(arr, pi+1, high)  # Sort right part

# Example usage
arr = [7, 2, 1, 6, 8, 5, 3, 4]
quick_sort(arr, 0, len(arr) - 1)
print(arr)  
