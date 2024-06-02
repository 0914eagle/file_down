
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
        package = queue.pop(0)
        order.append(package)
        
        for dependent_package in graph:
            if package in graph[dependent_package]:
                indegree[dependent_package] -= 1
                if indegree[dependent_package] == 0:
                    queue.append(dependent_package)
    
    if len(order) != len(graph):
        return 'cannot be ordered'
    
    return order

test_cases = []
while True:
    n = int(input())
    if n == 0:
        break
    packages = [input() for _ in range(n)]
    test_cases.append((n, packages))

for i, (n, packages) in enumerate(test_cases):
    result = install_packages(n, packages)
    print('\n'.join(result))
    if i < len(test_cases) - 1:
        print()
