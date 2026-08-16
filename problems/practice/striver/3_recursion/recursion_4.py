from core.decorators.solution import solution

@solution("Factorial of a given number", 1, "recursion")
def factorial(n):

    def recurse(x):
        if x == 0 or x == 1:
            return 1
        return x * recurse(x-1)

    return recurse(n)
