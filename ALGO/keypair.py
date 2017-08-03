''' Given an array A[] of n numbers and another number x,
 determine whether or not there exist two elements in A whose sum is exactly x.'''

def keypair(arr,num):
	new_arr = [x for x in arr if x < num]
	exist = False
	for n in  new_arr:
		if (num - n) in new_arr and n != (num-n):
			exist = True
	print exist


if __name__ == '__main__':
	num = int(raw_input().strip())
	arr = map(int,raw_input().strip().split())
	keypair(arr,num)