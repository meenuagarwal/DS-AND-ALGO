'''  find the minimum number of coins needed to change the input value
(an integer) into coins with denominations 1, 5, and 10. '''
#'python2'
import sys

def get_change(m):
	count = 0 #stores count of coins
	denominations = [10,5,1] #sorted denominations list
	coins = {} #dictionary to store value for each denomination
	weight = m
	for i in xrange(len(denominations)):
		mul = 0 #stores no. of coins for each denominations
		while ((weight - mul*denominations[i]) >= denominations[i]): 
			mul += 1
		weight = weight - mul*denominations[i] #update the weight 
		count += mul #increase count by no. of coins
		coins[denominations[i]] = mul #add denomination and no. of coins to dictionary
		if (weight == 0): #if weight is zero, return count
			print coins
			return count

if __name__ == '__main__':
	m = int(raw_input().strip())
	print(get_change(m))
