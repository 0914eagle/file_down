
def calculate_payment_difference(N):
    x = N * 800
    y = (N // 15) * 200
    return x - y

N = int(input())
result = calculate_payment_difference(N)
print(result)
