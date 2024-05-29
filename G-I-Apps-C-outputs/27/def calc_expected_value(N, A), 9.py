
def calc_expected_value(N, A):
    MOD = 1000000007

    dp_sum = [0] * (N + 1)
    dp_count = [0] * (N + 1)
    dp_sum[0] = 1

    for i in range(1, N + 1):
        for j in range(1, A[i - 1] + 1):
            new_dp_sum = [0] * (N + 1)
            new_dp_count = [0] * (N + 1)

            for k in range(1, N + 1):
                new_dp_sum[k] = (new_dp_sum[k] + dp_sum[k] * min(j, k)) % MOD
                new_dp_sum[k] = (new_dp_sum[k] + dp_count[k] * (k + 1)) % MOD

                if j == k:
                    new_dp_count[k] = (new_dp_count[k] + dp_count[k]) % MOD

            dp_sum = new_dp_sum
            dp_count = new_dp_count

    expected_sum = sum(dp_sum[1:]) % MOD
    expected_count = sum(dp_count[1:]) % MOD

    expected_value = pow(expected_sum * pow(expected_count, MOD - 2, MOD) % MOD, 1, MOD)
    return expected_value

N = int(input())
A = list(map(int, input().split()))
print(calc_expected_value(N, A))
