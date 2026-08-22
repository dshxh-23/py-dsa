from problems import solution

# ---- ---- ---- ----


@solution(
    problem = "leetcode #75: sort colors",
    solution_number = 1,
    approach = "two-pass partition",
    description = "",
    time = "O(n)",
    space = "O(1)",
    note = "",
)
def sortColors(nums: list[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """

    # arrange all 0's
    s = 0
    for f in range(len(nums)):
        if nums[f] == 0:
            nums[s], nums[f] = nums[f], nums[s]
            s += 1
        f += 1

    for f in range(s, len(nums)):
        if nums[f] == 1:
            nums[s], nums[f] = nums[f], nums[s]
            s += 1
        f += 1


# -- -- -- --


@solution(
    problem = "leetcode #75: sort colors",
    solution_number = 2,
    approach = "dutch national flag partition",
    description = "",
    time = "O(n)",
    space = "O(1)",
    note = "",
)
def sortColors_2(nums: list[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """

    low, curr, high = 0, 0, len(nums)-1

    while curr <= high:
        if nums[curr] == 0:
            nums[low], nums[curr] = nums[curr], nums[low]
            low += 1
            curr += 1

        elif nums[curr] == 1:
            curr += 1

        elif nums[curr] == 2:
            nums[curr], nums[high] = nums[high], nums[curr]
            high -= 1


# ---- ---- ---- ----


def main():
    ...

# -- -- -- --

main()