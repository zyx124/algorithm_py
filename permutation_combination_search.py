'''
Combination and permutation search often use DFS to go through all of possible results bit
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
		
	def bfs(self, nums, k, subset, index):
		if len(subset) == k:
			self.result.append(subset.copy())
			return 
		for i in range(index, len(nums)):
			subset.append(nums[i])
			self.dfs(nums, k, subset, i+1)
			subset.pop()
