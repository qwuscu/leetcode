from typing import List


class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        '''
        从头到尾遍历，如果该位数字为1，则向后前进两位，否则前进1位，循环的条件是i < n-1，即留出最后一位.
        当循环退出后，i正好停留在n-1上，说明最后一位是单独分割开的。
        '''

        length, n = 0, len(bits)
        while length < n - 1:
            if bits[length] == 1:
                length += 2
            else:
                length += 1
        return length == n-1


print(Solution().isOneBitCharacter([1,0,0]))