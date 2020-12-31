class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0: return 0
        if needle not in haystack: return -1
        m = len(haystack)
        n = len(needle)
        for i in range(m-n+1):
            if haystack[i: i+n] == needle:
                return i
        # if haystack == needle:
        #     return 0


print(Solution().strStr("hello", "ll"))
print(Solution().strStr("vvv", "vvvvvv"))
print(Solution().strStr("abc", "c"))