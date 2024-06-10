
A, B, C = map(int, input().split())
if C % B == 0:
    print("YES" if A % B == C % B else "NO")
else:
    print("YES" if C % B == (C + A) % B else "NO")

