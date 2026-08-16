from problems import solution

# ---- ---- ---- ----


@solution(
    problem = "leetcode #283: move zeroes",
    solution_number = 1,
    approach = "two-pointer swap",
    description = "",
    time = "O(n)",
    space = "O(1)",
    note = "",
)
def moveZeroes(nums: list[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1


# -- -- -- --


@solution(
    problem = "leetcode #283: move zeroes",
    solution_number = 2,
    approach = "extra array",
    description = "",
    time = "O(n)",
    space = "",
    note = "",
)
def moveZeroes_2(nums: list[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    curr_idx = 0
    for num in nums:
        if num != 0:
            nums[curr_idx] = num
            curr_idx += 1
    for i in range(curr_idx, len(nums)):
        nums[i] = 0


# ---- ---- ---- ----


def main():
    tests = [
        [0,1,0,3,12],
        [0],
    ]

    # -- --

    for test in tests:
        print(f"Original:\t{test}")
        moveZeroes(test)
        print(f"Solved:\t\t{test}")

# -- -- -- --

main()