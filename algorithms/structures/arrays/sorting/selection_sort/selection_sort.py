from algorithms.utils.swap import swap

def sort(arr):
    for i in range(len(arr)-1):
        minm = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[minm]:
                minm = j
        swap(arr, i, minm)