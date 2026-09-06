from problems import solution

# ---- ---- ---- ----


@solution(
    problem = "leetcode #209: minimum size subarray sum",
    solution_number = 1,
    approach = "brute force",
    time = "O(n^2)",
    space = "O(1)",
    description = "",
    note = "approach fails in leetcode due to TLE",
)
def minSubArrayLen_1(target: int, nums: list[int]) -> int:

    minm_len = float('inf')
    curr_sum = 0
    curr_len = 0    # also possible to replace curr_len with j-i+1
    
    for i in range(len(nums)):

        for j in range(i, len(nums)):
            curr_sum += nums[j]
            curr_len += 1
            if curr_sum >= target and curr_len < minm_len:
                minm_len = curr_len

        curr_sum = 0
        curr_len = 0

    return minm_len if minm_len != float('inf') else 0


@solution(
    problem = "leetcode #209: minimum size subarray sum",
    solution_number = 2,
    approach = "sliding window",
    time = "O(n)",
    space = "O(1)",
    description = "",
    note = "Optimal Approach",
)
def minSubArrayLen_2(target: int, nums: list[int]) -> int:

    left = 0
    right = 0

    min_len = float('inf')
    curr_sum = 0

    while right < len(nums):

        curr_sum += nums[right]

        while curr_sum >= target:
            min_len = min(min_len, right-left+1)
            curr_sum -= nums[left]
            left += 1

        right += 1

    return min_len if min_len != float('inf') else 0


# ---- ---- ---- ----


def main():

   tests = [
       (7, [2,3,1,2,4,3]),
       (4, [1,4,4]),
       (11, [1,1,1,1,1,1,1,1]),
   ]

   for test in tests:
       print(f"Target: {test[0]}  |  Array: {test[1]}")
       print(f"Output:\t{minSubArrayLen_2(*test)}")
       print()

# -- -- -- --

main()