def majority(arr,size):
	min_count = size/2
	num_dict = {}
	for num in arr:
		if num not in num_dict:
			num_dict[num] = 1
		else:
			num_dict[num] += 1
	for key,value in num_dict.items():
		if value > min_count:
			return key
	return "Sorry"


print (majority([2,2,1,1,1],5))