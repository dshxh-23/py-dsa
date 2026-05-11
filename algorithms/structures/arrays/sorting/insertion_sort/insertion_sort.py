from algorithms.utils.swap import swap


def sort(arr):
    """
    self implementation of insertion sort
    can be optimized further
    NOT the ideal insertion sort, but works following the same principle, since written by me
    """
    
    def _insert(arr, insert_index):

        for i in range(insert_index, 0, -1):
            if arr[i] < arr[i-1]:
                swap(arr, i, i-1)
            else:
                break

    sorted_len = 1

    while sorted_len < len(arr):

        # insert next element to it's correnct position in sorted array
        _insert(arr, sorted_len)
        sorted_len += 1     # increment size of sorted array
    
    return
    

