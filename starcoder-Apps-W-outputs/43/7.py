
n = int(input())
current_time = 0
max_queue_size = 0
total_sent = 0

while n > 0:
    t, c = map(int, input().split())
    queue = c
    while queue > 0:
        total_sent += 1
        current_time += 1
        queue -= 1
        max_queue_size = max(max_queue_size, total_sent)
    n -= 1
    
print(current_time, max_queue_size)
