''' Assembly Line Scheduling program using Dynamic Programming.
	2 ALs, N station for every AL denoted by S(i,j) where i refers to the AL and j refers to station number.
	Time taken at any station is denoted as a(i,j) and time taken to switch from j-1 to
	j station is 0 if it happens on same AL , otherwise t(i,j) when you switch AL as well. '''

def car_assembly(a,t,e,x,n):
	
	#M(i) stroes the minimum tike taken to leave station (i+1).
	M1 = [0]*(n)
	M2 = [0]*(n)
	
	#Base case: Time taken to leave first station is entry time + time spent at 1st station
	M1[0] = e[0] + a[0][0]
	M2[0] = e[1] + a[1][0]

	#Using Bottom-up approach
	for i in xrange(1,n):
		M1[i] = min(M1[i-1] + a[0][i] , M2[i-1] + a[0][i] + t[1][i])
		M2[i] = min(M2[i-1] + a[1][i] , M1[i-1] + a[1][i] + t[0][i])
	
	return min(M1[n-1] + x[0] , M2[n-1] + x[1])

if __name__=='__main__':
	a = [[4,5,3,2],[2,10,1,4]]
	t = [[0,7,4,5],[0,9,2,8]]
	e = [10,12]
	x = [18,7]
	print car_assembly(a,t,e,x,4)