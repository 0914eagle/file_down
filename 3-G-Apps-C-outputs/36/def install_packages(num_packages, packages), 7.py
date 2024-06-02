
def install_packages(num_packages, packages):
    graph = {}
    dependencies = {}
    installed = set()
    order = []

    for package in packages:
        package_name, *deps = package.split()
        graph[package_name] = deps
        dependencies[package_name] = set(deps)

    def dfs(node):
        if node in installed:
            return
        if node in dependencies:
            for dep in dependencies[node]:
                if dep not in installed:
                    dfs(dep)
        installed.add(node)
        order.append(node)

    for package in graph.keys():
        dfs(package)

    if len(order) != len(graph):
        return "cannot be ordered"
    else:
        return order

# Read input
while True:
    num_packages = int(input())
    if num_packages == 0:
        break
    packages = [input() for _ in range(num_packages)]

    result = install_packages(num_packages, packages)
    for package in result:
        print(package)
    print()

