class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        lookup={}
        ans=[None]*2
        n=len(nums)
        for num in nums:
            if num not in lookup:
                lookup[num]=1
            else:
                ans[0]=num
        for i in range(1,n+1):
            # when if i not in nums -> Time limit exceed, why???
            if i not in lookup:
                ans[1]=i
                break
        return ans



class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums2=set(nums)
        ans=[None]*2
        ans[0]=sum(nums)-sum(nums2)
        n=len(nums)
        ans[1]=sum(range(1,n+1))-sum(nums2)
        return ans