from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):
                flowerbed[i] = 1
                count += 1
        return count >= n

'''
fail at test case [0,0],2 expect false, actual true
[0,0,0,0], 3, expect false, actual true
'''
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 0
        end = len(flowerbed)
        while i < end:
            if flowerbed[i] == 0:
                if i == 0 and (i == end - 1 or flowerbed[i+1] == 0):
                    i += 1
                    n -= 1
                elif i == end-1 and flowerbed[i-1] == 0:
                    i += 1
                    n -= 1
                elif i + 2 < end and flowerbed[i + 2] == 0 and flowerbed[i + 1] == 0:
                    n -= 1
                    i += 2
                else:
                    i += 1
            else:
                i += 1  # flowerbed[i]==1
        return n <= 0


''' this works, but very slow '''
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 0
        end = len(flowerbed)
        while i < end:
            if flowerbed[i] == 0:
                if i == 0 and (i == end - 1 or flowerbed[i+1] == 0):
                    i += 1
                    n -= 1
                elif i == end-1 and flowerbed[i-1] == 0:
                    i += 1
                    n -= 1
                elif i + 2 < end and flowerbed[i + 2] == 0 and flowerbed[i + 1] == 0:
                    n -= 1
                    i += 2
                else:
                    i += 1
            else:
                i += 1  # flowerbed[i]==1
        return n <= 0



class Solution:
    def canPlaceFlowers(self, flowerbed, n):

        if n == 0: return True
        if not flowerbed: return False

        placed = 0
        left, mid, right = 0, 0, flowerbed[0]

        for i in range(len(flowerbed) - 1):

            left, mid, right = mid, right, flowerbed[i + 1]
            if not (left or mid or right):
                placed += 1
                mid = 1

            if placed == n:
                return True

        if not (mid or right): # failed at [1,0,0,0,1,0,0], 2, expected: true, actual: false
            placed += 1

        return placed >= n


if __name__ == "__main__":
    # flowerbed = [1,0,0,0,1,0,0] # -> [1,0,1,0,1,0,0],count=1 ->
    # n = 2
    # print(Solution().canPlaceFlowers(flowerbed, n))
    print(Solution().canPlaceFlowers([0], 1))
    print(Solution().canPlaceFlowers([0, 0], 2))  # false
    print(Solution().canPlaceFlowers([0, 0, 0, 0], 3))  # false
    print(Solution().canPlaceFlowers([0,0,1,0,1], 2))
    print(Solution().canPlaceFlowers([1,0,1,0,0], 1))
