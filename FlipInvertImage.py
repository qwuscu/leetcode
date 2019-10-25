class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        m, n = len(A), len(A[0])
        for i in range(m):
            A[i] = A[i][::-1]
            # for j in range(n):
            #     A[i][j] ^= 1
            for j in range(n):
                if A[i][j] == 1:
                    A[i][j] = 0
                else:
                    A[i][j] = 1
        return A


# [1,0,0] -> [0,0,1] -> [1,1,0]
# which means if A[i][j]^A[i][n-j-1]=1, no need to change

class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        m, n = len(A), len(A[0])
        for i in range(m):
            for j in range(int((n-1)/2)+1):
                if A[i][j]^A[i][n-j-1] == 0:
                    if A[i][j] == 0:
                        A[i][j] = 1
                        A[i][n-j-1] = 1
                    else:
                        A[i][j] = 0
                        A[i][n-j-1] = 0
        return A
    
    