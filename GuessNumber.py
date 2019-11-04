# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        i, j = 1, n
        while i < j:
            m = i + (j - i) // 2
            if guess(m) == 0:
                return m
            elif guess(m) == -1:
                j = m
            else:
                i = m + 1
        return j
