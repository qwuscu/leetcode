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
    

class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        m = len(A)
        n = len(A[0])
        for i in range(m):
            A[i] = A[i][::-1]
            for j in range(n):
                A[i][j] ^= 1
        return A


class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for row in A:
            for i in range((len(row) + 1) // 2):
                """
                In Python, the shortcut row[~i] = row[-i-1] = row[len(row) - 1 - i]
                helps us find the i-th value of the row, counting from the right.
                """
                row[i], row[~i] = row[~i] ^ 1, row[i] ^ 1
        return A