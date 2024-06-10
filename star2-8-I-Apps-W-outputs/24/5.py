
k, n_1, n_2, n_3, t_1, t_2, t_3 = map(int, input().split())
print((k * t_1 + (k - 1) * t_2 + (k - 1) * t_3) // (n_1 * n_2 * n_3))

