from algorithms.utils.swap import swap

def sort(arr):
    low = 0
    high = len(arr) - 1

    def _recurse(low, high):
        if low < high:
            pivot_index = partition(arr, low, high)

            _recurse(arr, low, pivot_index-1)
            _recurse(arr, pivot_index+1, high)
    
    _recurse(low, high)


def partition(arr, low, high):

    # last element is the pivot
    pivot = arr[high]

    # initializing i
    i = low-1

    # traversing through the array
    for j in range(low, high):

        # if current element is smaller then pivot:
        if arr[j] < pivot:
            i += 1
            swap(arr, i, j)
        
    swap(arr, i+1, high)
    pivot_index = i+1

    return pivot_index