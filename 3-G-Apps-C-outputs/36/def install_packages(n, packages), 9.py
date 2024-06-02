
def install_packages(n, packages):
    graph = {}
    indegree = {}
    order = []
    
    for package in packages:
        package_name, dependencies = package.split(' ', 1)
        dependencies = dependencies.split()
        
        graph[package_name] = dependencies
        indegree[package_name] = 0
    
    for package_name, dependencies in graph.items():
        for dependency in dependencies:
            indegree[dependency] += 1
    
    queue = [package_name for package_name in graph if indegree[package_name] == 0]
    
    while queue:
        queue.sort()
        package_name = queue.pop(0)
        order.append(package_name)
        
        for dependent_package in graph[package_name]:
            indegree[dependent_package] -= 1
            if indegree[dependent_package] == 0:
                queue.append(dependent_package)
    
    if len(order) == len(graph):
        return order
    else:
        return 'cannot be ordered'

# Read input and process test cases
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

