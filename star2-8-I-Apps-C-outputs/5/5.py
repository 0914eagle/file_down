
class Tree:
    def __init__(self, n, d):
        self.n = n
        self.d = d
        self.tree = [[] for _ in range(n)]

    def build(self, parent, child):
        self.tree[parent].append(child)
        self.tree[child].append(parent)

    def dfs(self, node, parent, distance):
        max_distance = distance
        for child in self.tree[node]:
            if child == parent:
                continue
            max_distance = max(max_distance, self.dfs(child, node, distance + 1))
        return max_distance

    def solve(self):
        max_distance = 0
        for node in range(self.n):
            max_distance = max(max_distance, self.dfs(node, -1, 0))
        return (max_distance + 1) // (self.d + 1)


def main():
    n, d = map(int, input().split())
    tree = Tree(n, d)
    for _ in range(n - 1):
        tree.build(*map(int, input().split()))
    print(tree.solve())


if __name__ == "__main__":
    main()

