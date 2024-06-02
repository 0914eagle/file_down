
def choose_vouchers(n, x, vouchers):
    min_cost = float('inf')
    
    for i in range(n):
        for j in range(i+1, n):
            if vouchers[i][1] < vouchers[j][0] or vouchers[j][1] < vouchers[i][0]:
                if vouchers[i][2] + vouchers[j][2] < min_cost and vouchers[i][1] - vouchers[i][0] + vouchers[j][1] - vouchers[j][0] == x:
                    min_cost = vouchers[i][2] + vouchers[j][2]
    
    if min_cost == float('inf'):
        return -1
    else:
        return min_cost

# Input parsing
n, x = map(int, input().split())
vouchers = []
for _ in range(n):
    l, r, cost = map(int, input().split())
    vouchers.append((l, r, cost))

# Call the function and print the result
result = choose_vouchers(n, x, vouchers)
print(result)
