
def total_shares_held(C, company_records):
    day_shares = {}
    
    for records in company_records:
        for shares, day in records:
            if day in day_shares:
                day_shares[day] += shares
            else:
                day_shares[day] = shares
    
    sorted_days = sorted(day_shares.keys())
    
    for day in sorted_days:
        print(day_shares[day], end=' ')

# Input parsing
C = int(input())
company_records = []
for _ in range(C):
    K = int(input())
    records = []
    for _ in range(K):
        N, D = map(int, input().split())
        records.append((N, D))
    company_records.append(records)

total_shares_held(C, company_records)
```
