class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        known = set()
        while True:
            num = 0
            for i in str(n):
                num += int(i)**2
            if num == 1:
                return True
            if num in known:
                return False
            known.add(num)
            n = num
        return True

if __name__ == '__main__':
    print(Solution().isHappy(19))
