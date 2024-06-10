
from collections import defaultdict


def solve(n, a):
    if n == 2 and a[0] == a[1]:
        return "NO"
    adj_list = defaultdict(list)
    for i in range(n - 1):
        adj_list[a[i]].append(i + 1)
    result = "YES\n"
    for key in adj_list:
        if len(adj_list[key]) > 1:
            for i in range(len(adj_list[key]) - 1):
                result += f"{adj_list[key][i]} {adj_list[key][i + 1]}\n"
    return result


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        print(solve(n, a))

