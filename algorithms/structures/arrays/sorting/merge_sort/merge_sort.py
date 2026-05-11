def sort(arr):

    # base case
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = sort(arr[:mid])
    right = sort(arr[mid:])

    return merge(left, right)


def merge(l, r):
    i = j = 0
    result = []

    # merging left and right sorted subarrays
    while i < len(l) and j < len(r):
        if l[i] <= r[j]:
            result.append(l[i])
            i += 1
        else:
            result.append(r[j])
            j += 1
    
    # appending leftovers into the array
    while i < len(l):
        result.append(l[i])
        i += 1
    
    while j < len(r):
        result.append(r[j])
        j += 1
    
    return result