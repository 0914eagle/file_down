
def solve(X, Y, Z):
    return (X - 2*Z) // (Y + Z)

if __name__ == "__main__":
    X, Y, Z = map(int, input().split())
    print(solve(X, Y, Z))
