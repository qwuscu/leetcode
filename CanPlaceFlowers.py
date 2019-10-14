from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):
                flowerbed[i] = 1
                count += 1
        return count >= n


if __name__ == "__main__":
    flowerbed = [1,0,0,0,1,0,0] # -> [1,0,1,0,1,0,0],count=1 ->
    n = 2
    print(Solution().canPlaceFlowers(flowerbed, n))
