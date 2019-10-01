from typing import List

    #two pointers, time complexity: O(n), spcae: O(1)
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0;
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
        return i+1


if __name__ == "__main__":
    print(Solution().removeDuplicates([1, 1, 2]))
