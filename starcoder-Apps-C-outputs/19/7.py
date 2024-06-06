
class Clock:
    def __init__(self, time):
        self.time = time
        self.visited = set()

    def dfs(self, time, count):
        if time == self.time:
            return count
        if time in self.visited:
            return -1
        self.visited.add(time)

        h1 = int(time[0])
        h2 = int(time[1])
        m1 = int(time[3])
        m2 = int(time[4])
        # h1
        count = self.dfs(str(self.modify(h1, 1)) + time[1:] , count + 1)
        count = self.dfs(str(self.modify(h1, -1)) + time[1:] , count + 1)
        # h2
        count = self.dfs(time[0] + str(self.modify(h2, 1)) , count + 1)
        count = self.dfs(time[0] + str(self.modify(h2, -1)) , count + 1)
        # m1
        count = self.dfs(time[:3] + str(self.modify(m1, 1)) , count + 1)
        count = self.dfs(time[:3] + str(self.modify(m1, -1)) , count + 1)
        # m2
        count = self.dfs(time[:4] + str(self.modify(m2, 1)) , count + 1)
        count = self.dfs(time[:4] + str(self.modify(m2, -1)) , count + 1)

        return count

    def modify(self, time, direction):
        if direction == 1:
            time = (time + 1) % 10
        else:
            time = (time - 1) % 10
        return time


if __name__ == "__main__":
    s = input()
    e = input()
    clock = Clock(s)
    count = clock.dfs(e, 1)
    print(count)
