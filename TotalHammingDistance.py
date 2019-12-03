class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        convert = "{0:032b}".format
        mapped = map(convert, nums)
        res = 0
        for i in zip(*mapped):
            res += (i.count('0') * i.count('1'))
        return res


class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        return sum(i.count('1') * i.count('0') for i in zip(*map('{:032b}'.format, nums)))