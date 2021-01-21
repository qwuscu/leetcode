from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = set(nums)
        nums = list(nums)
        nums.sort()
        if len(nums) < 3: return max(nums)
        return nums[-3]


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        ans = [-float('inf')] * 3
        for num in nums:
            # need to check ==, it may have duplicate val. just >, fail at [2,2,3,2]
            # if [2,2,3,2] => ans will be [3,2,2]
            if num >= ans[0]:
                if num == ans[0]:
                    # when =, continue. otherwise, it may goes to ans[1]
                    continue
                ans[2] = ans[1]
                ans[1] = ans[0]
                ans[0] = num
            # no =, fail at [5, 2, 2]
            elif num >= ans[1]:
                if num == ans[1]:
                    continue
                ans[2] = ans[1]
                ans[1] = num
            elif num >ans[2]:
                ans[2] = num

        if ans[2] == -float('inf'):
            return ans[0]
        else:
            return ans[2]
                


print(Solution().thirdMax([2,2,3,1]))
