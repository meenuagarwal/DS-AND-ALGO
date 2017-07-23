# 'python2'
import sys

length = int(raw_input().strip())
num = map(int,raw_input().strip().split(" "))

num.sort(reverse = True)
print (num[0]*num[1])