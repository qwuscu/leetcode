class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        lookup = {}
        ans = []
        for num in nums1:
            lookup[num] = lookup.get(num, 0) + 1

        for num in nums2:
            if num in lookup and lookup[num] > 0:
                ans.append(num)
                lookup[num] -= 1

        return ans

