
def add_comments(n, m, servers, commands):
    server_map = {ip: name for name, ip in servers}
    for command in commands:
        command_parts = command.split()
        ip = command_parts[-1][:-1]  # Remove the semicolon at the end
        name = server_map[ip]
        print(f"{command} #{name}")


# Read input
n, m = map(int, input().split())
servers = [input().split() for _ in range(n)]
commands = [input() for _ in range(m)]

# Call the function
add_comments(n, m, servers, commands)
```
