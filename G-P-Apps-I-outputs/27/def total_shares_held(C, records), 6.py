
def total_shares_held(C, records):
    days = set()
    for r in records:
        for shares, day in r:
            days.add(day)
    
    total_shares = {day: 0 for day in sorted(days)}
    
    for r in records:
        for shares, day in r:
            total_shares[day] += shares
    
    return " ".join(str(total_shares[day]) for day in sorted(total_shares))

# Input parsing
C = int(input())
records = []
for _ in range(C):
    K = int(input())
    company_records = []
    for _ in range(K):
        N, D = map(int, input().split())
        company_records.append((N, D))
    records.append(company_records)

# Call the function and print the output
print(total_shares_held(C, records))
```
