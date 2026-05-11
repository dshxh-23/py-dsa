from algorithms.utils.swap import swap

def sort(arr, reverse=False):
    """in-place sorting using bubble sort"""

    for i in range(len(arr)):
        for j in range(0, len(arr)-i-1):
            
            if reverse:
                if arr[j] < arr[j+1]:
                    swap(arr, j, j+1)
            else:
                if arr[j] > arr[j+1]:
                    swap(arr, j, j+1)

    return