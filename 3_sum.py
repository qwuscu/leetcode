from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        if len(nums) < 3: return ans
        nums.sort()
        n = len(nums)
        for i in range(n-2):
            l = i+1
            r = len(nums)-1
            while l < r:
                if nums[l]+nums[r]+nums[i]==0:
                    if [nums[i], nums[l], nums[r]] not in ans:
                        ans.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                elif nums[l]+nums[r]+nums[i] > 0:
                    r -= 1
                else:
                    l += 1
        return ans


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        ans = []
        nums.sort()
        for i in range(len(nums) - 2):
            target = -nums[i]
            dic = {}
            for j in range(i + 1, len(nums)):
                if target - nums[j] in dic:
                    res = [nums[i], target - nums[j], nums[j]]
                    if res not in ans:
                        ans.append(res)
                else:
                    dic[nums[j]] = j
        return ans



class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3: return []
        nums.sort()
        ans = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] > 0:
                break

            target = -nums[i]
            start, end = i + 1, len(nums) - 1
            while start < end:
                if start > i + 1 and nums[start] == nums[start - 1]:
                    start += 1
                    continue
                cur_sum = nums[start] + nums[end]
                if cur_sum == target:
                    ans.append([nums[i], nums[start], nums[end]])
                    start += 1
                    end -= 1
                elif cur_sum < target:
                    start += 1
                else:
                    end -= 1
        return ans


print(Solution().threeSum([-1,0,1,2,-1,-4]))
