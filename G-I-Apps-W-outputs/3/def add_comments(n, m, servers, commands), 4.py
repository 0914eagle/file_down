
def add_comments(n, m, servers, commands):
    server_dict = {ip: name for name, ip in servers}
    
    for command in commands:
        command_parts = command.split()
        ip = command_parts[-1][:-1]
        name = server_dict[ip]
        print(f"{command} #{name}")

# Input parsing
n, m = map(int, input().split())
servers = [input().split() for _ in range(n)]
commands = [input() for _ in range(m)]

add_comments(n, m, servers, commands)
```
