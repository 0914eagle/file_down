
def solve(N, L, a, c):
    a_sum = sum(a)
    a_sum_div_L = a_sum // L
    c_div_a = [c[i] / a[i] for i in range(N)]
    c_div_a_sorted = sorted(c_div_a)
    P1 = P2 = 0
    for i in range(L):
        P1 += c_div_a_sorted[i]
    for i in range(L, N):
        P2 += c_div_a_sorted[i]
    P1 /= L
    P2 /= (N - L)
    return P1 * P2

