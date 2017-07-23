#'python2'
import sys

n = int(raw_input().strip())
fib = [0,1]
for i in xrange(2,n+1):
	num = fib[i-1] + fib[i-2]
	fib.append(num)
print(fib[n])
