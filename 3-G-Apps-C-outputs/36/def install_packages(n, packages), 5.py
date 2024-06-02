
def install_packages(n, packages):
    graph = {}
    indegree = {}
    order = []
    
    for package in packages:
        name, *dependencies = package.split()
        graph[name] = dependencies
        indegree[name] = 0
    
    for package in graph:
        for dependency in graph[package]:
            indegree[dependency] += 1
    
    queue = [package for package in graph if indegree[package] == 0]
    
    while queue:
        queue.sort()
        current = queue.pop(0)
        order.append(current)
        
        for package in graph:
            if current in graph[package]:
                indegree[package] -= 1
                if indegree[package] == 0:
                    queue.append(package)
    
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
        packages.append(input())
    
    result = install_packages(n, packages)
    
    for package in result:
        print(package)
    
    print()

