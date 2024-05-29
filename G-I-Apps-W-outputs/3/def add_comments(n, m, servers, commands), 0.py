
def add_comments(n, m, servers, commands):
    server_dict = {ip: name for name, ip in servers}
    
    for command in commands:
        parts = command.strip().split()
        ip = parts[-1][:-1]
        name = server_dict[ip]
        print(f"{parts[0]} {parts[1]}; #{name}")

# Read input
n, m = map(int, input().split())
servers = [input().split() for _ in range(n)]
commands = [input() for _ in range(m)]

# Call the function with input values
add_comments(n, m, servers, commands)
```
