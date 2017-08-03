'''Given an array containing both negative and positive integers. 
	Find the contiguous sub-array with maximum sum.'''

def seq_array(arr):
	powerset = []
	max_sum = arr[0]
	for i in xrange(len(arr) + 1):
		for j in xrange(i):
			if arr[j:i] not in powerset:
				powerset.append(arr[j:i])
			new_sum = sum(arr[j:i])
			if new_sum > max_sum :
				max_sum = new_sum
	print max_sum


if __name__ == '__main__':
	seq_array([-10,4,5])