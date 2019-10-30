from typing import List


class Solution:
    # 将字符串按正、逆顺序两次扫描，第一次扫描计算当前位置字母与前一个目标字母之间的距离，
    # 后一次扫描计算当前位置字母与后一个字母之间的距离，两者取小即可。
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