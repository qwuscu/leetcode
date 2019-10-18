class Solution:
    def fib(self, N: int) -> int:
        if N <= 1:
            return N
        nums = [None] * (N+1)
        nums[0] = 0
        nums[1] = 1
        for i in range(2, N+1):
            nums[i] = nums[i-1] + nums[i-2]
        return nums[N]