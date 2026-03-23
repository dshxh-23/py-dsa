def remove_duplicates(s):
    str_list = []
    for c in s:
        if c not in str_list:
            str_list.append(c)
    
    return str.join("", str_list)



def main():
    str1 = "programming"
    str2 = "hello, there"
    print(remove_duplicates(str1))
    print(remove_duplicates(str2))



if __name__ == "__main__":
    main()