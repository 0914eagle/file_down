
def solve():
n = int(input())
b = list(map(int, input().split()))
l = [0] * (n + 2)
r = [0] * (n + 2)
for i in range(1, n + 1):
l[i] = max(l[i - 1], b[i - 1])
for i in range(n - 1, 0, -1):
r[i] = max(r[i + 1], b[i - 1])
damage = 0
damage_pos = 0
for i in range(1, n + 1):
if l[i - 1] + r[i + 1] > b[i - 1] and l[i - 1] + r[i + 1] - b[i - 1] > damage:
damage = l[i - 1] + r[i + 1] - b[i - 1]
damage_pos = i - 1
print(damage, damage_pos)


def main():
solve()
if __name__ == "__main__":
main()


