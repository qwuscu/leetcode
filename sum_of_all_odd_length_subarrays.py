from typing import List


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        totsum = 0
        n = len(arr)
        for i in range(1, n+1, 2):
            for j in range(n-i+1):
                totsum += sum(arr[j:j+i])
        return totsum


print(Solution().sumOddLengthSubarrays([1,4,2,5,3]))

