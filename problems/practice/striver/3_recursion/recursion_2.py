from core.decorators.solution import solution

@solution("Print N to 1 using Recursion", 1, "recursion")
def printNumbers(n):
    
    def recurse(x):
        if x == 1:
            print(x)
            return
        
        else:
            print(x)
            recurse(x-1)
    
    recurse(n)
    