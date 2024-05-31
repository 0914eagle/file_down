
def is_possible_to_one_element(n, a):
    max_count = max(a.count(num) for num in set(a))
    if max_count >= (n + 1) // 2:
        return "YES"
    return "NO"

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(is_possible_to_one_element(n, a))
