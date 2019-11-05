import math


# class Solution:
#     def arrangeCoins(self, n: int) -> int:
#          # n = (1 + x) * x / 2, 求解得 x = (-1 + sqrt(8 * n + 1)) / 2, 答案对x取整
#         return math.floor((-1+math.sqrt(8*n+1))/2)


"""
You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.

Given n, find the total number of full staircase rows that can be formed.

n is a non-negative integer and fits within the range of a 32-bit signed integer.
"""

# class Solution(object):
#     def arrangeCoins(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#
#         """
#         i, j = 1, n
#
#         while i <= j:
#             m = i + (j-i)//2
#             if m*(m+1) > n/2:
#                 j = m
#         # when n=8, it goes to infinite loop i=j=2
#         """
#         i, j = 1, n
#         while i <= j:
#             m = i + (j-i)//2
#             if m*(m+1) == 2*n:
#                 return m
#             elif m*(m+1) > 2*n:
#                 j = m-1
#             else:
#                 i = m+1
#         return j

class Solution:
    def arrangeCoins(self, n):
        res = 0
        while n > res:
            res += 1
            n -= res

        return res




print(Solution().arrangeCoins(8))
print(Solution().arrangeCoins(4))
print(Solution().arrangeCoins(5))
