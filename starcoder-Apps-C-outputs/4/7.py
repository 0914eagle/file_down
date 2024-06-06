
N = int(input())
balls = [list(input().split()) for _ in range(2*N)]
nums = [list(map(int, [balls[i][1], balls[i][0]])) for i in range(2*N)]
nums.sort(reverse = True)

ans = 0
for i in range(N):
    # 白と黒の数が正しくなっていないところは1回で直せる
    if nums[i][1] == 'B':
        ans += 1
    if nums[N+i][1] == 'W':
        ans += 1
print(ans)
