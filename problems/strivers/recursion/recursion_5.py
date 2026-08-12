from core.decorators.solution import solution

@solution("Reverse an array", 1, "recursion")
def reverse(self, arr: list, n: int) -> None:
    left = 0
    right = len(arr)-1
    def recurse(first, last, arr):
        if not left < right:
            return
        arr[left], arr[right] = arr[right], arr[left]
        recurse(left+1, right-1, arr)

    recurse(left, right, arr)