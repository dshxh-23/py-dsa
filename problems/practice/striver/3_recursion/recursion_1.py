from core.decorators.solution import solution

@solution("Print 1 to N using using Recursion", 1, "recursive")
def printNumbers(n):
    def recurse(n):
        if n==1:
            print(1)
            return
        else:
            recurse(n-1)
            print(n)
    
    recurse(n)
