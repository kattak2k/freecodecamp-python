def selection_sort(arr):
    n = len(arr)
    # 1. Outer loop to move the boundary of the unsorted sublist
    for i in range(n - 1):
        # 2. Assume the current position is the minimum
        min_idx = i
        
        # 3. Inner loop to find the actual minimum in the unsorted portion
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
                
        # 4. Swap the found minimum element with the first unsorted element
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            
    return arr


# 7. selection_sort([33, 1, 89, 2, 67, 245]) should return [1, 2, 33, 67, 89, 245].
# 8. selection_sort([5, 16, 99, 12, 567, 23, 15, 72, 3]) should return [3, 5, 12, 15, 16, 23, 72, 99, 567].
# 9. selection_sort([1, 4, 2, 8, 345, 123, 43, 32, 5643, 63, 123, 43, 2, 55, 1, 234, 92]) should return [1, 1, 2, 2, 4, 8, 32, 43, 43, 55, 63, 92, 123, 123, 234, 345, 5643]
