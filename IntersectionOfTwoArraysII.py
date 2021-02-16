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


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()

        p1 = p2 = 0
        res = []

        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] == nums2[p2]:
                res.append(nums1[p1])
                p1 += 1
                p2 += 1
            elif nums1[p1] < nums2[p2]:
                p1 += 1
            else:
                p2 += 1
        return res