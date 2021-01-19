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
        # n = len(nums)
        # k %= n
        # res = nums[:n - k][::-1] + nums[n - k:][::-1]
        # res.reverse()
        # return res
        #
        # # in-place
        # n = len(nums)
        # k %= n
        # nums[:n-k] = nums[:n-k][::-1]
        # nums[n-k:] = nums[n-k:][::-1]
        # nums.reverse()

        # extra space, space: O(n), time: O(n)
        n = len(nums)
        k = k % n
        a = [0 for _ in range(n)]
        for i in range(n):
            a[(i+k)%n]=nums[i]
        nums = a
        return nums


# brute force, time limit exceeded, time: O(n*k), space: O(1)
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        for i in range(k):
            previous = nums[-1]
            for j in range(n):
                nums[j], previous = previous, nums[j]


# using extra space, time: O(n) One pass is used to put the numbers in the new array. And another pass to copy the new array to the original one.
# space: O(n)
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        a = [0] * n
        for i in range(n):
            a[(i+k)%n] = nums[i]
        nums[:] = a

if __name__ == "__main__":
    nums = [1,2,3,4,5,6,7]
    k = 10
    print(Solution().rotate(nums, k))
