class Solution:
    # Hash，时间O(N)，空间O(N)
    def findPairs(self, nums: List[int], k: int) -> int:
        if k < 0: return 0
        lookup = {}
        ans = 0
        for num in nums:
            lookup[num] = lookup.get(num, 0) + 1
        if k == 0:
            for num in lookup:
                if lookup[num] > 1:
                    ans += 1
        else:
            for num in lookup:
                if num + k in lookup:
                    ans += 1
        return ans


class Solution:
    # 因为k可以是零，要特殊处理一下，所以有循环尾部 j += 1 的操作。
    # 双指针，时间O(nlogN)，空间O(1)
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        count = 0
        i, j = 0, 1
        while j < len(nums):
            if nums[j] - nums[i] < k:
                j += 1
            elif nums[j] - nums[i] > k:
                i += 1
            else:
                count += 1
                i += 1
                j += 1
                while j < len(nums) and nums[j] == nums[j - 1]:
                    j += 1
                while i < j and nums[i] == nums[i - 1]:
                    i += 1
            if i == j:
                # need to add this case, fail test case: [1,1,1,2,2], 0
                # when i=3, and j=3, if doesn't match while condition
                j += 1
        return count
   
