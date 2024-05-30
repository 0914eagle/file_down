
def calculate_total_shares():
    C = int(input())
    share_records = {}

    for _ in range(C):
        K = int(input())
        for _ in range(K):
            N, D = map(int, input().split())
            if D in share_records:
                share_records[D] += N
            else:
                share_records[D] = N

    sorted_days = sorted(share_records.keys())
    for day in sorted_days:
        print(share_records[day], end=" ")

calculate_total_shares()
```
