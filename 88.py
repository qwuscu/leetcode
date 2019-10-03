class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #space:  O(1), time: O(m+n)
        k = m + n - 1
        m = m - 1
        n = n - 1
        while m >= 0 and n >= 0:
            if nums2[n] >= nums1[m]:
                nums1[k] = nums2[n]
                n -= 1
            else:
                nums1[k] = nums1[m]
                m -= 1
            k -= 1
        while n >= 0:
            nums1[k] = nums2[n]
            k -= 1
            n -= 1



class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while m > 0 and n > 0:
            if nums2[n-1] >= nums1[m-1]:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
            else:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
        if m == 0:
            nums1[0:n] = nums2[0:n]
