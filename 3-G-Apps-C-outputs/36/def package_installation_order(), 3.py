
def package_installation_order():
    def dfs(node):
        visited[node] = 1
        for neighbor in graph[node]:
            if visited[neighbor] == 0:
                if not dfs(neighbor):
                    return False
            elif visited[neighbor] == 1:
                return False
        visited[node] = 2
        order.insert(0, node)
        return True

    while True:
        n = int(input())
        if n == 0:
            break

        packages = []
        graph = {}
        for _ in range(n):
            package, *dependencies = input().split()
            packages.append(package)
            graph[package] = dependencies

        order = []
        visited = {package: 0 for package in packages}

        for package in packages:
            if visited[package] == 0:
                if not dfs(package):
                    print("cannot be ordered")
                    break
        else:
            print('\n'.join(order))

        print()

package_installation_order()
