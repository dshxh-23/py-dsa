def count_vowels(s):
    vowels = "aeiou"
    count = 0

    for c in s:
        if c.lower() in vowels:
            count += 1
        
    return count



def main():
   str1 = "Hello, World!"
   str2 = "ths ln cntns n vwls"
   print(count_vowels(str1))
   print(count_vowels(str2))



if __name__ == "__main__":
    main()