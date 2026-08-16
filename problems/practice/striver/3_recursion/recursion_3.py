from core.decorators.solution import solution

@solution("Sum of First N Numbers", 1, "recursion")
def NnumbersSum(N):
    sum = [0]

    def recurse(x):
        if x < 1:
            return 0
        
        sum[0] += x
        recurse(x-1)

    recurse(N)
    return sum[0]
    