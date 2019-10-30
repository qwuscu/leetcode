from typing import List


class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        n = len(S)
        res = [n] * n
        pos = -n
        for i in range(n):
            if S[i] == C:
                pos = i
            res[i] = i-pos
        for i in range(n-1, -1, -1):
            if S[i] == C:
                pos = i
            res[i] = min(res[i], abs(i-pos))
        return res


print(Solution().shortestToChar("loveleetcode", "e"))