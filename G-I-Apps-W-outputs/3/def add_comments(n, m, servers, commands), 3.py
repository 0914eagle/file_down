
def add_comments(n, m, servers, commands):
    server_map = {server_ip: name for name, server_ip in servers}

    for command in commands:
        parts = command.split()
        ip = parts[-1][:-1]
        name = server_map[ip]
        print(f"{parts[0]} {ip}; #{name}")

# Read input
n, m = map(int, input().split())
servers = [input().split() for _ in range(n)]
commands = [input() for _ in range(m)]

# Call the function
add_comments(n, m, servers, commands)
```
