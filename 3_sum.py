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
    '''
    我倒是觉得，这题就掌握两个思想：
    1. 将3Sum退化成2Sum: for 循环每次固定好第一个数，剩下的问题不就是基础的2 Sum问题吗。
    2. 去重: 数组sort的以后，第一层的去重基本是模板了。
    因为这题比较特殊是3Sum, 意味着只要第二层不重复，第三层也不会重复。
    所以在第二层也就是while循环那里套用第一层的去重方法就好了。

    时间复杂度 O(n^2) 空间 O(1)
    '''

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
