from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        """
        Step1:划分成[1,2,3,4], [5,6,7]
        Step2:分别reverse，[4,3,2,1], [7,6,5]
        Step3:合并reverse，[5,6,7,1,2,3,4]
        """

        # this is not doing in-place, nums[:n-k] itself returns a new list in the first place.
        n = len(nums)
        k %= n
        res = nums[:n - k][::-1] + nums[n - k:][::-1]
        res.reverse()
        return res

        # in-place 
        n = len(nums)
        k %= n
        nums[:n-k] = nums[:n-k][::-1]
        nums[n-k:] = nums[n-k:][::-1]
        nums.reverse()


if __name__ == "__main__":
    nums = [1,2,3,4,5,6,7]
    k = 3
    print(Solution().rotate(nums, k))
