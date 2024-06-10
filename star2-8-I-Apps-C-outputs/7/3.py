
S = input()
T = [input().split() for i in range(26)]
K = int(input())
M = int(input())
m = list(map(int,input().split()))
for i in range(M):
    pos = m[i]
    for j in range(K):
        prev = pos
        for ch in S:
            pos += (ord(ch)-ord('a')+1)*len(T[ord(ch)-ord('a')])
        pos -= prev
        if pos <= len(S):
            print(S[pos-1])
            break
        pos -= len(S)
        for ch in range(26):
            if pos <= len(T[ch])*len(S):
                print(T[ch][(pos-1)//len(S)])
                break
            pos -= len(T[ch])*len(S)

