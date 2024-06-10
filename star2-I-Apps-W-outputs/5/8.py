
def ddos(n, requests):
    max_length = 0
    current_length = 0
    current_sum = 0
    for i in range(n):
        current_sum += requests[i]
        current_length += 1
        if current_sum > 100 * current_length:
            current_sum -= requests[i - current_length]
            current_length = 0
        else:
            max_length = max(max_length, current_length)
    return max_length

n = int(input())
requests = list(map(int, input().split()))
print(ddos(n, requests))

