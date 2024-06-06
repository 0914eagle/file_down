
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
from collections import deque
N = int(raw_input().strip())
adj_list = defaultdict(list)
numbers = defaultdict(list)

for _ in range(N):
    numbers_lst = map(int, raw_input().strip().split())
    numbers_lst.pop(0)
    for number in numbers_lst:
        adj_list[number].append(_)
        numbers[number].append(_)

def bfs(start, end):
    visited = set()
    queue = deque([(start, 0)])
    visited.add(start)
    while queue:
        vertex, count = queue.popleft()
        if vertex == end:
            return count
        for neighbour in adj_list[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append((neighbour, count + 1))
    return -1

for num in numbers.keys():
    for node1 in numbers[num]:
        for node2 in numbers[num]:
            if node1 != node2:
                print node1 + 1, node2 + 1, num
                break
