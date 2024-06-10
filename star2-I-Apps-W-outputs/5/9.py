
n = int(input())
requests = list(map(int, input().split()))

left = 0
right = 0
max_length = 0
total_requests = 0
while right < n:
    total_requests += requests[right]
    while total_requests > 100 * (right - left + 1):
        total_requests -= requests[left]
        left += 1
    max_length = max(max_length, right - left + 1)
    right += 1

print(max_length)

