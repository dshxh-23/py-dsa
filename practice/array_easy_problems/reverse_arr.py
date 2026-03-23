# Method 1: using an extra list
def reverse_list(arr):
    left = 0
    right = len(arr) - 1
    reverse_list = []

    while(right >= left):
        reverse_list.append(arr[right])
        right -= 1

    return reverse_list



# Method 2: slicing (python specific)
def reverse_list_1(arr):
    reversed_list = arr[::-1]


# Method 3: In-place reversal
def reverse_list_2(arr):
    left = 0
    right = len(arr)-1
    while(left < right):
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr


def main():
    arr = [19, 38, 42, 21, 39, 183, 48]
    print(reverse_list_2(arr))


if __name__ == "__main__":
    main()