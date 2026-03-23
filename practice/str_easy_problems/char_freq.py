def char_freq(str):
    freq = {}

    for ch in str:
        if ch not in freq:
            freq[ch] = 1
        else:
            freq[ch] += 1

    return freq 



def main():
    str1 = "aldfgfvear"
    str2 = "shfierlfqwerfsihvhwrawfhdscaiuw"
    print(char_freq(str1))
    print(char_freq(str2))


if __name__ == "__main__":
    main()