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


## Coordinate DP:
The problems that can be counted as coordinate type usually has a grid as the input.
Initialize the boundary conditions, usually the first column and row.

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

---

## Sequence
When we deal with the single sequence problems, usually an array with N+1 in length is initiated to store the results.

Let's take a look at 2 examples.

1. Word Break: Given a string s and a dictionary of words dict, determine if s can be break into a space-separated sequence of one or more dictionary words.

---

state: state[i] represents first i letters can break or not
function: 1 < j < i, if state[i - j] is valid and s[i - j:i] in the dict, then state[i] is valid
initialization: when there is not str, return True, thus state[0] == True
result: state[-1]

---

```python
class Solution:
	def wordBreak(self, s, dict):
		if len(s) == 0:
			return True
		if len(dict) == 0:
			return False
		state = [True] + [False] * len(s)
		max_len = max([len(i) for i in s])
		for i in range(1, len(s) + 1):
			for j in range(1, min(i, max_len) + 1):
				if not state[i - j]:
					continue
				if s[i - j:i] in dict:
					state[i] = True
					break
		return state[-1]
```

2. Check if a part of string is palindrome.

---

state: f[i][j] represents from ith to jth position of the string is a palindrome or not.
function: f[i + 1][j - 1] == True AND s[i] == s[j]
initialization: f[i][i] == True
result: f[x][y] represents the result of the string from xth to yth.

---

```
class Solution:
	def validPalidrome(self, s):
		n = len(s)
		is_palindrome = [[False for i in range(n)] for i in range(n)]
		for i in reversed(range(n)):
			for j in range(i, n):
				if s[i] == s[j] and (j - i < 2 or is_palindrome[i + 1][j - 1]):
					is_palindrome[i][j] = True

		return is_palindrome

```

If there are two sequences, we can use the similar mathods. 

state:f[i][j] represents the first i items of the first sequence and first j items of the second sequence.
initialization: f[i][0], f[0][j]
answer: f[n][m]
n = len(s1), m = len(s2)

1. Longest common sequence

state: f[i][j] is the longest common sequence of the first i elements of s1 and first j element of s2
function: f[i][j] = max(f[i - 1][j], f[i][j - 1], f[i - 1][j - 1] + 1) when s1[i] == s2[j]
f[i][j] = max(f[i - 1][j], f[i][j - 1]) when s1[i] != s2[j]
initialization: f[0][j] = f[i][0] = 0
result: f[m][n]

---

```python
class Solution:
	def longest_common_sub(self, s1, s2):
		m, n = len(s1), len(s2)
		f = [[0 for i in range(n + 1)] for j in range(m + 1)]
		for i in range(m):
			for j in range(n):
				if s1[i] != s2[j]:
					f[i + 1][j + 1] = max(f[i + 1][j], f[i][j + 1])
				else:
					f[i + 1][j + 1] = max(f[i + 1][j], f[i][j + 1], f[i][j] + 1)
		return f[m][n]
```


