from problems import solution

# ---- ---- ---- ----


@solution(
    problem = "leetcode #9: palindrome number",
    solution_number = 1,
    approach = "two pointer",
)
def isPalindrome(x: int) -> bool:
    x_str = str(x)
    return x_str == x_str[::-1]

# -- -- -- --

@solution(
    problem = "leetcode #9: palindrome number",
    solution_number = 2,
    approach = "construct reverse number and compare with original",
)
def isPalindrome_2(x: int) -> bool:

    # negative numbers and numbers ending in 0 (except 0) are not palindrome
    if (x < 0) or (x%10 == 0 and x != 0):
        return False

    reversed_half = 0
    while reversed_half < x:
        reversed_half = reversed_half*10 + x%10
        x //= 10

    # check condition for both even digit and odd digit numbers
    return x == reversed_half or x == reversed_half // 10
    

# ---- ---- ---- ----

def main():
    x1 = 121
    x2 = 1221
    x3 = 10000
    x4 = -39
    x5 = 583
    print(isPalindrome_2(x1))
    print(isPalindrome_2(x2))
    print(isPalindrome_2(x3))
    print(isPalindrome_2(x4))
    print(isPalindrome_2(x5))

main()