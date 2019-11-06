class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # sort two arrays, then compare
        nums1.sort()
        nums2.sort()
        ans = []
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                if nums1[i] not in ans:
                    ans.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                i += 1
        return ans


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        lookup = {}
        res = []
        for num in nums1:
            lookup[num] = lookup.get(num, 0) + 1
        for num in nums2:
            if num in lookup and num not in res:
                res.append(num)
        return res