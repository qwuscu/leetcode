class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        r, c = len(matrix), len(matrix[0])
        for i in range(r-1):
            for j in range(c-1):
                # 按照题意枚举每条对角线。即每个数和它右下方的数必须相同。
                if matrix[i][j] != matrix[i+1][j+1]:
                    return False
        return True
                
