class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0
        for i in range(n):
            for j in range(i + 1, n+1):
                if self.helper(s, i, j):
                    ans = max(ans, j - i)
        return ans

    def helper(self, s, i, j):
        unique = set()
        for x in range(i, j):
            if s[x] in unique:
                return False
            unique.add(s[x])
        return True


if __name__ == "__main__":
    print(Solution().lengthOfLongestSubstring(" "))
    print(Solution().lengthOfLongestSubstring("abcabcbb"))