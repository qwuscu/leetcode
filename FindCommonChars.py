from typing import List

# this only find most common without duplicates
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        lookup = {}
        for i in range(len(A)):
            for j in range(len(A[i])):
                # add this charater if it's not in lookup
                if A[i][j] not in lookup:
                    lookup[A[i][j]] = [i]
                # if this character already existed in this str, not append it
                else:
                    if i not in lookup[A[i][j]]:
                        lookup[A[i][j]].append(i)
        res = []
        com = 0
        for key in lookup:
            com = max(com, len(lookup[key]))
        for key in lookup:
            if len(lookup[key]) == com:
                res.append(key)
        return res


print(Solution().commonChars(["bella","label","roller"]))

# python has Counter method which counts characters 
from collections import Counter


class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        res = Counter(A[0])
        for i in range(1, len(A)):
            res = res & Counter(A[i])
        return list(res.elements())
    


class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        # answer map
        ans_map = {}
        mid_map = {}
        res = []
        for i in range(len(A[0])):
            if A[0][i] not in ans_map:
                ans_map[A[0][i]] = 1
            else:
                ans_map[A[0][i]] += 1
        for i in range(1, len(A)):
            # need to rest mid_map every time
            mid_map = {}
            for j in range(len(A[i])):
                if A[i][j] not in mid_map:
                    mid_map[A[i][j]] = 1
                else:
                    mid_map[A[i][j]] += 1

            for key in ans_map:
                if key not in mid_map:
                    ans_map[key] = -1
                else:
                    ans_map[key] = min(ans_map[key], mid_map[key])
        for key in ans_map:
            while ans_map[key] > 0:
                res.append(key)
                ans_map[key] -= 1
                
        return res


class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        lookup = list(A[0])

        for word in A:
            tmp = []

            for char in word:

                if char in lookup:
                    tmp.append(char)
                    lookup.remove(char)

            lookup = tmp



class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        lookup = list(A[0])

        for word in A:
            tmp = []

            for char in word:

                if char in lookup:
                    tmp.append(char)
                    lookup.remove(char)

            lookup = tmp
        return lookup
        
        
