from typing import List

# class Solution:
#     def maxProduct(self, nums: List[int]) -> int:
#         maxx = [None] * len(nums)
#         minn = [None] * len(nums)
#         ans = maxx[0] = minn[0] = nums[0]
#         for i in range(1, len(nums)):
#             maxx[i] = minn[i] = nums[i]
#             if nums[i] > 0:
#                 maxx[i] = max(maxx[i], maxx[i-1]*nums[i])
#                 minn[i] = min(minn[i], minn[i-1]*nums[i])
#             else:
#                 maxx[i] = max(maxx[i], minn[i-1]*nums[i])
#                 minn[i] = min(minn[i], maxx[i-1]*nums[i])
#             ans = max(maxx[i], ans)
#         return ans
    
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = nums[0]
        prev_pos_largest = nums[0]
        prev_neg_largest = nums[0]
        for num in nums[1:]:
            if num >= 0:
                cur_pos_largest = max(num, num*prev_pos_largest)
                cur_neg_largest = min(num, num*prev_neg_largest)
            else:
                cur_pos_largest = max(num, num*prev_neg_largest)
                cur_neg_largest = min(num, num*prev_pos_largest)
            result = max(result, cur_pos_largest)
            prev_neg_largest = cur_neg_largest
            prev_pos_largest = cur_pos_largest
        return result

# one pass
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
    #Approach : One pass
    #Time : O(n)
    #Space : O(1)
        if len(nums) == 0: return 0
        max_so_far = nums[0]
        min_so_far = nums[0]
        result = max_so_far
        for num in nums[1:]:
            tmp_max = max(num, max_so_far*num, min_so_far*num)
            min_so_far = min(num, max_so_far*num, min_so_far*num)
            max_so_far = tmp_max
            result = max(max_so_far, result)
        return result


 # brute force
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #Approach : Brute Force
        #Time : O(n^2)
        #Space : O(1)

        if len(nums) == 0:
            return 0

        result = nums[0]
        n = len(nums)
        for i in range(n):
            accu = 1
            for j in range(i, n):
                accu *= nums[j]
                result = max(result, accu)

        return result

if __name__ == "__main__":
    print(Solution().maxProduct([-2,0,-1,-6,2,-5,-4]))


