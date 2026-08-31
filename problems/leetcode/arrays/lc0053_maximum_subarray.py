from problems import solution

# ---- ---- ---- ----


@solution(
    problem = "leetcode #53: maximum subarray",
    solution_number = 1,
    approach = "optimized brute force",
    time = "O(n^2)",
    space = "O(1)",
    description = "",
    note = "Not accepted in leetcode due to time limit exceeded error",
)
def maxSubArray(nums: list[int]) -> int:

    if not nums:
        return 0

    # initializing initial largest sum
    largest = nums[0]
    curr = 0

    # looping through the entire array
    for i in range(len(nums)):

        # check all possible subarrays with ith element
        for j in range(i, len(nums)):
            curr += nums[j]
            if curr > largest:
                largest = curr

        # reinitializing curr for subarrays with (i+1)th element
        curr = 0

    return largest
    
# -- -- -- --


@solution(
    problem = "leetcode #53: maximum subarray",
    solution_number = 2,
    approach = "divide and conquer",
    description = "",
    time = "O(n log n)",
    space = "O(log n)",
    note = "",
)
def maxSubArray_2(nums: list[int]) -> int:

    def middle_sum(l, m, r):

        curr = 0
        l_maxm = float('-inf')
        r_maxm = float('-inf')

        # maxm sum on left side
        for idx in range(m, l-1, -1):
            curr += nums[idx]
            if curr > l_maxm:
                l_maxm = curr

        curr = 0

        # max sum on right side
        for idx in range(m+1, r+1):
            curr += nums[idx]
            if curr > r_maxm:
                r_maxm = curr

        return (l_maxm + r_maxm)


    def find_max(l, r):

        # base case
        if l == r:
            return nums[l]

        m = (l+r) // 2

        # recurrence relation
        return max(find_max(l, m), find_max(m+1, r), middle_sum(l, m, r))

    return find_max(0, len(nums)-1)

# -- -- -- --

@solution(
    problem = "leetcode #53: maximum subarray",
    solution_number = 3,
    approach = "dynamic programming (tabular method)",
    time = "O(n)",
    space = "O(n)",
    description = "",
    note = "",
)
def maxSubArray_3(nums: list[int]) -> int:
    ...


# -- -- -- --

@solution(
    problem = "leetcode #53: maximum subarray",
    solution_number = 4,
    approach = "Kadane's algorithm (dynamic programming)",
    time = "O(n)",
    space = "O(1)",
    description = "Uses Kadane's algorithm can find the maxm subarray sum in one-pass of the array. The key point of the algorithms is during traversal, curr represents the maximum subarray sum which has curr as the last element. we store the maximum sum and whenever curr is less then 0, we know that it won't contribute to the next maximum sum of the next subarray and hence, we reset it to 0.",
    note = "While kadane's algorithm is the optimal approach and has better theoretical time complexity, it is a sequential algorithm and cannot be parallelized. Compared to this, the divide and conquer approach is a parallelizable, and hence, might actually outperform kadane's algorithm in very large datasets by utilizing mulit-core CPUs.",
)
def maxSubArray_4(nums: list[int]) -> int:

    max_sum = nums[0]
    curr = 0

    for num in nums:
        curr += num

        if curr > max_sum:
            max_sum = curr
        
        if curr < 0:
            curr = 0

    return max_sum


# ---- ---- ---- ----

def main():
    tests = [
        [-2,1,-3,4,-1,2,1,-5,4],
        [1],
        [5,4,-1,7,8],
    ]

    for test in tests:
        print(f"Input: {test}\nOutput:\t{maxSubArray_2(test)}")
        print()

# -- -- -- --

main()