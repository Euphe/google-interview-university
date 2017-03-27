class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        perimeter = 0
        for i, row in enumerate(grid):
            for j, block in enumerate(row):
                if block:
                    #count water borders for block
                    right = False
                    left = False
                    up = False
                    down = False

                    if j == 0 or row[j-1] == 0:
                        left = True
                    if j == len(row)-1 or row[j+1] == 0:
                        right = True
                    if i == 0 or grid[i-1][j] == 0:
                        up = True
                    if i == len(grid)-1 or grid[i+1][j] == 0:
                        down = True
                    perimeter += int(right)+int(left) + int(up) + int(down)
        return perimeter
        
solution = Solution()

grid = [[0,1,1,1],
 [0,1,1,0],]

print(solution.islandPerimeter(grid))
