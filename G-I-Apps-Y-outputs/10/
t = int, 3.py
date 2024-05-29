
t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    s = input()
    p = list(map(int, input().split()))
    
    presses = [0] * 26
    presses_count = [0] * 26
    total = 0
    for i in range(m):
        presses_count[ord(s[p[i]-1]) - ord('a')] += 1
        total += 1
    
    for i in range(26):
        presses[i] = presses_count[i]
    
    for i in range(n):
        presses[ord(s[i]) - ord('a')] += total
        
    print(" ".join(map(str, presses)))
