
import sys

def query(id, m):
    h = m[id][2]
    min_s = 1000000000000000000
    min_id = -1
    for id1, (s, h1) in m.items():
        if s < m[id][0] and h1 >= h and s < min_s:
            min_s = s
            min_id = id1
    return min_id

def main():
    m = dict()
    q = dict()
    n, q_num = map(int, input().split())
    for _ in range(n):
        id, s, h = map(int, input().split())
        m[id] = (s, h)
    for _ in range(q_num):
        q[int(input())] = None
    
    for id in q:
        boss_id = query(id, m)
        if boss_id != -1:
            q[id] = (boss_id, 0)
    
    for id, (boss_id, num) in q.items():
        for id1, (s, h) in m.items():
            if s > m[id][0] and h >= m[id][2] and id1 != id and id1 != boss_id:
                q[id] = (boss_id, num + 1)
    
    for id, (boss_id, num) in q.items():
        print(boss_id, num)

if __name__ == '__main__':
    main()

