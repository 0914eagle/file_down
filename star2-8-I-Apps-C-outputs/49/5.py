
N, L = map(int, input().split())
a = list(map(int, input().split()))
c = list(map(int, input().split()))

a_sorted = sorted(a)
c_sorted = sorted(c)

store_1 = [a_sorted.pop(), c_sorted.pop()]
store_2 = [a_sorted.pop(), c_sorted.pop()]

while len(a_sorted) > 0:
    a_min = a_sorted.pop()
    c_min = c_sorted.pop()
    if store_1[0] < store_2[0]:
        store_1 = [a_min, c_min]
    else:
        store_2 = [a_min, c_min]

P1 = store_1[1] / store_1[0]
P2 = store_2[1] / store_2[0]
print(f"{P1 * P2:.3f}")

