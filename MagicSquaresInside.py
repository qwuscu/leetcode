from typing import List


class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        # 基本结论可得幻方中每行每列对角线和一定为15，且幻方中心一定为5，
        # 根据此增加判断条件，然后遍历各个3x3矩形统计。
        row, column = len(grid), len(grid[0])
        ans = 0
        for r in range(row - 2):
            for c in range(column - 2):
                if grid[r + 1][c + 1] == 5 and self.is_valid(grid, r, c):
                    ans += 1
        return ans

    def is_valid(self, grid, r, c):
        count = [0 for i in range(10)]
        for x in range(r, r + 3):
            for y in range(c, c + 3):
                k = grid[x][y]
                if k < 1 or k > 9 or count[k] == 1:
                    return False
                count[k] = 1
        if 15 != grid[r][c] + grid[r][c + 1] + grid[r][c + 2]:
            return False
        if 15 != grid[r + 1][c] + grid[r + 1][c + 1] + grid[r + 1][c + 2]:
            return False
        if 15 != grid[r + 2][c] + grid[r + 2][c + 1] + grid[r + 2][c + 2]:
            return False
        if 15 != grid[r][c] + grid[r + 1][c] + grid[r + 2][c]:
            return False
        if 15 != grid[r][c + 1] + grid[r + 1][c + 1] + grid[r + 2][c + 1]:
            return False
        if 15 != grid[r][c + 2] + grid[r + 1][c + 2] + grid[r + 2][c + 2]:
            return False
        if 15 != grid[r][c] + grid[r + 1][c + 1] + grid[r + 2][c + 2]:
            return False
        if 15 != grid[r + 2][c] + grid[r + 1][c + 1] + grid[r][c + 2]:
            return False
        return True


print(Solution().numMagicSquaresInside([[4,3,8,4],[9,5,1,9],[2,7,6,2]]))
