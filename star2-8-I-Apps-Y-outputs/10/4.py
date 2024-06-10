
A, B, C = map(int, input().split())

if C % B == 0:
    print("YES" if A % B == 0 else "NO")
else:
    print("YES" if C % B == A % B else "NO")

