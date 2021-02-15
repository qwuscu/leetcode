class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if not firstList or not secondList:
            return []
        ans = []
        f = len(firstList)
        s = len(secondList)
        i = j = 0
        while i < f and j < s:
            lo = max(firstList[i][0], secondList[j][0])
            hi = min(firstList[i][1], secondList[j][1])
            if lo <= hi:
                ans.append([lo, hi])

            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1
        return ans
# Time Complexity: O(M + N)O(M+N), where M, NM,N are the lengths of A and B respectively.

# Space Complexity: O(M + N)O(M+N), the maximum size of the answer.