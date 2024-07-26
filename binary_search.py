def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        
        # Check if target is present at mid
        if arr[mid] == target:
            return mid
        
        # If target is greater, ignore left half
        elif arr[mid] < target:
            left = mid + 1
        
        # If target is smaller, ignore right half
        else:
            right = mid - 1
    
    # If we reach here, then the element was not present
    return -1

# Example usage:
# sorted_array = [1, 3, 5, 7, 9, 11, 13, 15, 17]
# target = 7
# result = binary_search(sorted_array, target)
# if result != -1:
#     print(f"Element is present at index {result}")
# else:
#     print("Element is not present in array")