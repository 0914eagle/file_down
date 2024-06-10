
def solve(K: int) -> int:
    even_count = K // 2
    odd_count = K - even_count
    return even_count * odd_count

K = int(input())
print(solve(K))

