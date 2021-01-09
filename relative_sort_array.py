class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        from collections import Counter
        occ = Counter(arr1)
        ans = []
        for num in arr2:
            for i in range(0, occ[num]):
                ans.append(num)
        arr1.sort()
        for num in arr1:
            if num not in ans:
                for j in range(0, occ[num]):
                    ans.append(num)
        return ans


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        from collections import Counter
        occ = Counter(arr1)
        ans = []
        for num in arr2:
            for i in range(0, occ[num]):
                ans.append(num)
        tmp = []
        arr1 = set(arr1)
        for num in arr1:
            if num not in ans:
                for j in range(0, occ[num]):
                    tmp.append(num)
        tmp.sort()
        ans += tmp
        return ans


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        remainders = [num for num in arr1 if num not in arr2]
        remainders.sort()
        res = []
        mapping = {}
        for num in arr1:
            mapping[num] = mapping.get(num, 0) + 1
        for num in arr2:
            res += [num] * mapping[num]
        return res + remainders
