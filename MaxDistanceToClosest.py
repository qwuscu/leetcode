from typing import List


# class Solution:
#     def maxDistToClosest(self, seats: List[int]) -> int:
#         n = len(seats)
#         ans = [n] * n
#         seated = -float('inf')
#         for i in range(n):
#             if seats[i] == 1:
#                 seated = i
#             ans[i] = i-seated
#         for i in range(n-1, -1, -1):
#             if seats[i] == 1:
#                 seated = i
#             ans[i] = min(ans[i], abs(i-seated))
#         return max(ans)

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        left_index = seats.index(1)
        right_index = len(seats) - 1

        while right_index > 0 and seats[right_index] == 0:
            right_index -= 1

        zero, max_zero = 0, 0
        for i in range(left_index + 1, right_index + 1):
            if seats[i] == 0:
                zero += 1
                max_zero = max(zero, max_zero)
            else:
                zero = 0

        return max(left_index, len(seats) - 1 - right_index, (max_zero + 1) // 2)


# class Solution:
#     def maxDistToClosest(self, seats: List[int]) -> int:
#         i, res = 0, 0
#         for j in range(len(seats)):
#             if seats[j] == 1:
#                 if i == 0:
#                     res = j
#                 else:
#                     res = max(res, (j - i + 1) // 2)
#                 i = j + 1
#         res = max(res, len(seats) - i)
#         return res


print(Solution().maxDistToClosest([1,0,0,0]))
print(Solution().maxDistToClosest([1,0,0,0,1,0,1]))