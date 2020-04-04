# find the median of an array nums with lenth n, no matter n is odd or even
median = (nums[n // 2] + nums[~(n // 2)]) / 2

# get the column as a list of a 2D matrix. Example board = [[1,2,3], [4,5,6], [7,8,9]]
def get_column(board):
	column_matrix = []
	for col in zip(*board): # The asterisk here is for unpacking the board into rows
		column_matrix.append(col)
	return column_matrix
# The result would be [(1, 4, 7), (2, 5, 8), (3, 6, 9)]


"""
>>> m = [[0] * 4] * 2
>>> m[0][1] = 1
>>> m
	[[0, 1, 0, 0], [0, 1, 0, 0]]
instead of [[0, 1, 0, 0], [0, 0, 0, 0]]

"""


## Count bits
def count_bits(number):
	count = 0
	while a:
		if a & 1:
			count += 1
		a = a >> 1
	return count 
	
## Python Binary Operations
# &: and, 
# |: or, 
# ^: xor,
# ~x: ones complement, same as -x - 1
# x>>y: shift right, same as x // 2**y
# x<<y: shift left, same x * 2**y

# x // 2 is equivalent to x >> 1
# x * 2 is equivalent to x << 1
# check x is power is 2: return x & (x - 1) == 0



