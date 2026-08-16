from problems import solution

@solution(
    "leetcode #26: remove duplicates from sorted array",
    1,
    approach = "brute force"
)
def removeDuplicates(nums: list[int]) -> int:

    uniques = 0
    i = 0

    for _ in range(len(nums)-1):

        # duplicate: delete it but do not move pointer ahead 
        if nums[i] == nums[i+1]:
            nums.pop(i+1)

        # different: move the pointer ahead
        else:
            i += 1
            uniques += 1

    return uniques+1

# -- -- -- --

def removeDuplicates_1(nums: list[int]) -> int:

    slow, fast = 0, 1

    # iterate untill end of array
    while fast < len(nums):

        # case 1: duplicate value
        if nums[slow] == nums[fast]:
            fast += 1

        # case 2: unique value
        else:
            slow += 1
            nums[slow] = nums[fast]
            fast += 1

    return slow+1


# ---- ---- ---- ----

def main():
    tests = [
        [1,1,2],
        [0,0,1,1,1,2,2,3,3,4],
    ]
    for test in tests:
        print(removeDuplicates_1(test))
    print(tests)

# -- -- -- --

main()