from problems import solution

# ---- ---- ---- ----


@solution(
    problem = "leetcode #189: rotate array",
    solution_number = 1,
    approach = "brute force",
    time = "O(nk)",
    space = "O(1)",
    note = "fails leetcode test case 9 due to time limit exceeded."
)
def rotate(nums: list[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """

    k = k % len(nums)
    
    for _ in range(k):
        for i in range(len(nums)-1, 0, -1):
            nums[i], nums[i-1] = nums[i-1], nums[i]

# -- -- -- --

@solution(
    problem = "leetcode #189: rotate array",
    solution_number = 2,
    approach = "list slicing and concatenation",
    time = "O(n)",
    space = "O(n)"
)
def rotate_2(nums: list[int], k: int) -> None:

    # reducing k
    n = len(nums)
    k %= n

    # 
    nums[:] = nums[-k:] + nums[:-k]

# -- -- -- --

@solution(
    problem = "leetcode #189: rotate array",
    solution_number = 3,
    approach = "array reversal algorithm",
)
def rotate_3(nums: list[int], k: int) -> None:

    n = len(nums)

    # handle cases where k>nums
    k %= n

    # helper function to reverse part of array in-place
    def reverse(start: int, stop: int) -> None:
        while start < stop:
            nums[start], nums[stop] = nums[stop], nums[start]
            start += 1
            stop -= 1

    # array reversal algorithm to rotate array
    reverse(0, n-1)
    reverse(0, k-1)
    reverse(k, n-1)

# -- -- -- --

@solution(
    problem = "leetcode #189: rotate array",
    solution_number = 4,
    approach = "extra array mapping",
    description = "using pattern to find exact position of elements."
)
def rotate_4(nums: list[int], k: int) -> None:

    # reducing k
    n = len(nums)
    k %= n

    # copying list
    arr = nums.copy()

    # rotate
    for i in range(n):
        nums[i] = arr[(i-k) % n]

# ---- ---- ---- ----


def main():
    tests = [
        ([1,2,3,4,5,6,7], 3),
        ([-1,-100,3,99], 2),
    ]

    for test in tests:
        print(f"Original:\t{test[0]}")
        rotate_2(*test)
        print(f"Rotated by {test[1]}:\t{test[0]}")
        print()



# -- -- -- --

main()