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
