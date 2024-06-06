
'''
The first line contains two space-separated integers N (1 ≤ N ≤ 10^5) — the total number of tasks given, and M (0 ≤ M ≤ 10^5) — the total number of dependencies between tasks.

The next line contains N space-separated integers $E_{i} \in \{0,1 \}$. If E_{i} = 0, task i can only be executed on the main processor, otherwise it can only be executed on the coprocessor.

The next M lines describe the dependencies between tasks. Each line contains two space-separated integers T_1 and T_2 and means that task T_1 depends on task T_2 (T_1 ≠ T_2). Tasks are indexed from 0 to N - 1. All M pairs (T_1, T_2) are distinct. It is guaranteed that there are no circular dependencies between tasks.

Output one line containing an integer — the minimal number of coprocessor calls necessary to execute the program.
'''

def solution():
    n, m = map(int, input().split())
    tasks = list(map(int, input().split()))
    dp = [[0]*2 for _ in range(n)]
    for _ in range(m):
        i, j = map(int, input().split())
        dp[i][0] = max(dp[i][0], dp[j][0]+1)
        dp[i][1] = max(dp[i][1], dp[j][1]+1)
    ans = 0
    for i in range(n):
        ans += max(dp[i][tasks[i]], 1)
    return ans

print(solution())
