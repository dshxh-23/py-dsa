from core.decorators.solution import solution

@solution("Leetcode #509: Fibonacci Number", 1, "recursion")
def fib(n: int) -> int:

    def recurse(n):
        if n == 0 or n == 1:
            return n
        return recurse(n-1) + recurse(n-2)
    
    return recurse(n)

if __name__ == "__main__":
    print(fib(7))