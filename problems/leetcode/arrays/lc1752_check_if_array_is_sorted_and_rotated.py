from problems import solution

# ---- ---- ---- ----


@solution(
    problem = "leetcode #1752: check if array is sorted and rotated",
    solution_number = 1,
    approach = "pattern",
    description = "array is sorted and rotated if its value decreases between 2 consecutive elements atmost once. This also includes checking for last and first element."
)
def check(nums: list[int]) -> bool:
    counts = 0

    # count decreases between 1st and last element 
    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            counts += 1

    # check if no. decreases from last to first element
    if nums[len(nums)-1] > nums[0]:
        counts += 1

    # array is sorted and rotated only if count decreases atmost once.
    return False if counts > 1 else True

# -- -- -- --
