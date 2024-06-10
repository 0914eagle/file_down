
def solve(n, c, w):
    max_fruits = 0
    curr_fruits = 0
    for fruit_weight in w:
        if fruit_weight <= c:
            max_fruits += 1
            c -= fruit_weight
        else:
            break
    return max_fruits


if __name__ == "__main__":
    n, c = map(int, input().split())
    w = list(map(int, input().split()))
    print(solve(n, c, w))

