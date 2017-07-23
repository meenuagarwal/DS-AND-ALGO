# 'python2'
import sys

def get_fibonacci_last_digit_naive(n):
    fib = [0,1]
    for i in xrange(2,n+1):
        num = (fib[i-1] + fib[i-2])%10
        fib.append(num)
    return fib[n]

if __name__ == '__main__':
    input = int(raw_input().strip())
   
    print(get_fibonacci_last_digit_naive(input))
