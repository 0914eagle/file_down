
def install_packages(num_packages, packages):
    graph = {}
    in_degree = {}
    result = []
    
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
        queue.sort()
        current_package = queue.pop(0)
        result.append(current_package)
        
        for package in graph:
            if current_package in graph[package]:
                in_degree[package] -= 1
                if in_degree[package] == 0:
                    queue.append(package)
    
    if len(result) == len(graph):
        return result
    else:
        return "cannot be ordered"

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

