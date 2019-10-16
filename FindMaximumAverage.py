from typing import List

# time: O(n). We iterate over the numsnums array of length nn once to fill the sumsum array.
# Then, we iterate over n-k elements of  sum to determine the required result.
# space: O(n). We make use of a sum array of length nn to store the cumulative sum.
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        ans = [None] * len(nums)
        ans[0] = nums[0]
        for i in range(1,n):
            ans[i] = ans[i-1] + nums[i]
        res = ans[k-1]/k
        for i in range(k, n):
            res = max(res, (ans[i] - ans[i-k])/k)
        return res


# time: O(n). we iterate over the given nums array of length n once only
# space:O(1). constant extra space is used
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        total = 0
        for i in range(k):
            total += nums[i]
        result = total
        for i in range(k,len(nums)):
            total = total + nums[i] - nums[i-k]
            result = max(result, total)
        return result/k

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        total = sum(nums[:k])
        res = total
        for i in range(k, len(nums)):
            total = total + nums[i] - nums[i-k]
            res = max(res, total)
        return res/k


if __name__ == "__main__":
    print(Solution().findMaxAverage([-1],1))