# 'python2'
''' The goal of this code problem is to implement an algorithm for the fractional knapsack problem.
    The first line of the input contains the number n of items and the capacity W of a knapsack.
    The next n lines define the values and weights of items
    Output the maximal value of fractions of items that fit into the knapsack. '''

import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    fraction = []
    for i in xrange(len(weights)):
    	fraction.append([i,values[i]/float(weights[i])])
    fraction = sorted(fraction, key = lambda x: x[1], reverse = True)
    #fraction is a list sorted according to maximum value/weight ratio
    for f in fraction:
        # if knapsack is full, return the value
        if capacity == 0:
            return value
        #index is used to keep track of weight of current item
        index = f[0]
        # iterate untill item is finished
        while weights[index]>0:
            #taking the minimum of weight or capacity
            a = min(weights[index],capacity)
            #adding value by the fraction of value of item taken
            value += a*f[1]
            #decreasing weight and capacity 
            weights[index] -= a
            capacity -= a
            if capacity == 0:
                return value
    
    return value    

if __name__ == "__main__":
    items, capacity = map(int, raw_input().split())
    values = []
    weights = []
    for _ in xrange(items):
    	value,weight = map(int, raw_input().split())
    	values.append(value)
    	weights.append(weight)

    opt_value =  (get_optimal_value(capacity, weights, values))
    
    print("{:.10f}".format(opt_value))
 
