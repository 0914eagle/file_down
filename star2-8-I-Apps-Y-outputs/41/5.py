
from sys import stdin, stdout
def solve(n, k, p, q):
    p_count = [0] * 26
    q_count = [0] * 26
    for x in p:
        p_count[ord(x) - ord('a')] += 1
    for x in q:
        q_count[ord(x) - ord('a')] += 1
    
    p_sum = [p_count[0]]
    q_sum = [q_count[0]]
    for i in range(1, 26):
        p_sum.append(p_sum[-1] + p_count[i])
        q_sum.append(q_sum[-1] + q_count[i])
    
    if p_sum[-1] < k or q_sum[-1] < k:
        stdout.write("NO\n")
        return
    
    ans = ['a'] * n
    for i in range(n):
        x = ord(p[i]) - ord('a')
        y = ord(q[i]) - ord('a')
        if p_count[x] + q_count[x] > k:
            stdout.write("NO\n")
            return
        
        if p_count[x] >= q_count[x]:
            ans[i] = chr(x + ord('a'))
        else:
            ans[i] = chr(y + ord('a'))
        
        p_count[x] -= 1
        q_count[y] -= 1
    
    stdout.write("YES\n")
    stdout.write("".join(ans) + "\n")
def main():
    input = stdin.readline
    n, k = map(int, input().split())
    p = input().strip()
    q = input().strip()
    
    solve(n, k, p, q)
main()

