
def install_packages(num_packages, packages):
    dependencies = {}
    for package in packages:
        package_name, *deps = package.split()
        dependencies[package_name] = deps

    installed = set()
    order = []

    def dfs(package):
        if package in installed:
            return True
        if package in order:
            return False

        for dep in dependencies.get(package, []):
            if not dfs(dep):
                return False

        order.append(package)
        installed.add(package)
        return True

    for package in dependencies.keys():
        if not dfs(package):
            print("cannot be ordered")
            return

    print("\n".join(order[::-1]))

# Read input
while True:
    num_packages = int(input())
    if num_packages == 0:
        break

    packages = [input() for _ in range(num_packages)]
    install_packages(num_packages, packages)
    print()

