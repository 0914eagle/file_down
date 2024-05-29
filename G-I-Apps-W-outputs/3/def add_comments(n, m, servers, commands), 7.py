
def add_comments(n, m, servers, commands):
    ip_to_name = {ip: name for name, ip in servers}
    
    for command in commands:
        command_parts = command.split()
        ip = command_parts[-1][:-1]  # Extract the ip from the command
        name = ip_to_name[ip]
        print(f"{command} #{name}")

# Input processing
n, m = map(int, input().split())
servers = [input().split() for _ in range(n)]
commands = [input() for _ in range(m)]

# Call the function with the provided inputs
add_comments(n, m, servers, commands)
```
