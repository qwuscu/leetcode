class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        even = 0
        odd = 1
        n = len(A)
        res = [None for _ in range(n)]
        for i in range(n):
            if A[i] %2 == 0:
                res[even] = A[i]
                even += 2
            else:
                res[odd] = A[i]
                odd += 2
        return res