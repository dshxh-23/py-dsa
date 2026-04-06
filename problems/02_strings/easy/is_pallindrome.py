def is_pallindrome(str):
    return True if str == str[::-1] else False 

def is_pallindrome_1(str):
    l = str[0]
    r = str[-1]

    while(l < r):
        if(str[l] != str[r]):
            return False
        
        l += 1
        r -= 1

    return True


def main():
    str1 = "madam"    
    str2 = "maadam"
    str3 = "racecar"
    print(is_pallindrome_1(str1))
    print(is_pallindrome_1(str2))
    print(is_pallindrome_1(str3))


if __name__ == "__main__":
    main()