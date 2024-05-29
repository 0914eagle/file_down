
def add_server_names_to_commands(n, m, servers, commands):
    server_map = {ip: name for name, ip in servers}
    result = []
    for command in commands:
        command_parts = command.strip().split()
        ip = command_parts[1].strip(' ;')
        name = server_map[ip]
        result.append(f"{command.strip()} #{name}")
    return result

# Input
n, m = map(int, input().split())
servers = [input().split() for _ in range(n)]
commands = [input() for _ in range(m)]

# Output
result = add_server_names_to_commands(n, m, servers, commands)
for line in result:
    print(line)
```
