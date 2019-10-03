from typing import List


class Solution:
    #time: O(NlogN), space: O(N)
    def sortedSquares(self, A: List[int]) -> List[int]:
        for i in range(len(A)):
            A[i] = A[i] * A[i]
        A.sort()
        return A

class Solution:
    #time: O(N), space:O(N)
    def sortedSquares(self, A: List[int]) -> List[int]:
        n = len(A)
        pospointer = 0
        while pospointer < n and A[pospointer] < 0:
            pospointer += 1
        negpointer = pospointer - 1
        res = []
        #counter = 0
        while (negpointer >= 0 and pospointer < n):
            if A[negpointer] * A[negpointer] < A[pospointer] * A[pospointer]:
                res.append(A[negpointer] * A[negpointer])
                negpointer -= 1
            else:
                res.append(A[pospointer] * A[pospointer])
                pospointer += 1
            #counter += 1
        while negpointer >= 0:
            res.append(A[negpointer] * A[negpointer])
            #counter += 1
            negpointer -= 1
        while pospointer < n:
            res.append(A[pospointer] * A[pospointer])
            #counter += 1
            pospointer += 1
        return res


if __name__ == "__main__":
    print(Solution().sortedSquares([0, 2]))
