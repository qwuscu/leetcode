class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxx = [None] * len(nums)
        minn = [None] * len(nums)
        ans = maxx[0] = minn[0] = nums[0]
        for i in range(1, len(nums)):
            maxx[i] = minn[i] = nums[i]
            if nums[i] > 0:
                maxx[i] = max(maxx[i], maxx[i-1]*nums[i])
                minn[i] = min(minn[i], minn[i-1]*nums[i])
            else:
                maxx[i] = max(maxx[i], minn[i-1]*nums[i])
                minn[i] = min(minn[i], maxx[i-1]*nums[i])
            ans = max(maxx[i], ans)
        return ans
    
