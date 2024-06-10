
def solve(n, m, words):
    return "No"

def main():
    n, m = map(int, input().split())
    words = []
    for i in range(n):
        l, *s = map(int, input().split())
        words.append((l, s))
    print(solve(n, m, words))

if __name__ == "__main__":
    main()

