def fib(self, n: int) -> int:

    def recurse(n):
        if n == 0 or n == 1:
            return n
        return recurse(n-1) + recurse(n-2)
    
    return recurse(n)