
def choose_vouchers(n, x, vouchers):
    vouchers.sort(key=lambda v: v[2])
    min_cost = float('inf')
    
    for i in range(n):
        for j in range(i+1, n):
            if vouchers[i][1] < vouchers[j][0] or vouchers[j][1] < vouchers[i][0]:
                total_duration = (vouchers[i][1] - vouchers[i][0] + 1) + (vouchers[j][1] - vouchers[j][0] + 1)
                if total_duration == x:
                    min_cost = min(min_cost, vouchers[i][2] + vouchers[j][2])
    
    return min_cost if min_cost != float('inf') else -1

# Input
n, x = map(int, input().split())
vouchers = [list(map(int, input().split())) for _ in range(n)]

# Output
result = choose_vouchers(n, x, vouchers)
print(result)
