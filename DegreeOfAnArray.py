class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        lookup = {}
        for i in range(len(nums)):
            if nums[i] not in lookup:
                lookup[nums[i]] = [i]
            else:
                lookup[nums[i]].append(i)

        max_fre = 0
        for key in lookup:
            max_fre = max(max_fre, len(lookup[key]))

        degree = float('inf')
        for key in lookup:
            if len(lookup[key]) == max_fre:
                degree = min(degree, max(lookup[key])-min(lookup[key])+1)
        return degree



from collections import Counter 


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        c = Counter(nums)
        degree = max(c.values())
        first = {}
        last = {}
        for i, v in enumerate(nums):
            # first.setdefault(v, i)
            if v not in first:
                first[v] = i
            last[v] = i
        ans = float('inf')
        for v in c:
            if c[v] == degree:
                ans = min(ans, last[v] - first[v]+1)
        return ans

        # return min(last[v] - first[v] + 1 for v in c if c[v] == degree)