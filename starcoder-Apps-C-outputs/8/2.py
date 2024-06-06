
import queue

def main():
    n, m = map(int, input().split())
    puton = list(map(int, input().split()))
    remove = list(map(int, input().split()))
    get = []
    for _ in range(n):
        c, t = map(int, input().split())
        get.append((t, c))
    get.sort()

    que = queue.PriorityQueue()
    que.put((0, 0))
    for time, cloth in get:
        while not que.empty() and que.queue[0][0] < time:
            que.get()
        if que.qsize() == m:
            continue
        cloth -= 1
        if not que.empty():
            (end, cl) = que.get()
            end += remove[cl]
            que.put((end, cl))
        que.put((time + puton[cloth], cloth))
    print(que.qsize())

main()
