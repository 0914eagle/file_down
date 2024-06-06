
def confusion(n, c):
    if n == 1:
        return 1
    if c == 0:
        return pow(n, n-1, 1000000007)
    if n == 2:
        return pow(2, c, 1000000007)
    if c == n-1:
        return 0
    if c >= n-2:
        return pow(n, n-1, 1000000007) - confusion(n, n-2)
    
    if n % 2 == 1:
        return 0
    
    sum = 0
    for i in range(2, n-1):
        if c >= i:
            sum += confusion(i, c-i) * confusion(n-i, i) * pow(2, i-1, 1000000007) * pow(n-i, n-i-1, 1000000007)
            sum %= 1000000007
    return sum
    
n, c = map(int, input().split())
print(confusion(n, c))
