
import heapq

def expected_total_severity(B, T, f, bugs):
    bugs.sort(key=lambda x: x[1], reverse=True)  # Sort bugs by severity in descending order
    pq = [(-bugs[i][0], i, bugs[i][1]) for i in range(B)]  # Initialize priority queue with (-fix probability, bug index, severity)
    heapq.heapify(pq)
    total_severity = 0

    for _ in range(T):
        if not pq:
            break

        prob, idx, severity = heapq.heappop(pq)
        prob *= -1  # Get fix probability
        total_severity += prob * severity

        prob *= f  # Reduce fix probability after failure
        heapq.heappush(pq, (-prob, idx, severity))

    return total_severity

# Input processing
B, T, f = map(float, input().split())
B = int(B)
T = int(T)
bugs = []
for _ in range(B):
    p, s = map(float, input().split())
    bugs.append((p, int(s)))

result = expected_total_severity(B, T, f, bugs)
print('{:.6f}'.format(result))
