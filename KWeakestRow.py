from typing import List

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        m = len(mat)
        lookup = {}
        for i in range(m):
            lookup[i] = sum(mat[i])
        res = {k: lookup[k] for k in sorted(lookup, key=lookup.get)}
        return list(res.keys())[:k]

# this is not accepted solution, failed at 3rd test case on below
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        # 设置指针在每列遍历每行数组
        # 首选遇到0的数组所在行号加入result列表中，
        # 直到找到第k个结束遍历
        result = []
        for j in range(len(mat[0])):
            for i in range(len(mat)):
                if k > 0:
                    if mat[i][j] == 0 and i not in result:
                        k -= 1
                        result.append(i)
                else:
                    return result
        if k != 0:
            return [i for i in range(k)]


print(Solution().kWeakestRows([[1,0,0,0],[1,1,1,1],[1,0,0,0],[1,0,0,0]],2))
print(Solution().kWeakestRows([[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]], 3))
print(Solution().kWeakestRows([[1,0],[1,0],[1,0],[1,1]], 4))
