
from collections import deque


class HR:
    def __init__(self, id):
        self.id = id
        self.fired = deque()

    def fire(self, fired):
        self.fired.append(fired)

    def hire(self):
        return self.fired.popleft()


def solution(n, firing, hiring):
    hired = [0] * n
    hrs = [HR(i + 1) for i in range(n)]
    num_hrs = 0
    for i in range(n):
        fired = firing[i]
        hired[i] = hiring[i]
        if fired > 0:
            num_hrs = max(num_hrs, i + 1)
            hrs[i].fire(fired)
        if hired[i] > 0:
            num_hrs = max(num_hrs, i + 1)
            hired[i] = hrs[i].hire()

    return num_hrs, hired


if __name__ == "__main__":
    n = int(input())
    firing = []
    hiring = []
    for _ in range(n):
        f, h = map(int, input().split())
        firing.append(f)
        hiring.append(h)

    num_hrs, hired = solution(n, firing, hiring)
    print(num_hrs)
    print(" ".join(map(str, hired)))


