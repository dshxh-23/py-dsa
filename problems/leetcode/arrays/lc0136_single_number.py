from problems import solution

# ---- ---- ---- ----


@solution(
    problem = "leetcode #136: single number",
    solution_number = 1,
    approach = "",
    description = "",
    time = "O(n)",
    space = "O(n)",
    note = "solution is accepted, but does not work on constant extra space, as mentioned in leetcode.",
)
def singleNumber(nums: list[int]) -> int:
    if not nums:
        return 0

    visited = []
    for num in nums:
        if num not in visited:
            visited.append(num)
        else:
            visited.remove(num)
    return visited[0]


# -- -- -- --


@solution(
    problem = "leetcode #136: single number",
    solution_number = 2,
    approach = "bitwise XOR",
    description = "",
    time = "O(n)",
    space = "O(1)",
    note = "",
)
def singleNumber_2(nums: list[int]) -> int:
    result = 0
    for num in nums:
        result ^= num
    return result



# ---- ---- ---- ----


def main():
    tests = [
        [2,2,1],
        [4,1,2,1,2],
        [1],
    ]

    for test in tests:
        print(f"test:\t{test}\nresult:\t{singleNumber(test)}")

# -- -- -- --

main()