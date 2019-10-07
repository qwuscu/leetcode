class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for num in range(numRows):
            nums = [None for _ in range(num+1)]
            nums[0], nums[-1] = 1, 1 #first and last element in the row is 1
            for j in range(1, num):
                 nums[j] = res[num-1][j-1] + res[num-1][j]
            res.append(nums)
        return res


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = []
        for row in range(rowIndex+1):
            res.insert(0, 1)
            for i in range(1, len(res)-1):
                res[i] = res[i+1] + res[i]
        return res


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1]
        for _ in range(rowIndex):
            res = [x + y for x, y in zip([0] + res, res + [0])]
        return res

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1]
        for _ in range(1, rowIndex+1):
            x = [0] + res
            y = res + [0]
            res = [i+j for i, j in zip(x, y)]
        return res
    
