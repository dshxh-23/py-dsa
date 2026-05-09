def binary_search(arr, target):
    """array must be sorted"""

    low = 0
    high = len(arr) - 1

    while low < high:
        mid = (low + high) // 2

        if target == arr[mid]:
            return mid
        
        elif target < arr[mid]:
            high = mid - 1
        
        else:
            low = mid + 1
    
    return -1