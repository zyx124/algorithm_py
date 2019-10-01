## What is Dynamic Programming?

- Memory search algorithms, i.e. memorize the value of the past steps to avoid repetitive calculations.


## When is it likely to use DP?
- Find max or min
- Check validity
- Find the **number** of all solutions


## When not use DP?
- Find all the spesific solution instead of the total number
- Input is a set rather than a sequence
- Brute force complexity is O(n^k)

## DP consists of:
- state
- function
- initialization
- answer
For a DP problem, we should find the for elements listed above to obtain the solution.

## DP problem may have such types:
- Coordinate: eg. f[x] represents from start to coordinate x
- Single sequence: eg. f[i] represents first i positions.


Coordinate DP:
Initialize the boundary conditions like the first column and row.

1. Minimum Path Sum: Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its paths

---
state: grid[i][j] represents the number of paths from start to (i, j)
function: grid[x][y] = min(grid[x - 1][y], grid[x][y - 1])
initialization: 	grid[i][0] = 1 
 					grid[0][j] = 1
answer: grid[m - 1][n - 1]
---


```python
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
```

2. Climbing Stairs: Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

```python 
class Solution:
	def climb(self, n):
		if n == 0:
			return 0
		if n == 1:
			return 1
		if n == 2:
			return 2
		result = [1, 2]
		for i in range(n - 2):
			result.append(result[-2] + result[-1])
		return result[-1]
```


