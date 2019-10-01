class Solution:
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     for i in range(len(nums)-1):
    #         for j in range(i+1, len(nums)):
    #             if nums[i] + nums[j] == target:
    #                 return [i, j]
    #     return [0, 0]


    def twoSum(self, nums, target):
        mapping = {}
        for i in range(len(nums)):
            tmp = target - nums[i]
            if tmp in mapping:
                return [mapping[tmp], i]
            else:
                mapping[nums[i]] = i
        return [0, 0]


if __name__ == "__main__":
    print(Solution().twoSum([2,7,9,11], 9))
