class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r * c != len(nums) * len(nums[0]):
            return nums
        newNums = []
        newNums_row = []
        j = 0
        for num_row in nums:
            for num in num_row:
                newNums_row.append(num)
                j += 1
                if j == c:
                    newNums.append(newNums_row)
                    j = 0
                    newNums_row = []
        return newNums
                
        
