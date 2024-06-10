
def solve(n, b):
    return " ".join(map(str, b))

if __name__ == "__main__":
    n = int(input())
    b = list(map(int, input().split()))
    print(solve(n, b))

