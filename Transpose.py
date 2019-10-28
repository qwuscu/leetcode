from typing import List


class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        # time: O(R*C), where RR and CC are the number of rows and columns in the given matrix A.
        # space: O(R*C), the space used by the answer.
        r = len(A)
        c = len(A[0])
        res = [[None] * r for _ in range(c)]
        for i in range(c):
            for j in range(r):
                res[i][j] = A[j][i]
        return res



print(Solution().transpose([[1,2,3],[4,5,6]]))