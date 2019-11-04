# n = int(input("please enter the number："))
# for i in range(2, n):
#     if n % i == 0:
#         print(" %d is not a prime number！" % n)
#         break
# else:
#     print(" %d is a prime number！" % n)


# res = []
# for i in range(2,100):
# 	for j in range(2,i):
# 		if i%j == 0:
# 			break
# 	else:
# 		res.append(i)
# print(res)


# def eratosthenes(n):
#     IsPrime = [True] * (n + 1)
#     for i in range(2, int(n ** 0.5) + 1):
#         if IsPrime[i]:
#             for j in range(i * i, n + 1, i):
#                 IsPrime[j] = False
#     return [x for x in range(2, n + 1) if IsPrime[x]]
#
# if __name__ == "__main__":
#     print(eratosthenes(120))

# class Solution:
#     def countPrimes(self, n: int) -> int:
#         isPrime = [True] * (n+1)
#         res = 0
#         for i in range(2,n+1):
#             if isPrime[i]:
#                 res += 1
#                 for j in range(i,n+1,i):
#                     isPrime[j] = False
#         return res
#
#
# print(Solution().countPrimes(2))


from collections import Counter


# class Solution(object):
#     def commonChars(self, A):
#         ans_map = {}
#         mid_map = {}
#         res = []
#         for i in range(len(A[0])):
#             if A[0][i] not in ans_map:
#                 ans_map[A[0][i]] = 1
#             else:
#                 ans_map[A[0][i]] += 1
#         for i in range(1, len(A)):
#             mid_map = {}
#             for j in range(len(A[i])):
#                 if A[i][j] not in mid_map:
#                     mid_map[A[i][j]] = 1
#                 else:
#                     mid_map[A[i][j]] += 1
#
#             for key in ans_map:
#                 if key not in mid_map:
#                     ans_map[key] = -1
#                 else:
#                     ans_map[key] = min(ans_map[key], mid_map[key])
#         for key in ans_map:
#             while ans_map[key] > 0:
#                 res.append(key)
#                 ans_map[key] -= 1
#
#         return res



# print(Solution().commonChars(["bella", "label", "roller"]))
# print(Solution().commonChars(["cool","lock","cook"]))


# A = ["bella", "label", "roller"]
# map1 = {}
# map2 = {}
# for a in A[0]:
#     map1[a] = map1.get(a, 0) + 1
# print(map1)
#
# for i in range(1, len(A)):
#     map2 = {}
#     for j in range(len(A[i])):
#         if A[i][j] not in map2:
#             map2[A[i][j]] = 1
#         else:
#             map2[A[i][j]] += 1
#     print(map2)
#     for key in map2:
#         if key in map1:
#             map1[key] = min(map1[key], map2[key])
#
#     print(map1)


# A = ["bella", "roller"]
# ans = list(A[0])
# print(ans)
# for word in A[1:]:
#     tmp = []
#     for char in word:
#         if char in ans:
#             tmp.append(char)
#             ans.remove(char)
#
# print(ans)



import collections


# class Solution:
#     """
#     @param nums: a list of integers
#     @return: return a integer
#     """
#     def findShortestSubArray(self, nums):
#         # write your code here
#         c = collections.Counter(nums)
#         first, last = {}, {}
#         for i, v in enumerate(nums):
#             first.setdefault(v, i)
#             last[v] = i
#         degree = max(c.values())
#         return min(last[v] - first[v] + 1 for v in c if c[v] == degree)
#
#
# print(Solution().findShortestSubArray([1, 2, 2, 3, 1]))
# print(Solution().findShortestSubArray([1, 2, 2, 3, 1, 4, 2]))

class Solution:
    def flipAndInvertImage(self, A):
        # Write your code here
        n = len(A)
        m = len(A[0])
        for i in range(n):
            for j in range(int((m - 1) / 2) + 1):
                if (A[i][j] ^ A[i][m - j - 1]) == 0:
                    if A[i][j] == 0:
                        A[i][j] = 1
                        A[i][m - j - 1] = 1
                    else:
                        A[i][j] = 0
                        A[i][m - 1 - j] = 0
        return A


print(Solution().flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]))