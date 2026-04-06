"""
2 String are anagrams if they contain the same characters, but in different order.

For e.g., silent and listen are anagrams.
"""

def is_anagram(str1, str2):
    # here, using a set is wrong. This is because a string can contain multiple occurances of same character and a set will treat it as the same
    # i.e., ABCC and ABC are not anagrams. But using set will result in true here.
    return True if sorted(str1) == sorted(str2) else False


# Method 2 - usign frequency-count approach
def is_anagram_1(str1, str2):
    if len(str1) != len(str2):
        return False

    freq = {}
    for ch in str1:
        freq[ch] = freq.get(ch, 0) + 1

    for ch in str2:
        if ch not in freq or freq[ch] == 0:
            return False
        else:
            freq[ch] -= 1
        
        return True



def main():
    print(is_anagram_1("sillent", "llisten"))
    print(is_anagram_1("silen", "listen"))



if __name__ == "__main__":
    main()