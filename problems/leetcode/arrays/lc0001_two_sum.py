from problems import solution

# ---- ---- ---- ----


@solution(
    problem = "leetcode #1: two sum",
    solution_number = 1,
    approach = "brute force",
    description = "",
    time = "O(n^2)",
    space = "O(1)",
    note = "",
)
def twoSum(nums: list[int], target: int) -> list[int]:
    for i, num in enumerate(nums):
        if (target-num) in nums[i+1:]:
            nums.remove(num)
            return [i, nums.index(target-num)+1]


# -- -- -- --


@solution(
    problem = "leetcode #1: two sum",
    solution_number = 2,
    approach = "one-pass hash map",
    description = "",
    time = "O(n)",
    space = "O(n)",
    note = "dict in python is implemented as a hash table, so lookup only takes O(1) time.",
)
def twoSum_2(nums: list[int], target: int) -> list[int]:

    # lookup in python dict takes O(1) time (cause it's implemented using hash tables).
    seen = {}   # num : index

    for i in range(len(nums)):
        num = nums[i]
        complement = target-num

        # check if complement already exists
        if complement in seen:
            return (seen[complement], i)

        # else insert num to seen
        seen[num] = i


# ---- ---- ---- ----


def main():
    ...

# -- -- -- --

main()



class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for i, num in enumerate(nums):
            if (target-num) in nums[i+1:]:
                nums.remove(num)
                return [i, nums.index(target-num)+1]