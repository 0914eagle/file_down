
def add_comments_to_nginx_config(n, m, servers, commands):
    ip_to_name = {ip: name for name, ip in servers}
    for command in commands:
        command_parts = command.split()
        ip = command_parts[1][:-1]
        name = ip_to_name[ip]
        print(f"{command.rstrip()} #{name}")

# Read input
n, m = map(int, input().split())
servers = [input().split() for _ in range(n)]
commands = [input() for _ in range(m)]

# Call the function and print the output
add_comments_to_nginx_config(n, m, servers, commands)
```
