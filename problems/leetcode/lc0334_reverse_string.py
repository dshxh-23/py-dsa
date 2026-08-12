from core.decorators.solution import solution


@solution("Reverse String", 1, "looping")
def reverseString(s: list[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    left = 0
    right = len(s)-1

    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    

@solution("Reverse String", 2, "recursion")
def reverseString_1(s: list[str]) -> None:

    def recurse(left, right, arr):
        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
            recurse(left+1, right-1, arr)

    recurse(0, len(s)-1, s)
