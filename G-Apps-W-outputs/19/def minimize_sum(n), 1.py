
def minimize_sum(n):
    result = []
    for i in range(1, n + 1):
        result.append(i)
        result.append(i)
    return result

n = int(input())
result = minimize_sum(n)
print(*result)
