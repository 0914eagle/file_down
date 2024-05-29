
def add_comments(n, m, servers, commands):
    server_dict = {ip: name for name, ip in servers}
    for command in commands:
        parts = command.split()
        ip = parts[1][:-1]
        name = server_dict[ip]
        print(f"{parts[0]} {parts[1]} # {name}")

# Example input
n = 2
m = 2
servers = [("main", "192.168.0.2"), ("replica", "192.168.0.1")]
commands = ["block 192.168.0.1;", "proxy 192.168.0.2;"]
add_comments(n, m, servers, commands)
```
