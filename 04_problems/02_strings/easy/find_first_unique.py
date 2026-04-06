def find_first_unique(s):
    """Returns the 1st unique (non-repeating) character of a string"""
    
    freq = {}
    for c in s:
        freq[c.lower()] = freq.get(c.lower(), 0) + 1

    for key in freq:
        if freq[key] == 1:
            return key



def main():
    print(find_first_unique("swiss"))   
    print(find_first_unique("Hello, there"))   


if __name__ == "__main__":
    main()