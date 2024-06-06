

def optimal_strategy(N,P,en,p):
	dp = [[0 for i in range(N+1)] for j in range(N+1)]
	# dp[i][j] is the minimum energy required to find the parrot with at least p probability while 
	# considering boxes from i to j
	for gap in range(N):
		for i in range(1,N-gap+1):
			j = i + gap
			if i == j:
				if p[i] >= P:
					dp[i][j] = 0
				else:
					dp[i][j] = 1e9
			else:
				temp1 = 0
				temp2 = 0
				if p[i] >= P:
					temp1 = dp[i+1][j]
				else:
					temp1 = dp[i+1][j] + en[i]

				if p[j] >= P:
					temp2 = dp[i][j-1]
				else:
					temp2 = dp[i][j-1] + en[j]

				dp[i][j] = min(temp1,temp2)
	return dp[1][N]


N,P = map(float,input().split())
N = int(N)
p = []
en = []
for i in range(N):
	x,y = map(float,input().split())
	en.append(int(x))
	p.append(y)

print(int(optimal_strategy(N,P,en,p)))

