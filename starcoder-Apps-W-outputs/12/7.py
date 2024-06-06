

from sys import stdin

def countSubarrays(arr,n,k,t):
	start, end = 0,0
	res = 0
	curr_sum = 0
	while end<n:
		curr_sum+=arr[end]
		while start<end and curr_sum>t:
			curr_sum-=arr[start]
			start+=1
		if curr_sum<=t:
			rem_elements = n-end
			res+=rem_elements
			if rem_elements>=k:
				res-=rem_elements-k+1
		end+=1
	return res

if __name__ == "__main__":
	n,t,k = [int(i) for i in stdin.readline().split()]
	arr = [int(i) for i in stdin.readline().split()]
	print(countSubarrays(arr,n,k,t))
