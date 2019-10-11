class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        lookup = {}
        n = len(nums)
        for num in nums:
            lookup[num] = 1
        for i in range(len(nums)):
            if i not in lookup:
                return i
        return len(nums)

# wrong answer, Time Limit Exceeded
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if i not in nums:
                return i
        return len(nums)
     
# Method Two, calculate the sum
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        ans = (0+n)*(n+1)//2
        total = sum(nums)
        return ans - total


# method three
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
    # put nums[i] into nums[nums[i]]
    # then iterate whole array, first nums[index] != index is the ans
    # o(N) time o(1) space 
    
        n = len(nums)
        i = 0
        while i < n:
            while nums[i] != i and nums[i] < n:
                t = nums[i]
                nums[i] = nums[t]
                nums[t] = t
            i += 1
        for i in range(n):
            if nums[i] != i:
                return i
        return n
        
