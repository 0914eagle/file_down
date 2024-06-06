

n,s,m,k = map(int,input().split())

arr = list(map(int,input().split()))

arr = arr[::-1]

arr_list = []

for i in range(n):
    arr_list.append([i+1,arr[i]])

arr_list = sorted(arr_list,key=lambda x: x[1])

# print(arr_list)

arr_dict = {arr_list[0][1]:[arr_list[0][0]]}

for i in range(1,len(arr_list)):
    if arr_list[i][1] in arr_dict:
        arr_dict[arr_list[i][1]].append(arr_list[i][0])
    else:
        arr_dict[arr_list[i][1]] = [arr_list[i][0]]

# print(arr_dict)

sub_arr = []

for i in range(s):
    l,r = map(int,input().split())
    sub_arr.append([l,r])

dp = [[0 for i in range(m+1)] for j in range(s+1)]

# print(dp)

for i in range(1,s+1):
    for j in range(1,m+1):
        dp[i][j] = dp[i-1][j]
        for x in range(sub_arr[i-1][0],sub_arr[i-1][1]+1):
            if x in arr_dict:
                for y in arr_dict[x]:
                    if y in dp[i-1][j-1]:
                        dp[i][j] = max(dp[i][j],dp[i-1][j-1][y]+1)

# print(dp)

if dp[s][m]>=k:
    print(arr_list[k-1][1])
else:
    print(-1)

