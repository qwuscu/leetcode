from typing import List


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




class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r * c != len(nums) * len(nums[0]):
            return nums

        from queue import Queue
        que = Queue()
        for row in nums:
            for num in row:
                que.put(num)
        new_nums = []
        for i in range(r):
            new_row = []
            for j in range(c):
                new_row.append(que.get())
            new_nums.append(new_row)
        return new_nums

print(Solution().matrixReshape([[1,2],[3,4]], 1, 4))