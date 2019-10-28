class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        sign = None
        for i in range(1, len(A)):
            if sign == None:
                if A[i] - A[i-1] > 0:
                    sign = 1
                elif A[i] - A[i-1] < 0:
                    sign = -1
            else:
                if (A[i] - A[i-1]) * sign < 0:
                    return False
        return True



class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        is_incre = True
        is_decre = True
        for i in range(1, len(A)):
            if A[i] < A[i-1]:
                is_incre = False
                break
        for i in range(1, len(A)):
            if A[i] > A[i-1]:
                is_decre = False
                break
        return is_incre or is_decre