#'python2'
''' Maximizing Revenue in Online Ad Placement 
    The first line contains no. of slots (equal to no. of ads) for page.
    The second contains profit per click and third line contains no. of clicks for the slot.
    Goal is to distribute the ads among the slots to maximize the total revenue.'''

import sys

def max_dot_product(a, b):
    res = 0
    a.sort(reverse = True)
    b.sort(reverse = True)
    for i in range(len(a)):
        res += a[i] * b[i]
    return res

if __name__ == '__main__':
    items = map(int,raw_input().strip().split()) #no. of slots
    a = map(int,raw_input().split()) #profit per click for each ad
    b = map(int,raw_input().split()) #no. of clicks per slot
    print(max_dot_product(a, b))
    
