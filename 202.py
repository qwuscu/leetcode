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
 
class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while True:
            total_num = 0
            while n > 0:
                total_num += (n % 10) ** 2
                n = n // 10

            if total_num == 1:
                return True
            if total_num in seen:
                return False
            seen.add(total_num)

            n = total_num

        # return True

if __name__ == '__main__':
    print(Solution().isHappy(19))
