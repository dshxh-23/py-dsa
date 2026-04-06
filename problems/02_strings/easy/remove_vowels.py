def remove_vowels(s):
    vowels = "aeiou"
    result = "" 
    for ch in s:
        if ch.lower() not in vowels:
           result += ch

    return result

def main():
    print(remove_vowels("algorithm"))

if __name__ == "__main__":
    main()