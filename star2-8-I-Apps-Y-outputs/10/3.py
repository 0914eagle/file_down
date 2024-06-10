
A, B, C = map(int, input().split())
print("YES" if (C + A - 1) % B <= A - 1 else "NO")

