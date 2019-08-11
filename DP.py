'''
When is possible to use dynamic programming?
- find max or min
- check validity
- find the number of all solutions

When not use DP?
- find all the spesific solution instead of the total number
- input is a set rather than a sequence
- brute force complexity is O(n^k)

DP consists of:
- state
- function
- initialization
- answer

DP problem:
- coordinate: eg. f[x] represent from start to coordinate x
- 
'''

# coordinate DP

## 1. Minimum Path Sum: Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its paths

class Solution:
	def minPathSum(self, grid):
		if not grid:
			return 0
		m, n = len(grid), len(grid[0])
		for i in range(m):
			for j in range(n):
				if i == 0 and j > 0:
					grid[i][j] += grid[i][j - 1]
				if j == 0 and i > 0:
					grid[i][j] += grid[i - 1][j]
				elif j > 0 and i > 0:
					grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])

		return grid[m - 1][n - 1]
		

		
		
