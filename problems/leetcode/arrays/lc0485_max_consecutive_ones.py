from problems import solution

# ---- ---- ---- ----


@solution(
    problem = "leetcode 0485: max consecutive ones",
    solution_number = 1,
    approach = "",
    description = "",
    time = "O(n)",
    space = "O(1)",
    note = "",
)
def findMaxConsecutiveOnes(nums: list[int]) -> int:
    ones = 0
    curr = 0

    for i in range(len(nums)):

        # break streak
        if nums[i] == 0:
            if curr > ones:
                ones = curr
            curr = 0

        # increment streak
        elif nums[i] == 1:
            curr += 1

            # handle for edge case where last element is 1
            if i == len(nums)-1 and curr > ones:
                ones = curr

    return ones

# ---- ---- ---- ----


def main():
    tests = [
        [1,1,0,1,1,1],
        [1,0,1,1,0,1]
    ]

    for test in tests:
        print(f"array: {test}\nresult: {findMaxConsecutiveOnes(test)}")

# -- -- -- --

main()