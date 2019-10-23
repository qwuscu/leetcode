class Solution:
    def climb_stairs(self, n: int) -> int:
        res = [None] * (n+1)
        if n == 1: return 1
        elif n == 2: return 2
        else:
            res[1] = 1
            res[2] = 2
            for i in range(3, n+1):
                res[i] = res[i-1] + res[i-2]
        return res[n]


    def test(self, n, expected):
        output = Solution().climb_stairs(n)
        print(n, output)
        assert expected == output


if __name__ == "__main__":
    Solution().test(3, 3)
    Solution().test(2, 2)
    

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1: return n
        last = 1
        secondlast = 1
        for i in range(2, n+1):
            now = last + secondlast
            secondlast = last
            last = now
        return now
            
