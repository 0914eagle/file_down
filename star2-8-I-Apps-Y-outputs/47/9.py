
n, p, k = map(int, input().split())
ts = list(map(int, input().split()))

def calculate_original_length(n, p, k, ts):
    original_length = 0
    for i in range(n):
        segment_length = ts[i] if i == 0 else ts[i] - ts[i-1]
        speed_factor = (100 + p * i) / 100
        original_length += segment_length / speed_factor
    original_length += (k - ts[-1]) / (100 + p * n)
    return original_length

print(calculate_original_length(n, p, k, ts))

