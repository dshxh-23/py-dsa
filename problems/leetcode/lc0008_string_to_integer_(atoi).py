def myAtoi(self, s: str) -> int:
        
    # remove leading and trailing whitespaces
    s = s.strip()

    # return 0 for empty sting
    if not s:
        return 0

    # handing signedness
    neg = False
    if s[0] == "+" or s[0] == "-":
        if s[0] == "-":
            neg = True
        s = s[1:]

    # convert string to int
    num = 0
    for char in s:
        try:
            num = num*10 + int(char)
        
        # stop when encounter NaN
        except ValueError:
            break
        
    # correction for negative integer
    if neg:
        num *= -1
    
    # rounding and returning integer
    if (num < -2**31):
        return -2**31
    elif (num > 2**31-1):
        return 2**31-1
    else:
        return num