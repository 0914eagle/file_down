
from typing import List

def solve(x: int) -> List[int]:
    result = [0] * 9
    while x > 0:
        result[x % 10 - 1] += 1
        x //= 10
    return result

def add(a: List[int], b: List[int]) -> List[int]:
    return [a[i] + b[i] for i in range(9)]

def calculate(x: int) -> List[int]:
    result = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    while x > 0:
        result = add(solve(x), result)
        x -= 1
    return result

def main():
    l, r = map(int, input().split())
    if l == r:
        print(" ".join(map(str, solve(l))))
    else:
        print(" ".join(map(str, add(calculate(r), solve(l - 1)))))

if __name__ == "__main__":
    main()
