
def add_comments_to_nginx_configuration(n, m, servers, commands):
    server_map = {ip: name for name, ip in servers}
    result = []
    for command in commands:
        command_parts = command.split()
        ip = command_parts[1][:-1]  # Remove the last character (;) to get the ip
        name = server_map[ip]
        result.append(f"{command} #{name}")
    return result

# Input
n, m = map(int, input().split())
servers = [input().split() for _ in range(n)]
commands = [input().strip() for _ in range(m)]

# Output
result = add_comments_to_nginx_configuration(n, m, servers, commands)
for line in result:
    print(line)
```
