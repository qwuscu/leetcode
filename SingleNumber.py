class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        lookup = {}
        for num in nums:
            lookup[num] = lookup.get(num, 0) + 1
        for key in lookup:
            if lookup[key] == 1:
                return key


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # 异或运算具有很好的性质，相同数字异或运算后为0，并且具有交换律和结合律，故将所有数字异或运算后即可得到只出现一次的数字。
        # 异或运算
        ans = 0
        for num in nums:
            ans = ans ^ num
        return ans