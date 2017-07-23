#'python2'
import sys

def lcm_naive(a, b):
	return (a*b)/gcd_naive(a, b)
 
def gcd_naive(a, b):
	if b>a: a,b = b,a
	if b == 0:
		return a
	else:
		a_rem = a%b
		return gcd_naive(b,a_rem)


if __name__ == '__main__':
    a,b = map(int,raw_input().strip().split(" "))
    print(lcm_naive(a, b))

