
def install_packages(num_packages, packages):
    graph = {}
    in_degree = {}
    order = []

    for package in packages:
        package_name, dependencies = package.split(' ', 1)
        dependencies = dependencies.split()
        graph[package_name] = dependencies
        in_degree[package_name] = 0

    for package in graph:
        for dependency in graph[package]:
            in_degree[dependency] += 1

    queue = [package for package in graph if in_degree[package] == 0]

    while queue:
        package = queue.pop(0)
        order.append(package)

        for dependent_package in graph[package]:
            in_degree[dependent_package] -= 1
            if in_degree[dependent_package] == 0:
                queue.append(dependent_package)

    if len(order) == len(graph):
        return order
    else:
        return 'cannot be ordered'

# Read input
while True:
    num_packages = int(input())
    if num_packages == 0:
        break

    packages = []
    for _ in range(num_packages):
        packages.append(input())

    result = install_packages(num_packages, packages)

    for package in result:
        print(package)

    print()

