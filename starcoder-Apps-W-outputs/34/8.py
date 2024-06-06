
from sys import stdin, stdout

def main():
    n = int(stdin.readline())
    data = [stdin.readline().strip().split() for _ in range(n)]
    data.sort(key=lambda x: x[1] == "1")

    res = []
    for i, d in enumerate(data):
        res.append(f"move {d[0]} {i + 1}")

    stdout.write(f"{len(res)}\n")
    stdout.write("\n".join(res))

if __name__ == "__main__":
    main()
