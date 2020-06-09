"""
Two-Pointer method is one of the most commonly used algorithms. The two pointers can be in the same direction or in opposite directions. This method is usually used to solve linear data structures, such as arrays and linked lists. The two pointers can also be at different arrays. 

classic problems:
1. Two pointers in opposite directions:
	i. 2Sum, 3Sum, 4Sum, Trapping rain water, 
	ii. partition, quickSort, quickSelect, valid Palindrome
2. In the same directions:
	minimum size subarray sum, 
3. Two arrays, two pointers


"""

# 4Sum: Given an array and a target, find all the combinations of 4 numbers in the list to have a sum equal to the target value.
# eg. Input:[1,0,-1,0,-2,2],0
# Output:
# [[-1, 0, 0, 1]
# ,[-2, -1, 1, 2]
# ,[-2, 0, 0, 2]]

def fourSum(numbers, target):
	numbers.sort()
	result = []
	for i in range(len(numbers) - 3):
		if i and numbers[i] == numbers[i - 1]:
			continue
		for j in range(i + 1, len(numbers) - 2):
			if j > i + 1 and numbers[j] == numbers[j - 1]:
				continue
			left, right = j + 1, len(numbers) - 1
			while left < right:
				sum = numbers[i] + numbers[j] + numbers[left] + numbers[right]
				if sum == target:
					result.append([numbers[i], numbers[j], numbers[left], numbers[right]])
					left += 1
					right -= 1
					while left < right and numbers[left] == numbers[left - 1]:
						left += 1
					while left < right and numbers[right] == numbers[right + 1]:
						right -= 1
				elif sum < target:
					left += 1
				else:
					right -= 1
	return result
	

# Partition
def partition(array, low, high):
    pivot = array[high]
    index = low
    for i in range(low, high):
        if array[i] < pivot: 
            array[i], array[index] = array[index], array[i]
            index = index + 1
    array[index], array[high] = array[high], array[index]
    return index

# Minimum size subarray: Given an array of n positive integers and a positive integer s, find the minimum length of the contiguous subarray of which the sum >= s, if there isn't one, return 0
# The solution to this problem with time O(n^2) is not that hard to come out. We just need to find all the contiguous subarrays. By using two pointers, we can avoid some cases that are 

