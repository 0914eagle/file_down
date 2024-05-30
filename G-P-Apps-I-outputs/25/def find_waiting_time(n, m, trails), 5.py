
def find_waiting_time(n, m, trails):
    adj_list = [[] for _ in range(n)]
    for u, v, d in trails:
        adj_list[u].append((v, d))
        adj_list[v].append((u, d))
    
    INF = float('inf')
    dist_day = [INF] * n
    dist_knight = [INF] * n
    
    dist_day[0] = 0
    dist_knight[0] = 0
    
    day_queue = [(0, 0)]  # (time, node)
    knight_queue = [(0, 0)]  # (time, node)
    
    while day_queue or knight_queue:
        for _ in range(len(day_queue)):
            time_d, node_d = day_queue.pop(0)
            for neighbor, duration in adj_list[node_d]:
                new_time = time_d + duration
                if new_time <= 12 and new_time < dist_day[neighbor]:
                    dist_day[neighbor] = new_time
                    day_queue.append((new_time, neighbor))
        
        for _ in range(len(knight_queue)):
            time_k, node_k = knight_queue.pop(0)
            for neighbor, duration in adj_list[node_k]:
                new_time = time_k + duration
                if new_time <= 12 and new_time < dist_knight[neighbor]:
                    dist_knight[neighbor] = new_time
                    knight_queue.append((new_time, neighbor))
    
    return max(dist_day[n-1] - 1, dist_knight[n-1])

# Reading input
n, m = map(int, input().split())
trails = [list(map(int, input().split())) for _ in range(m)]

# Calculating waiting time
waiting_time = find_waiting_time(n, m, trails)
print(waiting_time)
```
