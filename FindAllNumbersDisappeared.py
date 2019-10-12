class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        lookup = {}
        ans = []
        i = 1
        for num in nums:
            if num not in lookup:
                lookup[num] = 1
            else:
                lookup [num] += 1
        while i <= len(nums):
            if i not in lookup:
                ans.append(i)
            i += 1
        return ans

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        vis = [None] * len(nums)
        ans = []
        for num in nums:
            vis[num-1] = 1
        for i in range(len(vis)):
            if vis[i] == None:
                ans.append(i+1)
        return ans
