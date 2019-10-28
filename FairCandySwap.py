class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        sum_A, sum_B = sum(A), sum(B)
        # Time Limit Exceeded if doesn't set B
        set_B = set(B)
        
        for a in A:
            if a + (sum_B-sum_A)/2 in set_B:
                return (a, a+(sum_B-sum_A)//2)



class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        sum_A, sum_B = sum(A), sum(B)
        A.sort()
        B.sort()
        ans = []
        tmp = sum_A - (sum_B+sum_A)//2
        i, j = 0, 0
        while i < len(A) and j < len(B):
            if A[i] - B[j] == tmp:
                ans.append(A[i])
                ans.append(B[j])
                break
            elif A[i] - B[j] > tmp:
                j += 1
            else:
                i += 1
        return ans
                            