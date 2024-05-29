
def add_comments(n, m, servers, commands):
    server_dict = {server[1]: server[0] for server in servers}
    for command in commands:
        command_parts = command.split()
        ip = command_parts[1][:-1]
        name = server_dict[ip]
        print(f"{command} #{name}")

# Input
n, m = map(int, input().split())
servers = [input().split() for _ in range(n)]
commands = [input() for _ in range(m)]

# Output
add_comments(n, m, servers, commands)
```
