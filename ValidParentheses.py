class Solution:
    def isValid(self, s: str) -> bool:
        lookup = {"(":")", "{":"}", "[":"]"}
        stack = []
        for char in s:
            if char in lookup:
                stack.append(char)
            else:
                if len(stack) > 0 and lookup[stack[-1] ]== char:
                    stack.pop()
                else:
                    return False
        return len(stack)==0


print(Solution().isValid("()"))