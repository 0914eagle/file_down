
def sort_tickets(input_list):
    n = input_list[0]
    tickets = input_list[1:]
    tickets.sort()
    return ' '.join(map(str, tickets))


input_str = input().strip()
input_list = list(map(int, input_str.split()))

print(sort_tickets(input_list))
```
