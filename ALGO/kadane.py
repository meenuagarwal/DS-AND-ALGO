'''Given an array containing both negative and positive integers. 
	Find the contiguous sub-array with maximum sum.'''

def max_subarray(A):
    max_ending_here = max_so_far = A[0]
    for x in A[1:]:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

print max_subarray([-3,-1,2,4,-6,0])