
def reconstruct_order(n, a):
    order = [0] * n
    for i in range(n):
        order[a[i] - 1] = i + 1
    return order


n = int(input())
a = list(map(int, input().split()))

order = reconstruct_order(n, a)
print(*order)

