
# Python3 program to find Minimum 
# cost of filling gas tank using 
# minimum number of trips 

# Return minimum cost to fill 
# gas tank 
def minCost(distance, cost, n, gas): 

	# Initialise result 
	res = float("INF") 

	# Consider all points as 
	# starting points 
	for i in range(n): 
		
		# If i'th gas station can't 
		# be starting point 
		if (distance[i] >= gas): 
			continue

		# To store cumulative distance 
		# covered and cost incurred 
		curdis = 0
		curcost = 0

		# Traverse from i'th point to 
		# next possible starting point 
		j = i 
		while (j < n and curdis + distance[j] <= gas): 
		
			# Increment cost and distance 
			curcost += (gas - curdis) * cost[j] 
			curdis += distance[j] 

			# Increment j to next gas 
			# station 
			j += 1

		# If we reached next starting 
		# point, update result 
		if (j < n): 
			curcost += (gas - curdis) * cost[j] 
			res = min(res, curcost) 

	# If result is INF then it 
	# means it is impossible to 
	# fill gas tank 
	if (res == float("INF")): 
		print("cancel road trip") 
	else: 
		print(res) 

# Driver code 
if __name__ == "__main__": 
	distance = [2, 1, 11] 
	cost = [100, 10, 5] 
	n = len(distance) 
	gas = 10
	minCost(distance, cost, n, gas) 

# This code is contributed by 
# (Ashutosh_Raj_Singh) 
