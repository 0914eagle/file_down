
def install_packages(n, packages):
    graph = {}
    indegree = {}
    order = []
    
    for package, dependencies in packages:
        graph[package] = dependencies
        indegree[package] = 0
    
    for package, dependencies in packages:
        for dep in dependencies:
            indegree[dep] += 1
    
    queue = [package for package in graph if indegree[package] == 0]
    
    while queue:
        package = queue.pop(0)
        order.append(package)
        
        for dep_package, dep_dependencies in graph.items():
            if package in dep_dependencies:
                indegree[dep_package] -= 1
                if indegree[dep_package] == 0:
                    queue.append(dep_package)
    
    if len(order) == len(graph):
        return order
    else:
        return "cannot be ordered"

# Read input
while True:
    n = int(input())
    if n == 0:
        break
    
    packages = []
    for _ in range(n):
        package_info = input().split()
        package = package_info[0]
        dependencies = package_info[1:]
        packages.append((package, dependencies))
    
    result = install_packages(n, packages)
    
    for package in result:
        print(package)
    print()

