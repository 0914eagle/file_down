
# k_longest_prefix_strings.py

def longest_common_prefix_strings(A):
    s = [f'{"a"*A[0]}{"b"*A[1]}']
    for i in range(1, len(A) - 1):
        s.append(f'{"a"*(A[i] - A[i - 1])}')
    s.append(f'{"b"*(A[-1])}')
    return s

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        A = list(map(int, input().split()))
        print(*longest_common_prefix_strings(A), sep='\n')
