class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        i = 0
        j = len(A)-1
        while i < j:
            if A[i] % 2 != 0:
                A[i], A[j] = A[j], A[i]
                j -= 1
            else:
                i += 1
        return A