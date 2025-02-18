Merge Sort Algorithm
Merge Sort is a Divide and Conquer algorithm that recursively splits an array into two halves, sorts each half, and then merges the sorted halves to produce a final sorted array. It has a time complexity of O(n log n) in the worst, average, and best cases, making it highly efficient for large datasets.

Algorithm Steps:

Divide: Split the array into two halves.
Conquer: Recursively sort each half.
Combine: Merge the two sorted halves into a single sorted array.
Merge Function:
The merge function is responsible for combining two sorted arrays. It compares the elements of both arrays and places them in the correct order to form a single sorted array.

Time Complexity:

Best Case: O(n log n)
Average Case: O(n log n)
Worst Case: O(n log n)
Space Complexity:

O(n) due to the extra space used for storing the merged arrays during the sorting process.
