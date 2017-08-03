''' Given an array of size n-1 and given that there are numbers from 1 to n with one missing, 
	the missing number is to be found '''

def missing_element(arr, size):
	arr.sort()
	for index in xrange(size-1):
		if (arr[index+1]-arr[index] > 1):
			print (arr[index] + 1)

missing_element([2,3,6,4],4)