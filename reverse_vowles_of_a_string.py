# 'str' object does not support item assignment in Python
# In Python, strings are immutable, so you can't change their characters in-place.
# str.lower() method

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ["a", "e", "i", "o", "u"]
        ls = list(s)
        i = 0
        j = len(s) - 1
        while i < j:
            if ls[i].lower() in vowels and ls[j].lower() in vowels:
                tmp = ls[i]
                ls[i] = ls[j]
                ls[j] = tmp
                i += 1
                j -= 1
            elif ls[i].lower() not in vowels:
                i += 1
            else:
                j -= 1
        return "".join(ls)


class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ["a", "e", "i", "o", "u"]
        stack = []
        for char in s:
            if char.lower() in vowels:
                stack.append(char)

        res = ""
        for i in range(len(s)):
            if s[i].lower() not in vowels:
                res += s[i]  # this works because it creates new str every iteration 
            else:
                res += stack.pop()
        return res
    # 72 ms, 14.8MB