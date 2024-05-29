
from queue import PriorityQueue

def final_health_of_last_monster(N, A):
    pq = PriorityQueue()

    for a in A:
        pq.put(a)

    while pq.qsize() > 1:
        a = pq.get()
        b = pq.get()

        if a != b:
            pq.put(abs(a - b))

    return pq.get()

# Read input from Standard Input
N = int(input())
A = list(map(int, input().split()))

# Call the function and print the output
print(final_health_of_last_monster(N, A))
