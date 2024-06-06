
import sys
import math

def main():
    nrcnm = list(map(int,input().split()))
    n_r,n_c,n,m = nrcnm
    n_file = n + m
    file_info = []
    for i in range(n_file):
        file_info.append(list(map(int,input().split())))
    #print(n_r,n_c,n,m,file_info)
    #print(n_file)
    file_info.sort(key = lambda x:(x[1],x[0]))
    #print(file_info)
    stack = []
    for i in range(n_file):
        if len(stack) == 0:
            stack.append(file_info[i])
        else:
            if file_info[i][0] - stack[-1][0] < 15 and file_info[i][1] - stack[-1][1] < 9:
                stack.pop()
                stack.append(file_info[i])
            else:
                stack.append(file_info[i])
    #print(stack)
    stack.reverse()
    stack = [x[0] for x in stack]
    #print(stack)
    dp = [[0] * (n_c + 1) for _ in range(n_file + 1)]
    for i in range(n_file + 1):
        dp[i][0] = 0
    for i in range(n_c + 1):
        dp[0][i] = 0
    for i in range(1,n_file + 1):
        for j in range(1,n_c + 1):
            dp[i][j] = dp[i - 1][j]
            if j - (stack[i - 1] + 9) >= 0:
                dp[i][j] = max(dp[i][j],dp[i - 1][j - (stack[i - 1] + 9)] + 1)
    print(n_file - dp[n_file][n_c])
    
    
if __name__ == "__main__":
    main()
