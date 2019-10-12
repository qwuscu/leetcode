from typing import List


class Solution:
    # 同时记录count和result，若当前数为1，count加一，若count此时大于result，将result更新为count。若不为1，重置连续数count为0。
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        result = 0
        count = 0
        for num in nums:
            if num == 1:
                count += 1
                result = max(count, result)
            else:
                count = 0
        return result


if __name__ == "__main__":
    print(Solution().findMaxConsecutiveOnes([1,1,0,1,1,1]))