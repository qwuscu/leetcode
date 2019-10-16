class Solution:
    """
    @param arrs: an array of arrays
    @return: return the max distance among arrays
    """
    # https://www.lintcode.com/problem/maximum-distance-in-arrays/descriptions
    def maxDiff(self, arrs):
        # write your code here
        res = 0
        ma = arrs[0][-1]
        mi = arrs[0][0]
        for arr in arrs[1:]:
            tmp = max(abs(arr[0]-ma), abs(arr[-1]-mi))
            res = max(res, tmp)
            ma = max(ma, arr[-1])
            mi = min(mi, arr[0])
        return res


print(Solution().maxDiff([[1,2,3,4,5,6,7,8,9],[0,10]]))