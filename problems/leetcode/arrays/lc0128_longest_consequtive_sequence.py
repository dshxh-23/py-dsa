from problems import solution

# ---- ---- ---- ----


@solution(
    problem = "leetcode #128: longest consequtive sequence",
    solution_number = 1,
    approach = "sorting",
    time = "O(n log n)",
    space = "O(n)",
    description = "",
    note = "",
)
def longestConsecutive_1(nums: list[int]) -> int:
    nums.sort()

    curr_streak = 1
    max_streak = 0

    for i in range(len(nums)-1):

        if nums[i+1] - nums[i] == 1:
            curr_streak += 1

        elif nums[i] != nums[i+1]:
            max_streak = max(curr_streak, max_streak)
            curr_streak = 0

    # to handle the case where the last non-terminated streak is the max streak
    return max(max_streak, curr_streak)
        
# -- -- -- --


@solution(
    problem = "leetcode #128: longest consequtive sequence",
    solution_number = 2,
    approach = "hash set",
    time = "O(n)",
    space = "O(n)",
    description = "",
    note = "Lookup in hash set takes O(1) time.",
)
def longestConsecutive_2(nums: list[int]) -> int:

    # convert to hash set for O(1) lookup
    n_set = set(nums)
    max_streak = 0

    # traverse the hashset
    for num in n_set:

        # encountered chain leader (1st member of chain)
        if num-1 not in n_set:
            curr_streak = 1 
            curr_val = num+1

            # find subsequent members of chain and count streak
            while curr_val in n_set:
                curr_streak += 1
                curr_val += 1

            max_streak = max(curr_streak, max_streak)

    return max_streak
                


# ---- ---- ---- ----


def main():
   tests = [
       [100,4,200,1,3,2],
       [0,3,7,2,5,8,4,6,0,1],
       [1,0,1,2]
   ]

   for test in tests:
       print(f"Input:\t{test}\nOutput:\t{longestConsecutive_1(test)}\n")

# -- -- -- --

main()