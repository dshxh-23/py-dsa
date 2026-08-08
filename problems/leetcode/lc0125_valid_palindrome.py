class Solution:
    def isPalindrome(self, s: str) -> bool:

        # making a new array with only alpha numeric chars
        new = []
        for i in s:
            if i.isalnum():
                new.append(i.lower())

        # checking if string is pallindrome or not
        for i in range( (len(new)-1)//2 + 1 ):
            if not new[i] == new[len(new)-1-i]:
                return False
        return True
    