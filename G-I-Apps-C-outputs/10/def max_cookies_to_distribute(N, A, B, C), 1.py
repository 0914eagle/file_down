
def max_cookies_to_distribute(N, A, B, C):
    total_cookies = A + B + C
    max_cookies_per_person = total_cookies // 2
    cookies_to_distribute = min(N, max_cookies_per_person)
    return cookies_to_distribute * 2

# Input
input_line = input().strip().split()
N = int(input_line[0])
A = int(input_line[1])
B = int(input_line[2])
C = int(input_line[3])

# Output
print(max_cookies_to_distribute(N, A, B, C))
```
