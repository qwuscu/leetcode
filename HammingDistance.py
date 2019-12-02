class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        ans = x ^ y
        count = 0
        while ans:
            count += 1
            ans = ans & (ans - 1)
        return count


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return '{0:b}'.format(x ^ y).count('1')
