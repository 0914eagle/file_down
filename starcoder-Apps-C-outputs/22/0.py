
class Solution:
	def getMin(self, n, m, h, A, C):
		# Write your code here
		n, m, h = map(int, input().split())
		A = list(map(int, input().split()))
		C = [list(map(int, input().split())) for _ in range(m)]
		x = []
		d = []
		for i in range(n):
			for j in range(n):
				if j != i:
					if A[i] == A[j]:
						x.append(i+1)
						x.append(j+1)
		for i in x:
			if i not in d:
				d.append(i)
		x = []
		for i in d:
			for j in range(m):
				if C[j][0] == i:
					x.append(C[j][1])
				if C[j][1] == i:
					x.append(C[j][0])
		print(len(d))
		print(*d)


if __name__ == '__main__':
    s = Solution()
    n = int(input())
    m = int(input())
    h = int(input())
    A = list(map(int, input().split()))
    C = [list(map(int, input().split())) for _ in range(m)]
    s.getMin(n, m, h, A, C)
