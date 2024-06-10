

k, n_1, n_2, n_3, t_1, t_2, t_3 = map(int, input().split())

washing_time = t_1 * k
drying_time = (washing_time + t_2 * n_2 - 1) // n_2
folding_time = (drying_time + t_3 * n_3 - 1) // n_3

print(folding_time)


