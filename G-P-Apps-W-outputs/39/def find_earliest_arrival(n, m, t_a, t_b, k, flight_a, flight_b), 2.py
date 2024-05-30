
import sys

def find_earliest_arrival(n, m, t_a, t_b, k, flight_a, flight_b):
    min_time = float('inf')
    for i in range(k+1):
        if i > n or k-i > m:
            continue
        possible_arrival_times = []
        for j in range(i+1):
            if i == 0 or j == i:
                possible_arrival_times.append(flight_a[j] + t_a + t_b)
            else:
                possible_arrival_times.append(max(flight_a[j] + t_a, flight_b[k-i+j]))
        min_time = min(min_time, max(possible_arrival_times))
    return min_time if min_time != float('inf') else -1

if __name__ == "__main__":
    n, m, t_a, t_b, k = map(int, input().split())
    flight_a = list(map(int, input().split()))
    flight_b = list(map(int, input().split()))

    result = find_earliest_arrival(n, m, t_a, t_b, k, flight_a, flight_b)
    print(result)
