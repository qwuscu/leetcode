from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums: return -1
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid

            if nums[mid] < nums[right]:
                if nums[mid] < target <= nums[right]: # if target < nums[right], [1,3],3 => -1
                    left = mid + 1
                else:
                    right = mid
            else:
                if nums[left] <= target < nums[mid]: # if nums[left]<target, [2,3,1],2 => -1
                    right = mid
                else:
                    left = mid + 1

        if nums[left] == target:
            return left
        else:
            return -1


if __name__ == "__main__":
    print(Solution().search([4,5,6,7,0,1,2],0))
    print(Solution().search([1,3], 3))
    print(Solution().search([1, 3], 1))
    print(Solution().search([1], 1))
    print(Solution().search([2,3,1], 2))