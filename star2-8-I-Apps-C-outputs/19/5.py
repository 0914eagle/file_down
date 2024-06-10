
import sys
n = int(input())
dict = set([input() for i in range(n)])
start,end = input(),input()
if start not in dict or end not in dict:
    print(0)
    print(-1)
    exit()
dict.add(end)
queue = [(start,0)]
visited = set()
visited.add(start)
while len(queue) > 0:
    word,step = queue.pop(0)
    if word == end:
        print(end)
        print(step)
        exit()
    for i in range(len(word)):
        for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            new = word[:i] + c + word[i+1:]
            if new in dict and new not in visited:
                queue.append((new,step+1))
                visited.add(new)
print(0)
print(-1)

