'''
Partition, combination and permutation often use DFS to search all of possible results bit
by bit. Backtrack is a commonly used technique.
'''

## permutation of a list of numbers: [1,3,4,54,5....]
class Solution:

	def permute(self, nums):
        # write your code here
        self.result = []
        self.dfs(nums, [])
        return self.result
    
    def dfs(self, nums, temp):
        if len(temp) == len(nums):
            self.result.append(temp.copy())
            
        for i in range(len(nums)):
            if nums[i] not in temp:
                temp.append(nums[i])
                self.dfs(nums, temp)
                temp.pop()
			
## combinations: find the combinations of k numbers out of a list.
class Solution:
	
	def combine(self, nums, k)
		self.result = []
		self.dfs(nums, k, [], 0)
		return self.result 
		
	def dfs(self, nums, k, subset, index):
		if len(subset) == k:
			self.result.append(subset.copy())
			return 
		for i in range(index, len(nums)):
			subset.append(nums[i])
			self.dfs(nums, k, subset, i+1)
			subset.pop()
			
## find subsets -> find the combinations of k numbers out of a list
## where k is from 0 to len(list). Example: [0] -> [[], [0]]
class Solution:
	
	def subset(self, nums):
		if nums is None:
			return 
		nums.sort()
		result = []
		subset = []
		index = 0
		self.dfs(nums, subset, index, result)
		return result
		
	def dfs(self, nums, subset, index, result):
		result.append(subset.copy())
		for i in range(index, len(nums)):
			subset.append(nums[i])
			self.dfs(nums, subset, i+1, result)
			subset.pop()
		
# we can actually actually treat the combinitions and permutations as graph problems. Trees are also graphs that can be solved by dfs or bfs.

# Take a look at the graph problems.
# Topological sorting: directed and undirected graphs


			
			
			
			
