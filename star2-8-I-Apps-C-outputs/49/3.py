
n, l = list(map(int, input().split()))
a = list(map(int, input().split()))
c = list(map(int, input().split()))
a.sort(reverse=True)
c.sort(reverse=True)
min_prod = 1e10
for i in range(n-l+1):
    store_1 = sum(a[:i])
    store_2 = sum(a[i:])
    price_1 = sum(c[:i]) / store_1
    price_2 = sum(c[i:]) / store_2
    min_prod = min(min_prod, price_1 * price_2)

print(min_prod)

