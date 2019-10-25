from typing import List


class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        m, n = len(M), len(M[0])
        result = [[0] * n for _ in M]

        for i in range(m):
            for j in range(n):
                value, count = M[i][j], 1
                if i - 1 >= 0:
                    value += M[i - 1][j]
                    count += 1
                    if j - 1 >= 0:
                        value += M[i - 1][j - 1]
                        count += 1
                    if j + 1 < n:
                        value += M[i - 1][j + 1]
                        count += 1
                if i + 1 < m:
                    value += M[i + 1][j]
                    count += 1
                    if j - 1 >= 0:
                        value += M[i + 1][j - 1]
                        count += 1
                    if j + 1 < n:
                        value += M[i + 1][j + 1]
                        count += 1
                if j - 1 >= 0:
                    value += M[i][j - 1]
                    count += 1
                if j + 1 < n:
                    value += M[i][j + 1]
                    count += 1
                result[i][j] = value // count
        return result


print(Solution().imageSmoother([[2,3,4],[5,6,7],[8,9,10],[11,12,13],[14,15,16]]))
# print(Solution().imageSmoother([[1,1,1],[1,0,1],[1,1,1]]))


class Solution(object):
    def imageSmoother(self, M):
        R, C = len(M), len(M[0])
        ans = [[0] * C for _ in M]

        for r in xrange(R):
            for c in xrange(C):
                count = 0
                for nr in (r-1, r, r+1):
                    for nc in (c-1, c, c+1):
                        if 0 <= nr < R and 0 <= nc < C:
                            ans[r][c] += M[nr][nc]
                            count += 1
                ans[r][c] /= count

        return ans