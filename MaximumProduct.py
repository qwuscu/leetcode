from typing import List

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
    #  Time complexity : O(nlogn). Sorting the numsnums array takes nlogn time.
    # Space complexity : O(logn). Sorting takes O(logn) space.
        nums.sort()
        ans1 = nums[-1]*nums[-2]*nums[-3]
        ans2 = nums[0]*nums[1]*nums[-1]
        return max(ans1, ans2)

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
    # time: O(n). only one interation over the nums array of length n is required
    # space: O(1). Constant extra space is used.
        min1, min2 = float('inf'), float('inf')
        max1, max2, max3 = -float('inf'), -float('inf'), -float('inf')
        for num in nums:
            if num < min1:
                min2 = min1
                min1 = num
            elif num < min2:
                min2 = num

            if num > max1:
                max3 = max2
                max2 = max1
                max1 = num
            elif num > max2:
                max3 = max2
                max2 = num
            elif num > max3:
                max3 = num
        return max(min1*min2*max1, max1*max2*max3)


print(Solution().maximumProduct([9,1,5,6,7,2]))
